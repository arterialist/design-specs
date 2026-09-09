---
name: Systems benchmark
description: High-density system sans-serif benchmark report with shaded tabular data, executive callout boxes, and responsive sparkline telemetry grids.
colors:
  primary: "#000000"
  on-primary: "#000000"
  background: "#ffffff"
  surface: "#ffffff"
  surface-container: "#eeeeee"
  outline: "#000000"
  neutral-variant: "#333333"
typography:
  h1:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 22.4px
    fontWeight: 400
    lineHeight: 1.2
  h2:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 16.8px
    fontWeight: 400
    lineHeight: 1.3
  h3:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
  table:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
  caption:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1.3
  code:
    fontFamily: 'Menlo, Consolas, monospace'
    fontSize: 12.6px
    fontWeight: 400
    lineHeight: 1.4
rounded:
  none: 0px
spacing:
  unit: 4px
  margin-page: 16px
  max-width: 1120px
  padding-cell: 3px 6px
components:
  callout-box:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
  table-header:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  sparkline-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
---

# Systems benchmark

## Overview

![Systems benchmark preview](preview.png)

A high-density systems engineering layout built for benchmark comparisons, performance regressions, resource profiling, and hardware profiling reports. The interface pairs clean native system typography with compact tabular data, prominent callout boxes, and responsive grids of sparkline telemetry charts.

This design enforces extreme brevity, high tabular density, and concrete telemetry. It forces the interface to communicate through numbers: wall-clock durations, CPU seconds, memory allocations (RSS MB), and sparkline trends. Prose is strictly confined to constrained 80-character notes that name specific algorithmic changes and physical bottlenecks. Meaningless filler, generic recommendations, and multi-paragraph commentary are prohibited.

Use this design when presenting performance evaluations across multiple runs, configurations, or pool sizes. The visual tone is utilitarian and objective. Rather than heavy branding or decorative graphics, the layout relies on crisp 1px and 2px black rules, light neutral grey table headers, and tabular numerals to make comparisons easy to parse.

## Colors

The palette is strictly neutral, focusing on ink contrast and subtle grey surface shading.

### Primary
- **Solid Black (`#000000`):** Core body text, major 2px borders, 1px table rules, and sparkline trace lines.
- **Pure White (`#ffffff`):** Page background, table cell fill, callout box interior, and sparkline background.

### Neutral & surface
- **Header Wash Grey (`#eeeeee`):** Light neutral fill for table header rows (`th`).
- **Charcoal (`#333333`):** Small subtitles, captions, and secondary notes.

| Token | Name | Value | Role |
| --- | --- | --- | --- |
| `primary` | Solid black | `#000000` | Text, borders, dividing rules, and sparkline polyline strokes |
| `background` | Pure white | `#ffffff` | Page background, table cells, and sparkline canvas |
| `surface` | Pure white | `#ffffff` | Callout box and card surfaces |
| `surface-container` | Header wash grey | `#eeeeee` | Shaded table header backgrounds |
| `outline` | Solid rule | `#000000` | Borders for tables, boxes, and sparkline frames |
| `neutral-variant` | Charcoal | `#333333` | Subtitles, figure labels, and footnotes |

Do not add colored status pills, gradient fills, or accent colors. High-contrast monochrome rules ensure clean reproduction across screens and print.

## Typography

The typography uses the operating system's native sans-serif stack paired with a monospace font for identifiers and code:
- **System sans stack:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- **Monospace stack:** `Menlo, Consolas, monospace`

| Role | Family | Size / Leading | Weight & Treatment |
| --- | --- | --- | --- |
| Document title (`h1`) | Sans | 22.4px / 1.2 | 400 normal, 2px solid bottom rule |
| Section title (`h2`) | Sans | 16.8px / 1.3 | 400 normal, 1px solid bottom rule |
| Subheading (`h3`) | Sans | 14px / 1.3 | 700 bold |
| Body text | Sans | 14px / 1.45 | 400 normal, capped at 80ch |
| Table text | Sans | 14px / 1.4 | 400 normal, tabular numbers |
| Table caption | Sans | 14px / 1.4 | 400 normal, italic |
| Figure caption | Sans | 11.2px / 1.3 | 400 normal |
| Small footnote | Sans | 11.5px / 1.3 | 400 normal, charcoal (`#333333`) |
| Code & pre | Monospace | 12.6px / 1.4 | 400 normal |

Numeric data in tables and sparklines uses `font-variant-numeric: tabular-nums` so numbers align reliably in vertical columns. Microcopy must remain objective and brief. Eliminate em dashes and marketing adverbs.

## Layout

The document centers inside a `1120px` max-width container with `2rem` vertical margins and `1rem` horizontal padding:

1. **Document title:** Single line header with a 2px solid black underline.
2. **Executive callout box:** Ruled container highlighting top-line speedups and resource reductions.
3. **Context & narrative:** Structured sections with an 80-character reading line limit (`max-width: 80ch`).
4. **Benchmark summary tables:** Dense data tables with right-aligned numeric figures.
5. **Sparkline telemetry grid:** Multi-column responsive grid of small-multiples resource charts.
6. **Detailed analysis lists:** Numbered or bulleted findings with bold inline lead-ins.
7. **Collapsible details:** Native `<details>` tags housing secondary datasets and raw runs.

### Responsive breakpoints

