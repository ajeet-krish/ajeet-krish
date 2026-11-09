"""Generate self-contained SVG figures for the GitHub profile README.

Fetches contribution and language data from the GitHub GraphQL API and
renders four SVG files (two figures, each in dark and light theme) into
the output directory.

Environment variables:
    GITHUB_TOKEN  GitHub API token (preferred).
    GH_TOKEN      Fallback token if GITHUB_TOKEN is unset.
    OUT_DIR       Output directory for the SVG files. Default: "dist".
    GH_USER       GitHub login to fetch. Default: "ajeet-krish".

Usage:
    GITHUB_TOKEN=ghp_... python assets/src/build.py
    OUT_DIR=/tmp/out python assets/src/build.py
"""

from __future__ import annotations

import datetime
import json
import math
import os
import sys
import urllib.error
import urllib.request
from typing import Any

GRAPHQL_URL = "https://api.github.com/graphql"

DEFAULT_GH_USER = "ajeet-krish"
DEFAULT_OUT_DIR = "dist"

FONT_FAMILY = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
ACCENT_COLOR = "#0A66C2"
SEGMENT_GAP_DEG = 1.5

THEMES: dict[str, dict[str, str]] = {
    "dark": {
        "bg": "#0D1117",
        "panel": "#161B22",
        "ink": "#C9D1D9",
        "rule": "#21262D",
        "muted": "#8B949E",
    },
    "light": {
        "bg": "#FFFFFF",
        "panel": "#F6F8FA",
        "ink": "#24292F",
        "rule": "#D0D7DE",
        "muted": "#6E7781",
    },
}

LEVEL_TO_QUARTILE: dict[str, int] = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}

GRID_OPACITY: dict[int, float] = {
    0: 0.08,
    1: 0.30,
    2: 0.50,
    3: 0.72,
    4: 0.95,
}

CAPTION_FIG_01 = "FIG. 01 \u00b7 COMMIT DISCRETIZATION, 52 WEEK DOMAIN \u00b7 SOURCE: GITHUB API"
CAPTION_FIG_02 = "FIG. 02 \u00b7 LANGUAGE DISTRIBUTION, BYTES OF CODE \u00b7 SOURCE: GITHUB API"

WEEKDAY_LABELS: dict[int, str] = {1: "MON", 3: "WED", 5: "FRI"}


class BuildError(Exception):
    """Raised when the API response is missing required data."""


GRAPHQL_QUERY = """
query ProfileFigures($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
            contributionLevel
          }
        }
      }
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      nodes {
        languages(first: 10) {
          edges {
            size
            node {
              name
              color
            }
          }
        }
      }
    }
  }
}
"""


def read_env(name: str, default: str) -> str:
    """Read an environment variable, falling back to a default."""
    value = os.environ.get(name, "")
    return value if value.strip() else default


