---
name: Broadsheet audit
description: High-contrast black-and-white broadsheet with serif body text, ruled data tables, summary strips, execution waterfalls, and restrained semantic tinting.
colors:
  primary: "#000000"
  on-primary: "#ffffff"
  background: "#ffffff"
  on-background: "#000000"
  surface: "#ffffff"
  on-surface: "#000000"
  outline: "#000000"
  secondary: "#1e7d3c"
  tertiary: "#b3261e"
  success: "#1e7d3c"
  success-container: "#dff3e4"
  error: "#b3261e"
  error-container: "#f9e2df"
  neutral-variant: "#333333"
  neutral-subtle: "#555555"
  surface-intermediate: "#bbbbbb"
  trace-secondary: "#666666"
  trace-grid: "#dddddd"
typography:
  h1:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 22.5px
    fontWeight: 400
    lineHeight: 1.2
  h2:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 16.2px
    fontWeight: 400
    lineHeight: 1.3
  h3:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 14.2px
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 14.5px
    fontWeight: 400
    lineHeight: 1.45
  meta:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 12.8px
    fontWeight: 400
    lineHeight: 1.4
  caption:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 12.3px
    fontWeight: 400
    lineHeight: 1.4
  metric-value:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 24.6px
    fontWeight: 400
    lineHeight: 1.1
  metric-label:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 11.3px
    fontWeight: 400
    lineHeight: 1.3
  table:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: 12.5px
    fontWeight: 400
    lineHeight: 1.35
  code:
    fontFamily: 'Menlo, Consolas, monospace'
    fontSize: 11.9px
    fontWeight: 400
    lineHeight: 1.4
  waterfall-label:
    fontFamily: 'Menlo, Consolas, monospace'
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
rounded:
  none: 0px
spacing:
  unit: 4px
  margin-page: 24px
  max-width: 1180px
  max-width-narrow: 960px
  padding-cell: 4px 7px
components:
  table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  metric-strip:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
  status-gap:
    backgroundColor: "{colors.error-container}"
    textColor: "{colors.error}"
  status-ok:
    backgroundColor: "{colors.success-container}"
    textColor: "{colors.success}"
  code-block:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
  waterfall-trace-primary:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.none}"
  waterfall-trace-network:
    backgroundColor: "{colors.surface-intermediate}"
    rounded: "{rounded.none}"
---

# Broadsheet audit

## Overview

![Broadsheet audit preview](preview.png)

A high-density, black-and-white editorial layout designed for system audits, technical disclosures, performance benchmarks, and diagnostic reporting. The aesthetic draws from traditional newspaper broadsheets and classical type specimens: stark black rules, serif prose, dense metric strips, inverted table headers, and sharp unrounded geometry.

This design enforces radical conciseness and data density. Interfaces built with this system must present hard data: raw counts, exact latency distributions (P50, P95, P99), discrete pipeline states, and error percentages. It strictly prohibits AI copy tropes, promotional framing, and conversational summaries. The page functions as an audit ledger where data density and visual hierarchy eliminate the need for multi-paragraph prose.

Use this design for technical reports, architectural audits, execution waterfalls, deep-dive postmortems, and complex inventories. It excels when the reader needs to digest large volumes of interconnected technical information quickly without decorative friction. The layout uses zero drop shadows, zero card elevations, and zero decorative icons. Pure black ink on white paper commands the page, while color appears solely as targeted semantic tinting for passing and failing states.

## Colors

The palette is rooted in strict monochrome contrast with restrained functional accents for diagnostic status.

### Primary
- **Ink Black (`#000000`):** Body text, heading dividers, table borders, table header backgrounds, waterfall compute spans, and diagram linework.
- **Pure White (`#ffffff`):** Page background, table cells, and inverted text on table headers.

### Secondary
- **Forest Green (`#1e7d3c`):** Covered, passing, or verified audit state text. Paired with Pale Mint (`#dff3e4`) for cell backgrounds.

### Tertiary
- **Crimson Red (`#b3261e`):** Deficit, gap, error, or missing state text. Paired with Pale Rose (`#f9e2df`) for cell backgrounds.