| Viewport Width | Adjustments |
| --- | --- |
| Above 720px | Multi-column sparkline grid (`repeat(auto-fill, minmax(340px, 1fr))`) |
| 720px and below | Sparkline grid stacks into a single column, horizontal table scroll enabled |

All tables maintain horizontal overflow protection through parent scroll wrappers.

## Elevation & depth

Surfaces are strictly flat. The layout uses no box shadows, elevation layers, or blur effects.

Depth and hierarchy rely on:
- **Rule weight hierarchy:** 2px rules define document headers and executive callout frames. 1px rules enclose tables, sparkline cells, and section breaks.
- **Tonal shading:** Shaded `#eeeeee` table headers create clear separation between column labels and data rows.
- **Framed containers:** Distinct `.box` callouts separate executive findings from general narrative flow.

## Shapes

Geometry is strictly rectilinear:
- **Corners:** Every element uses `border-radius: 0px`. This applies to callout boxes, table borders, sparkline chart frames, and code blocks.
- **Stroke rules:**
  - 2px solid black: Title bottom rule and executive callout box border.
  - 1px solid black: Section bottom rules, table cell borders, and sparkline SVG borders.

## Components

### Executive callout box

A prominent container placed near the top of the report to display critical findings, key metrics, and recommended settings:
- Border: `2px solid #000000`.
- Padding: `0.8rem 1rem 1rem`.
- Margin: `1rem 0 2rem`.
- Title: `h2` inside the box with `margin-top: 0; border: 0` to eliminate duplicate dividing rules.
- Content rule: State verified performance multipliers (such as `18x lower CPU` or `151s down to 35s`) and concrete recommendations directly. Never add greeting text, introductory throat-clearing, or conversational commentary.

### Shaded benchmark tables

Compact tabular structures optimized for comparing benchmarks across workloads and configurations:
- Framework: `border-collapse: collapse; width: 100%; margin: 0.6rem 0`.
- Borders: `1px solid #000000` on all cells.
- Padding: `3px 6px` per cell.
- Header (`th`): Filled with `#eeeeee`, normal font weight, 1px solid black border.
- Text alignment:
  - First column (`th:first-child`, `td:first-child`, `td.l`): Left-aligned for workload names or metrics.
  - Value columns (`td`, `th`): Right-aligned with `font-variant-numeric: tabular-nums`.
- Captions: Placed above the table, left-aligned, set in italic text (`font-style: italic`).

### Sparkline telemetry grid (Signature Component)

A small-multiples grid of compact SVG sparklines tracking memory, CPU, or latency over time:
- Grid layout: `display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 1rem`.
- Figure container: `margin: 0`.
- Caption (`figcaption`): Top label set at `11.2px` with monospace test names (`code`) and explicit peak value annotations.
- SVG chart frame:
  - Dimensions: `width="340" height="56" viewBox="0 0 340 56"`.
  - Border: `1px solid #000000; display: block; margin-top: 2px`.
  - Background: Pure white (`#ffffff`).
  - Plot stroke: `polyline` with `fill="none" stroke="#000000" stroke-width="1"`.
- Multi-run comparison: Supports placing multiple figures side-by-side to visually identify memory leaks, plateaus, and spikes.

### Narrative notes blocks

Constrained reading passages for technical explanations and postmortem context:
- Container class: `.notes`.
- Line width: Constrained to `max-width: 80ch` on paragraphs and list items.
- Content rule: Explain specific technical constraints, bottlenecks, and mechanisms. Omit speculative adjectives and conversational padding.

### Performance gain lists

Unordered lists documenting specific architectural changes and speedups:
- Class: `ul.gain`.
- Items: Spaced at `margin: 0.2rem 0` with bold leading phrases naming the mechanism, followed immediately by the measured speedup or memory delta.

### Collapsible details

Native disclosure element for raw logs and secondary runs:
- Container: `details { margin: 0.4rem 0 }`.
- Summary: `summary { cursor: pointer; font-weight: 500 }`.

## Do's and Don'ts

- **Do** document performance changes with concrete numbers, measured deltas, and memory peaks.
- **Do** lead optimization bullets with the concrete mechanism followed by the measured result.
- **Do** maintain strict 80-character width limits on prose to prevent rambling explanations.
- **Do** use native system sans-serif typography (`-apple-system, sans-serif`) for crisp, platform-native rendering.
- **Do** set table numerals to tabular numbers (`tabular-nums`) and right-align all metric values.
- **Do** wrap figures in a responsive CSS grid with `minmax(340px, 1fr)` for small-multiples telemetry.
- **Do** use 0px unrounded corners across all boxes, tables, and sparkline charts.
- **Do** use light grey `#eeeeee` solely on table header backgrounds to ground data columns.
- **Don't** write subjective performance claims ('runs quickly', 'significantly faster') without including the exact benchmark delta.
- **Don't** add conversational padding, greeting banners, or speculative advice.
- **Don't** use em dashes in comparisons; use clear comparative phrasing or tables.
- **Don't** add drop shadows, rounded corners, or glowing line graphs.
- **Don't** use decorative badge pills or colored status indicators.
- **Don't** import third-party web font packages; rely on system font stacks.
- **Don't** center-align tabular numbers or mix left and right alignment within a single numeric column.
- **Don't** use smoothed curves or filled areas under sparklines; use simple 1px polyline strokes.