def escape_xml(text: str) -> str:
    """Escape a string for use in XML text or attribute values."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def fetch_graphql(token: str, gh_user: str) -> dict[str, Any]:
    """Run a single GraphQL query and return the decoded JSON payload."""
    payload = json.dumps({"query": GRAPHQL_QUERY, "variables": {"login": gh_user}}).encode("utf-8")
    request = urllib.request.Request(  # noqa: S310 (GitHub API endpoint is fixed)
        GRAPHQL_URL,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-figure-build",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")
        raise BuildError(f"GraphQL HTTP {error.code}: {detail}") from error
    except urllib.error.URLError as error:
        raise BuildError(f"GraphQL request failed: {error.reason}") from error

    decoded: Any = json.loads(body)
    if not isinstance(decoded, dict):
        raise BuildError("GraphQL response is not a JSON object")

    errors = decoded.get("errors")
    if errors:
        raise BuildError(f"GraphQL errors: {json.dumps(errors)}")

    data = decoded.get("data")
    if not isinstance(data, dict):
        raise BuildError("GraphQL response has no data object")
    return data


def require_mapping(value: Any, path: str) -> dict[str, Any]:
    """Return value as a dict or fail loudly with the path that is missing."""
    if not isinstance(value, dict):
        raise BuildError(f"missing object at {path}")
    return value


def require_list(value: Any, path: str) -> list[Any]:
    """Return value as a list or fail loudly with the path that is missing."""
    if not isinstance(value, list):
        raise BuildError(f"missing array at {path}")
    return value


def extract_contribution_weeks(data: dict[str, Any]) -> list[list[tuple[str, int]]]:
    """Flatten the contribution calendar into weeks of (date, quartile) pairs.

    The API returns weeks column-major; the first and last week may hold
    fewer than seven days, so the week structure is preserved.
    """
    user = require_mapping(data.get("user"), "data.user")
    calendar = require_mapping(
        user.get("contributionsCollection"), "data.user.contributionsCollection"
    ).get("contributionCalendar")
    weeks = require_list(
        require_mapping(calendar, "data.user.contributionsCollection.contributionCalendar").get(
            "weeks"
        ),
        "data.user.contributionsCollection.contributionCalendar.weeks",
    )

    weeks_out: list[list[tuple[str, int]]] = []
    for week_index, week in enumerate(weeks):
        week_map = require_mapping(week, f"weeks[{week_index}]")
        days = require_list(
            week_map.get("contributionDays"), f"weeks[{week_index}].contributionDays"
        )
        week_days: list[tuple[str, int]] = []
        for day_index, day in enumerate(days):
            day_map = require_mapping(day, f"weeks[{week_index}].contributionDays[{day_index}]")
            date = day_map.get("date")
            if not isinstance(date, str) or not date:
                raise BuildError(f"weeks[{week_index}].contributionDays[{day_index}].date missing")
            if "contributionCount" not in day_map:
                raise BuildError(
                    f"weeks[{week_index}].contributionDays[{day_index}].contributionCount missing"
                )
            level_name = day_map.get("contributionLevel")
            if level_name not in LEVEL_TO_QUARTILE:
                raise BuildError(
                    f"weeks[{week_index}].contributionDays[{day_index}].contributionLevel "
                    f"invalid: {level_name!r}"
                )
            week_days.append((date, LEVEL_TO_QUARTILE[level_name]))
        if not week_days:
            raise BuildError(f"weeks[{week_index}] has no contribution days")
        weeks_out.append(week_days)

    if not weeks_out:
        raise BuildError("contribution calendar has no weeks")
    return weeks_out


def extract_language_totals(
    data: dict[str, Any],
) -> tuple[dict[str, int], dict[str, str]]:
    """Aggregate language byte totals and colors across owned repositories."""
    user = require_mapping(data.get("user"), "data.user")
    repositories = require_mapping(user.get("repositories"), "data.user.repositories")
    nodes = require_list(repositories.get("nodes"), "data.user.repositories.nodes")

    totals: dict[str, int] = {}
    colors: dict[str, str] = {}
    for node_index, node in enumerate(nodes):
        if node is None:
            continue
        node_map = require_mapping(node, f"repositories.nodes[{node_index}]")
        languages = require_mapping(
            node_map.get("languages"), f"repositories.nodes[{node_index}].languages"
        )
        edges = require_list(
            languages.get("edges"), f"repositories.nodes[{node_index}].languages.edges"
        )
        for edge_index, edge in enumerate(edges):
            edge_path = f"repositories.nodes[{node_index}].languages.edges[{edge_index}]"
            edge_map = require_mapping(edge, edge_path)
            size = edge_map.get("size")
            if not isinstance(size, int) or size < 0:
                raise BuildError(f"{edge_path}.size invalid: {size!r}")
            language = require_mapping(edge_map.get("node"), f"{edge_path}.node")
            name = language.get("name")
            if not isinstance(name, str) or not name:
                raise BuildError(f"{edge_path}.node.name missing")
            color = language.get("color")
            totals[name] = totals.get(name, 0) + size
            if isinstance(color, str) and color:
                colors.setdefault(name, color)

    for name, color in colors.items():
        if name not in totals:
            raise BuildError(f"language color without byte total: {name}")
    if not totals:
        raise BuildError("no language data found")
    return totals, colors


def aggregate_languages(totals: dict[str, int]) -> list[tuple[str, int]]:
    """Sort languages by bytes, keep the top six, and fold the rest into OTHER."""
    ordered = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    top = ordered[:6]
    remainder = ordered[6:]
    segments = list(top)
    if remainder:
        segments.append(("OTHER", sum(size for _, size in remainder)))
    return segments


def text_element(
    x: float, y: float, text: str, size: int, fill: str, anchor: str = "start"
) -> str:
    """Render a monospace text element."""
    return (
        f'<text x="{x:g}" y="{y:g}" font-family="{FONT_FAMILY}" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}">{escape_xml(text)}</text>'
    )


def render_contribution_grid(
    weeks: list[list[tuple[str, int]]], theme: dict[str, str]
) -> str:
    """Render FIG. 01: the contribution calendar as a plotted grid.

    Each week is one column of seven rows (Sunday to Saturday); partial
    edge weeks simply leave the unused cells as bare graph paper.
    """
    width = 800
    height = 192
    grid_left = 58.0
    grid_top = 58.0
    cell_size = 13.0
    cell_gap = 1.5
    grid_right = grid_left + 53 * cell_size
    grid_bottom = grid_top + 7 * cell_size
    ink = theme["ink"]
    rule = theme["rule"]
    muted = theme["muted"]
    panel = theme["panel"]

    parts: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="{FONT_FAMILY}">',
        f'<rect width="{width}" height="{height}" fill="{theme["bg"]}"/>',
        f'<rect x="16" y="14" width="{width - 32}" height="{height - 28}" '
        f'fill="{panel}" stroke="{rule}" stroke-width="1"/>',
    ]

    # Subtle graph paper grid.
    grid_lines: list[str] = []
    for step in range(54):
        x = grid_left + step * cell_size
        grid_lines.append(
            f'<line x1="{x:g}" y1="{grid_top:g}" x2="{x:g}" y2="{grid_bottom:g}" '
            f'stroke="{rule}" stroke-width="0.4"/>'
        )
    for step in range(8):
        y = grid_top + step * cell_size
        grid_lines.append(
            f'<line x1="{grid_left:g}" y1="{y:g}" x2="{grid_right:g}" y2="{y:g}" '
            f'stroke="{rule}" stroke-width="0.4"/>'
        )
    parts.append(f'<g opacity="0.6">{"".join(grid_lines)}</g>')

    # Month labels above the grid, at the column holding each month's first day.
    seen_months: set[str] = set()
    for column, week in enumerate(weeks[:53]):
        for date_text, _level in week:
            month = date_text[5:7]
            if month not in seen_months:
                seen_months.add(month)
                x = grid_left + column * cell_size + cell_size / 2.0
                parts.append(text_element(x, grid_top - 10, f"M{month}", 8, muted, "middle"))

    # Weekday labels along the left (rows are Sunday to Saturday).
    for weekday, label in WEEKDAY_LABELS.items():
        y = grid_top + weekday * cell_size + cell_size / 2.0 + 3.0
        parts.append(text_element(grid_left - 8, y, label, 8, muted, "end"))

    # Contribution squares with graduated ink opacity.
    for column, week in enumerate(weeks[:53]):
        for date_text, level in week:
            try:
                parsed = datetime.date.fromisoformat(date_text)
            except ValueError as error:
                raise BuildError(f"invalid contribution date: {date_text!r}") from error
            row_index = (parsed.weekday() + 1) % 7
            x = grid_left + column * cell_size
            y = grid_top + row_index * cell_size
            opacity = GRID_OPACITY[level]
            parts.append(
                f'<rect x="{x:g}" y="{y:g}" width="{cell_size - cell_gap:g}" '
                f'height="{cell_size - cell_gap:g}" fill="{ink}" fill-opacity="{opacity:g}" '
                f'stroke="{rule}" stroke-width="0.3"/>'
            )

    # Thin rule frame and engineering caption.
    parts.append(
        f'<rect x="{grid_left:g}" y="{grid_top:g}" '
        f'width="{grid_right - grid_left:g}" height="{grid_bottom - grid_top:g}" '
        f'fill="none" stroke="{ink}" stroke-width="1"/>'
    )
    parts.append(text_element(grid_left, height - 18, CAPTION_FIG_01, 9, muted))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def polar_point(cx: float, cy: float, radius: float, angle_deg: float) -> tuple[float, float]:
    """Convert a center, radius, and angle to a cartesian point."""
    angle_rad = math.radians(angle_deg)
    return cx + radius * math.cos(angle_rad), cy + radius * math.sin(angle_rad)


def arc_path(
    cx: float,
    cy: float,
    outer_radius: float,
    inner_radius: float,
    start_deg: float,
    end_deg: float,
) -> str:
    """Build a closed donut segment path from start and end angles."""
    large_arc = 1 if (end_deg - start_deg) % 360.0 > 180.0 else 0
    x1, y1 = polar_point(cx, cy, outer_radius, start_deg)
    x2, y2 = polar_point(cx, cy, outer_radius, end_deg)
    x3, y3 = polar_point(cx, cy, inner_radius, end_deg)
    x4, y4 = polar_point(cx, cy, inner_radius, start_deg)
    return (
        f"M {x1:.3f} {y1:.3f} "
        f"A {outer_radius:g} {outer_radius:g} 0 {large_arc} 1 {x2:.3f} {y2:.3f} "
        f"L {x3:.3f} {y3:.3f} "
        f"A {inner_radius:g} {inner_radius:g} 0 {large_arc} 0 {x4:.3f} {y4:.3f} Z"
    )


def render_language_donut(
    segments: list[tuple[str, int]],
    language_colors: dict[str, str],
    theme: dict[str, str],
) -> str:
    """Render FIG. 02: a donut chart of language byte share with a legend."""
    width = 480
    height = 260
    cx = 118.0
    cy = 134.0
    outer_radius = 82.0
    inner_radius = 50.0
    ink = theme["ink"]
    rule = theme["rule"]
    muted = theme["muted"]
    panel = theme["panel"]

    total = sum(size for _, size in segments)
    if total <= 0:
        raise BuildError("language byte total must be positive")

    parts: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="{FONT_FAMILY}">',
        f'<rect width="{width}" height="{height}" fill="{theme["bg"]}"/>',
        f'<rect x="16" y="14" width="{width - 32}" height="{height - 28}" '
        f'fill="{panel}" stroke="{rule}" stroke-width="1"/>',
    ]

    gap = SEGMENT_GAP_DEG if len(segments) > 1 else 0.0
    angle = -90.0
    for name, size in segments:
        sweep = 360.0 * size / total
        start = angle + gap / 2.0
        end = angle + sweep - gap / 2.0
        color = language_colors.get(name, ACCENT_COLOR)
        if end - start >= 359.9:
            # A single full circle cannot be expressed as one arc.
            parts.append(
                f'<circle cx="{cx:g}" cy="{cy:g}" r="{outer_radius:g}" '
                f'fill="{escape_xml(color)}"/>'
            )
            parts.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="{inner_radius:g}" fill="{panel}"/>')
        else:
            if end <= start:
                end = start + 0.1
            parts.append(
                f'<path d="{arc_path(cx, cy, outer_radius, inner_radius, start, end)}" '
                f'fill="{escape_xml(color)}" fill-rule="evenodd" '
                f'stroke="{theme["bg"]}" stroke-width="1"/>'
            )
        angle += sweep

    parts.append(text_element(cx, cy - 4, f"{len(segments)}", 22, ink, "middle"))
    parts.append(text_element(cx, cy + 16, "LANGS", 9, muted, "middle"))

    # Legend list at the right with language name and percent.
    legend_x = 236.0
    legend_top = 66.0
    row_step = 26.0
    for index, (name, size) in enumerate(segments):
        color = language_colors.get(name, ACCENT_COLOR)
        y = legend_top + index * row_step
        parts.append(
            f'<rect x="{legend_x:g}" y="{y - 8:g}" width="10" height="10" '
            f'fill="{escape_xml(color)}" stroke="{rule}" stroke-width="0.5"/>'
        )
        parts.append(text_element(legend_x + 18, y, name, 10, ink))
        percent = 100.0 * size / total
        parts.append(text_element(width - 40, y, f"{percent:.1f}%", 10, muted, "end"))

    parts.append(text_element(24, height - 24, CAPTION_FIG_02, 9, muted))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def write_svg(out_dir: str, file_name: str, content: str) -> None:
    """Write one SVG file into the output directory."""
    path = os.path.join(out_dir, file_name)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main() -> int:
    """Fetch GitHub data and write the four themed SVG figures."""
    token = os.environ.get("GITHUB_TOKEN", "").strip() or os.environ.get("GH_TOKEN", "").strip()
    if not token:
        print("error: GITHUB_TOKEN or GH_TOKEN must be set", file=sys.stderr)
        return 1

    gh_user = read_env("GH_USER", DEFAULT_GH_USER)
    out_dir = read_env("OUT_DIR", DEFAULT_OUT_DIR)

    try:
        data = fetch_graphql(token, gh_user)
        weeks = extract_contribution_weeks(data)
        language_totals, language_colors = extract_language_totals(data)
    except BuildError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as error:
        print(f"error: invalid JSON from GitHub API: {error}", file=sys.stderr)
        return 1

    segments = aggregate_languages(language_totals)

    os.makedirs(out_dir, exist_ok=True)

    figures: list[tuple[str, str]] = [
        ("fig-01-commit-discretization.svg", "light"),
        ("fig-01-commit-discretization-dark.svg", "dark"),
        ("fig-02-language-donut.svg", "light"),
        ("fig-02-language-donut-dark.svg", "dark"),
    ]
    try:
        for file_name, theme_name in figures:
            theme = THEMES[theme_name]
            if file_name.startswith("fig-01"):
                svg = render_contribution_grid(weeks, theme)
            else:
                svg = render_language_donut(segments, language_colors, theme)
            write_svg(out_dir, file_name, svg)
            print(f"wrote {os.path.join(out_dir, file_name)}")
    except BuildError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