### Neutral & surface
- **Charcoal (`#333333`):** Subdued secondary labels, waterfall timing figures, and captions.
- **Muted Grey (`#555555`):** Inactive state text and waterfall axis ticks.
- **Mid Grey (`#bbbbbb`):** Intermediate timeline bars and network round-trip spans.
- **Dark Grey (`#666666`):** Secondary trace spans (such as embedding or parsing steps).
- **Fine Rule Grey (`#dddddd`):** Vertical time gridlines in execution waterfalls.

| Token | Name | Value | Role |
| --- | --- | --- | --- |
| `primary` | Ink black | `#000000` | Text, rules, borders, table headers, and compute spans |
| `background` | Pure white | `#ffffff` | Document background and base table cell surface |
| `on-primary` | Inverted white | `#ffffff` | Table header text and inverted bar text |
| `outline` | Ink rule | `#000000` | Structural borders, grid lines, and section underlines |
| `secondary` | Forest green | `#1e7d3c` | Verified status text |
| `success-container` | Pale mint | `#dff3e4` | Verified status cell background |
| `tertiary` | Crimson red | `#b3261e` | Gap status text |
| `error-container` | Pale rose | `#f9e2df` | Gap status cell background |
| `neutral-variant` | Charcoal | `#333333` | Metric labels, timing readouts, and secondary captions |
| `neutral-subtle` | Muted grey | `#555555` | Dormant states and axis markings |
| `surface-intermediate` | Mid grey | `#bbbbbb` | Intermediate timeline bars and network latency spans |
| `trace-secondary` | Dark grey | `#666666` | Secondary trace operations |
| `trace-grid` | Fine rule grey | `#dddddd` | Time interval vertical gridlines |

Do not add decorative gradients or colored header banners. Color exists only to signal compliance or deficits in tabular data.

### Texture and patterns

The design uses an SVG diagonal hatch pattern for storage and database operations in waterfalls:
- Pattern definition: 5px × 5px unit rotated 45 degrees (`patternTransform="rotate(45)"`).
- Hatch stroke: 2px solid black line on white fill.
- CSS fallback: `repeating-linear-gradient(45deg, #000 0 2px, #fff 2px 5px)`.

## Typography

The design relies entirely on standard system serif and monospace font stacks without remote font downloads:
- **Serif stack:** `Georgia, "Times New Roman", serif`
- **Monospace stack:** `Menlo, Consolas, monospace`

| Role | Family | Size / Leading | Weight & Treatment |
| --- | --- | --- | --- |
| Document title (`h1`) | Serif | 22.5px / 1.2 | 400 normal, 2px solid bottom rule |
| Section title (`h2`) | Serif | 16.2px / 1.3 | 400 normal, 1px solid bottom rule |
| Subheading (`h3`) | Serif | 14.2px / 1.3 | 700 bold |
| Body text | Serif | 14.5px / 1.45 | 400 normal |
| Metadata note | Serif | 12.8px / 1.4 | 400 normal |
| Caption note | Serif | 12.3px / 1.4 | 400 normal, charcoal (`#333333`) |
| Section navigation | Serif | 12.5px / 1.4 | 400 normal, unadorned links |
| Metric number | Serif | 24.6px / 1.1 | 400 normal |
| Metric label | Serif | 11.3px / 1.3 | 400 normal, charcoal (`#333333`) |
| Table text | Serif | 12.5px / 1.35 | 400 normal, wraps anywhere |
| Detail table text | Serif | 11.3px / 1.3 | 400 normal, compact inspection |
| Code & pre | Monospace | 11.9px / 1.4 | 400 normal |
| Timeline bar | Serif | 10.4px / 1.2 | 400 normal |
| Waterfall label | Monospace | 11px / 1.2 | 400 normal |

Headings remain normal weight (`font-weight: 400`), distinguished by scale and solid black bottom rules rather than heavy bolding. Subheadings use bold serif at 14.2px for crisp inline demarcation. Eliminate em dashes, marketing buzzwords, and promotional adverbs throughout the microcopy.

## Layout

The document follows a single-column broadsheet flow centered within a container capped between `960px` (benchmarks and waterfalls) and `1180px` (broad tables and audits):

1. **Document title:** Single line header with a 2px solid black underline.
2. **Metadata banner:** Concise dateline and scope description.
3. **Anchor navigation bar:** Flat inline list of internal jump links.
4. **Metric summary strip:** Ruled KPI block summarizing key counts and statistics.
5. **Inline status legend:** Compact row of swatches identifying status fills.
6. **Narrative & structured tables:** Alternating analysis prose, dense data tables, and latency benchmarks.
7. **Execution waterfalls:** SVG timeline charts tracking hierarchical execution spans.
8. **Collapsible details:** Native `<details>` containers for supplementary inventories and raw audits.

The page container has `2.5rem` to `3rem` top and bottom margins and `1.5rem` horizontal padding.

### Responsive breakpoints

| Viewport Width | Adjustments |
| --- | --- |
| Above 900px | 6-column metric strip, 2-column comparative layout, 190px timeline row labels |
| 900px and below | 3-column metric strip, single-column stacked layout, 120px timeline row labels, timeline bar text scales to 0.6rem |

All data tables and diagrams sit inside an overflow wrapper (`overflow-x: auto`) with `margin: 0.4rem 0 1rem` to ensure responsive scrolling on narrow viewports without breaking page layout.

## Elevation & depth

The design is completely flat. No box shadows, elevations, or layered backdrops are permitted.

Depth and structure are communicated through:
- **Ink rule thickness:** 2px rules indicate major document boundaries; 1px rules mark internal table cells and section headings.
- **Value inversion:** Solid black table header cells (`background: #000; color: #fff`) create strong visual anchors for columns.
- **Tonal washes:** Soft red and green tints separate evaluated states from neutral rows without breaking the typographic plane.

## Shapes

Geometry is strictly rectilinear:
- **Corners:** Every element uses `border-radius: 0px`. This includes tables, buttons, metric blocks, code containers, timeline bars, and legend swatches.
- **Borders:**
  - 2px solid black: Document title underline, metric strip frame, timeline matrix outer frame.
  - 1px solid black: Section underlines, table cells, code blocks, diagram containers, legend swatches, and timeline bars.

## Components

### Metric summary strip

A continuous 6-column grid displaying key counts and high-level measurements:
- Container: `border: 2px solid #000000; margin: 0.8rem 0 1.4rem`.
- Internal dividers: `1px solid #000000` vertical rules between cells.
- Padding: `0.5rem 0.7rem` per cell.
- Value typography: `24.6px` serif, line height `1.1`. Must display raw verified integers or calibrated seconds.
- Label typography: `11.3px` serif, charcoal (`#333333`). Must name the exact system entity without fluff.
- Mobile breakpoint: Collapses into 3 columns on viewports at or below 900px.

### Ruled data tables

Dense information tables built for rapid scanning:
- Framework: `border-collapse: collapse; width: 100%; font-size: 12.5px`.
- Cells: `border: 1px solid #000000; padding: 0.25rem 0.45rem`.
- Cell wrapping: `overflow-wrap: anywhere; max-width: 34ch`.
- Table header (`th`): `background: #000000; color: #ffffff; font-weight: normal; text-align: left`.
- Numeric cells (`td.n`): `text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums`.
- Key-value tables (`table.kv`): First column fixed at `22%` width with bold text.
- Collapsible detail tables: Formatted at `11.3px` font size with `28ch` max cell width.

### Status cells

Targeted semantic highlights applied directly to table cells:
- **Pass / Covered (`.cell-ok`):** Background `#dff3e4`, bold forest green text (`#1e7d3c`).
- **Gap / Missing (`.cell-gap`):** Background `#f9e2df`, bold crimson red text (`#b3261e`).
- **Neutral / Partial (`.cell-part`):** Pure white background (`#ffffff`).

### Execution trace waterfall (Signature Component)

An SVG timeline chart representing multi-step execution traces, latency bottlenecks, and nested parent nodes:
- Dimensions: `viewBox="0 0 900 H"`, width `100%`, inline styles using `font: 11px Menlo, Consolas, monospace`.
- Time axis gridlines: Fine `1px stroke="#dddddd"` vertical rules spaced at even intervals across the chart duration, with centered time labels (`fill="#666666"`).
- Parent container spans: Dashed rect (`fill="none" stroke="#000000" stroke-dasharray="3,2"`) with bold node label at the top.
- Trace bar variants:
  - Primary compute / execution: `fill="#000000"` (solid black).
  - Secondary helper / embedding: `fill="#666666"` (dark grey).
  - Storage / database batch: `fill="url(#hatch)" stroke="#000000"` (45-degree monochrome diagonal hatch).
  - Network round trip / external API: `fill="#bbbbbb" stroke="#000000"` (mid grey with black stroke).
  - Checkpoint / state transaction: `fill="#ffffff" stroke="#000000"` (white with black stroke).
- Label positioning: Left-aligned at `x="8"` or `x="0"` with operation title. Duration readout right-aligned following the bar (`fill="#333333"`).
- Explanatory captions: Accompanying notes placed directly above or below the chart in `12.3px` serif text (`#333333`).

### Timeline matrix

A discrete execution grid mapping tasks, jobs, or pipeline stages against time intervals or states:
- Frame: `border: 2px solid #000000; padding: 0.4rem; margin: 0.8rem 0 0.3rem`.
- Grid: `grid-template-columns: 190px repeat(N, 1fr); gap: 2px`.
- Column header (`.tlh`): Centered `11.3px` text with `1px solid #000000` bottom border.
- Row label (`.tll`): Left-aligned `11.9px` text spanning the first column.
- Segment bars (`.bar`): `1px solid #000000` border, `0.3rem 0.4rem` padding, single-line truncated text:
  - Active (`.build`): Black background, white text.
  - Intermediate (`.warm`): Mid-grey background (`#bbbbbb`), black text.
  - Inactive (`.off`): White background, muted grey text (`#555555`).

### Anchor navigation

Flat, unobtrusive link bar placed under the masthead metadata:
- Font: `12.5px` serif.
- Links: Black text without underlines at rest (`color: #000000; margin-right: 0.9rem`).
- Underlines appear on hover.

### Code and preformatted blocks

- Font: `11.9px / 1.4 Menlo, Consolas, monospace`.
- Container: `border: 1px solid #000000; padding: 0.5rem 0.7rem; overflow-x: auto; background: #ffffff`.

### Linear diagrams

Mermaid or SVG process flows rendered in pure black and white:
- Container: `border: 1px solid #000000; padding: 0.6rem; overflow-x: auto; margin: 0.4rem 0 1rem`.
- Flowchart theme:
  - Node fill: `#ffffff`.
  - Node text and borders: `#000000` with 1px stroke.
  - Connector lines: `#000000` solid or dotted.
  - Font family: `Georgia, serif` at 12px.
  - Curves: strictly `linear` (orthogonal, no curved spline interpolation).

### Status legend

- Container: Inline row with `11.9px` text and `1rem` right margins.
- Swatches (`.sw`): `12px × 10px` or `14px × 10px` rectangular blocks with `1px solid #000000` border and `4px` right margin.

## Do's and Don'ts

- **Do** present verified metrics, error rates, and latency numbers directly in ruled tables and summary strips.
- **Do** label execution trace bars with exact operation names and millisecond durations.
- **Do** use pure black rules (`#000000`) on white backgrounds (`#ffffff`) for crisp broadsheet contrast.
- **Do** wrap every data table and SVG waterfall in an `overflow-x: auto` container to maintain responsive legibility.
- **Do** right-align all numeric data and set `white-space: nowrap` on numeric cells.
- **Do** use strict 0px unrounded corners on all borders, containers, and table cells.
- **Do** reserve color exclusively for semantic pass and fail diagnostic cells.
- **Do** set table headers with solid black backgrounds and white unbolded text.
- **Don't** write explanatory introductory paragraphs that restate what the table or waterfall already shows.
- **Don't** use em dashes, exclamation points, or decorative conversational preambles.
- **Don't** add drop shadows, blur filters, or floating card components.
- **Don't** use decorative icons, colorful badges, or rounded pill tags.
- **Don't** import web fonts; rely on system serif (`Georgia, "Times New Roman", serif`) and monospace stacks.
- **Don't** use curved bezier lines in architectural diagrams; use orthogonal linear connectors.
- **Don't** add animated entrances, transitions, or hover movements.
