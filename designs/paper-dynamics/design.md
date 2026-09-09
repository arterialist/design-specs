---
name: Paper dynamics
description: A paper-backed analytical interface with fine rules, restrained plots, and readable measurements.
colors:
  primary: "#24251f"
  on-primary: "#f7f5ef"
  secondary: "#245d79"
  tertiary: "#984526"
  background: "#f7f5ef"
  on-background: "#24251f"
  surface: "#f7f5ef"
  surface-container: "#eeede4"
  on-surface: "#24251f"
  on-surface-variant: "#5e6056"
  outline: "#c4c4b6"
  diagram-outline: "#bcbeb0"
  success: "#356342"
  selection-text: "#ffffff"
typography:
  headline:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.02em
  masthead:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.5
  intro:
    fontFamily: Georgia, serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  control:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  readout:
    fontFamily: Menlo, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
  hint:
    fontFamily: '"Avenir Next", Verdana, sans-serif'
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
rounded:
  none: 0px
  control: 2px
spacing:
  unit: 8px
  control-gap: 12px
  section-gap: 24px
  reading-column-gap: 32px
  margin-desktop: 40px
  margin-tablet: 24px
  margin-mobile: 16px
  main-max-width: 1600px
  masthead-max-width: 1536px
  canvas-height: 640px
  canvas-height-mobile: 520px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.control}"
    width: 112px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
  button-secondary:
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: 9px 14px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-container}"
  select:
    rounded: "{rounded.control}"
    padding: 7px
    height: 44px
  seek-slider:
    height: 36px
---

# Paper dynamics

## Overview

![Paper dynamics preview](preview.png)

A paper-backed analytical interface designed for studying changing signals, state-space trajectories, and complex dynamic states. The primary plot takes up most of the page. Compact controls sit directly above it, while structured interpretations and exact numerical readouts sit below.

This design enforces strict analytical discipline. Interfaces built with this system must prioritize raw signal data, physical units, and synchronized telemetry over explanatory prose. Eliminate greeting banners, marketing fluff, decorative cards, and AI narrative summaries. Every visual element must function as an instrument.

Use this design when users need to inspect visual data closely, compare multiple states, and read exact measurements. The surrounding interface remains quiet and unobtrusive: no raised cards, decorative icons, glowing neon traces, or decorative entrance animations.

## Colors

The palette uses warm paper neutrals, strong graphite contrast, and restrained channel accents.

### Primary
- **Graphite (`#24251f`):** Core text, primary button fill, selected sample markers, and primary structural dividing lines.
- **Warm Paper (`#f7f5ef`):** Foundational page background, transparent canvas backdrop, and primary button text.

### Secondary
- **Ink Blue (`#245d79`):** First data channel, link hover state, keyboard focus outlines, and native input accents.

### Tertiary
- **Burnt Rust (`#984526`):** Second data channel and error or warning highlights.

### Neutral & surface
- **Paper Wash (`#eeede4`):** Secondary button hover background and selected event highlights.
- **Hairline Grey (`#c4c4b6`):** Section divider rules and control borders.
- **Diagram Grey (`#bcbeb0`):** 3D canvas plane wireframes and background reference trajectories.
- **Muted Olive Grey (`#5e6056`):** Secondary labels, axis descriptions, and chart annotations.
- **White (`#ffffff`):** Selected text against the accent selection background.
- **Muted Green (`#356342`):** Semantic success state indicator.

| Token | Name | Value | Role |
| --- | --- | --- | --- |
| `background` | Warm paper | `#f7f5ef` | Page, transparent canvas backdrop, and primary button text |
| `primary` | Graphite | `#24251f` | Text, primary button, selected samples, and strong rules |
| `on-surface-variant` | Muted olive grey | `#5e6056` | Supporting labels and plot annotations |
| `surface-container` | Paper wash | `#eeede4` | Secondary button hover and selected event background |
| `outline` | Hairline grey | `#c4c4b6` | Section dividers and control borders |
| `diagram-outline` | Diagram grey | `#bcbeb0` | Canvas plane outlines and background trajectories |
| `secondary` | Ink blue | `#245d79` | First data channel, link hover, focus ring, and native input accent |
| `tertiary` | Burnt rust | `#984526` | Second data channel and error highlights |
| `success` | Muted green | `#356342` | Semantic success token |
| `selection-text` | White | `#ffffff` | Selected text against accent selection background |

The two rule colours (`#c4c4b6` for general dividers and `#bcbeb0` for canvas diagrams) are distinct and intentional. Do not convert the blue and rust data channels into generic success and failure indicators unless the data semantically represents that meaning.

### Paper texture

Use the accompanying [paper.webp](assets/paper.webp) asset. Repeat it across a fixed, full-viewport layer at a display size of 768 × 512 CSS pixels and 55% opacity. The layer ignores pointer events (`pointer-events: none`) and sits behind all content. The visualization canvas is transparent so the paper continues beneath diagrams.

The texture contains no writing, lines, or geometric objects. Do not add notebook grids, torn paper edges, or drop shadows. Without the asset, maintain the warm paper color (`#f7f5ef`) as the base fallback.

## Typography

Local font stacks are used without remote web font downloads:
- **Sans stack:** `"Avenir Next", Verdana, sans-serif`
- **Serif stack:** `Georgia, serif`
- **Monospace stack:** `Menlo, monospace`

| Role | Family | Size / Leading | Weight & Treatment |
| --- | --- | --- | --- |
| Masthead | Sans | 18px / 27px | 700 title, 400 muted descriptor |
| Headline | Sans | 24px / 31.2px | 600, tracking `-0.02em` |
| Opening explanation | Serif | 16px / 24px | 400, emphasis in italics |
| Controls | Sans | 14px / 21px | 400 |
| Control labels & legend | Sans | 13px / 19.5px | 400 |
| Reading section heading | Sans | 16px / 24px | Bold (700) |
| Reading section prose | Sans | 14px / 21px | 400 |
| Closing section heading | Sans | 18px / 27px | Bold (700) |
| Closing section prose | Sans | 15px / 22.5px | 400 |
| Interaction hints | Sans | 12px / 18px | Muted (`#5e6056`) |
| Exact-value readout | Monospace | 12px / 19.2px | 400, one measurement per line |
| Canvas layer names | Sans | 14px | 600, right-aligned beside each plane |
| Canvas variable descriptions | Sans | 11px | Muted (`#5e6056`) |
| Canvas coordinate ranges | Monospace | 10px | Muted (`#5e6056`) |

Use sentence case throughout. Monospace is reserved for numeric readouts, coordinates, and status counters, rather than general technical prose. Exact-value readouts format to five significant digits. Counters use tabular numerals. Avoid conversational filler or em dashes in labels and notes.

## Layout

The layout uses a structured vertical flow:

1. **Masthead:** Compact bar with title on the left and utility link on the right.
2. **Heading & narrative:** Primary title row with secondary action, followed by a serif introductory explanation.
3. **Control bar:** Wrapping row containing selectors, replay controls, and status indicators.
4. **Main diagram:** Full-width 3D canvas positioned between thin horizontal rules.
5. **Telemetry & legend:** Interaction hints paired with a two-channel legend.
6. **Seek slider:** Full-width range timeline with tick counter and event shortcuts.
7. **Reading columns:** Two unboxed columns separating qualitative interpretation on the left from exact numeric readouts on the right.
8. **Closing section:** Concluding analysis separated by a 1px dashed rule.

The main content container is centred with a `1600px` maximum width. The masthead uses a `1536px` maximum width. Both apply `40px` horizontal page padding on desktop viewports.

The heading row applies a 24px gap, 24px top margin, and 12px bottom margin. The control row uses 12px gaps and 16px margin above the plot. The main plot canvas is 640px tall without an enclosing card or background fill. The two reading columns split evenly with a 32px gap, 16px top margin, and 28px bottom margin. The closing section begins with a 1px dashed graphite rule, 20px top padding, and 32px bottom margin.

### Responsive breakpoints

| Viewport Width | Adjustments |
| --- | --- |
| Above 1000px | 40px horizontal page padding |
| 701px to 1000px | 24px horizontal page padding |
| 700px and below | 16px horizontal padding; heading row stacks; reading columns stack into single column; control gap becomes 8px; canvas height scales to 520px; masthead shrinks to 16px with descriptor wrapping; main heading becomes 20px / 26px |

When canvas width falls below 600px, layer names scale to 11px and variable descriptions to 9px. Event shortcuts and legend items wrap cleanly without clipping.

## Elevation & depth

Surfaces are strictly flat at rest. Depth is established through:
- Fine wireframe outlines (0.8px `#bcbeb0` and 1px `#c4c4b6`).
- Perspective tilt and 3D plane projection.
- Subtle background washes (`#eeede4`) for state changes over the warm paper (`#f7f5ef`).

No box shadows, ambient blurs, elevation overlays, or card surfaces are used. Tactile interaction depth is achieved solely via a 1px downward translation on active press (`transform: translateY(1px)`).

## Shapes

The interface uses architectural, near-square geometry:
- **Interactive controls:** Buttons, inputs, and select elements use a minimal 2px corner radius (`rounded: 2px`).
- **Structural containers:** Content wrappers, sections, and canvas frames use sharp 0px unrounded corners.
- **Dividers & strokes:** 1px solid dividers (`#c4c4b6`), 0.8px diagram plane wireframes (`#bcbeb0`), and 1px dashed graphite lines (`#24251f` with 3px/4px or 3px/6px dash patterns).

## Components

### Buttons

- **Primary replay button:** Graphite fill (`#24251f`), warm paper text (`#f7f5ef`), 2px radius, min-height 44px, min-width 112px. Hover changes background to ink blue (`#245d79`). Toggles between Play and Pause states while maintaining role.
- **Secondary button:** Transparent fill, 1px border (`#c4c4b6`), 2px radius, 9px vertical / 14px horizontal padding, min-height 44px. Hover adds paper wash (`#eeede4`) and shifts border to graphite (`#24251f`). Active press translates 1px down without transition easing.
- **Disabled state:** 45% opacity, no active translation. Use a wait cursor only when waiting is the explicit cause of the disabled state.
- **Event shortcuts:** Underlined text appearance with transparent borders, 13px font, 6px vertical / 10px horizontal padding, min-height 36px desktop / 44px mobile. Selected state removes underline, adding paper wash background (`#eeede4`) and a hairline border.

### Selectors and timeline

- **Select dropdowns:** Native select menus with transparent background, 1px border (`#c4c4b6`), 2px radius, 7px padding, and 44px min-height. Labels remain visible beside controls.
- **Seek slider:** Full-width native range input with ink blue accent (`#245d79`) and min-height 36px. Paired with a left-aligned label and a right-aligned monospace current or total tick counter. Native track and thumb controls are maintained.

### Links and focus

- **Text links:** Inherit parent text color with a 4px underline offset (`text-underline-offset: 4px`). Hover turns ink blue (`#245d79`).
- **Keyboard focus:** 2px solid ink blue ring with a 3px offset (`outline: 2px solid #245d79; outline-offset: 3px`).
- **Text selection:** Ink blue background (`#245d79`) with pure white text (`#ffffff`).

### Reading blocks

- **Prose blocks:** Unboxed document typography without card borders or background cards. Introductory serif passage has a 92ch line-length cap. General prose inherits a 76ch cap. Prose must state physical findings and observed correlations directly, avoiding conversational preambles.
- **Readout blocks:** Exact numerical measurements displayed in aligned monospace blocks (`Menlo, monospace`), visible directly on the page without requiring hover tooltips. Always pair measurements with standard physical units.

### 3D diagram stack

- **Plane geometry:** Four open wireframe rectangular planes (580 × 220 model units) vertically stacked with 125 model units separation. Rendered with 0.8px stroke (`#bcbeb0`) at a default view of yaw -0.32 rad, tilt 0.38 rad, zoom 1.
- **Time ribbons:** 1.2px stepped traces in ink blue (`#245d79`) and burnt rust (`#984526`) on separate tracks, with a 3px graphite point on each trace indicating current tick, aligned by a 1px dashed cross-plane cursor (3px / 4px dash).
- **State-space trajectories:** 0.8px grey trace showing complete trajectory, 1.8px ink blue trace showing recent segment, and a 4px graphite point marking the selected sample.
- **Interaction & camera:** Dragging canvas rotates camera yaw and tilt. Pinch or wheel zooms within 0.55 to 1.5x. Dedicated Rotate view (+0.3 rad yaw) and Reset view (restores default camera) buttons provide accessible keyboard and click controls. Playback starts paused at a replay cadence of 12 ticks per second.

## Do's and Don'ts

- **Do** format exact measurements to five significant digits with explicit units (`V`, `A`, `ms`, `rad`).
- **Do** state concrete physical mechanisms and numerical bounds instead of subjective narrative impressions.
- **Do** keep readings, measurement ranges, and channel legends continuously visible alongside plots without relying on hover tooltips.
- **Do** use warm paper (`#f7f5ef`) and the subtle repeated texture as the backdrop for all analytical visualizations.
- **Do** maintain sharp (0px) structural containers and subtle 2px control corners for an instrument-grade feel.
- **Do** preserve the distinction between divider outline (`#c4c4b6`) and diagram outline (`#bcbeb0`).
- **Do** respect user motion preferences by removing button press translation under `prefers-reduced-motion`.
- **Don't** generate greeting banners, empty summary cards, or AI conversational prose.
- **Don't** use em dashes in notes or labels; use periods, commas, or structured data rows.
- **Don't** use drop shadows, elevation blurs, glowing neon traces, or skeuomorphic bevels.
- **Don't** enclose sections in raised cards or floating white containers.
- **Don't** use decorative entrance animations, smoothed camera easing, or idle animations.
- **Don't** treat the two data channels (`ink blue` and `burnt rust`) as generic success or failure indicators.
- **Don't** add decorative grids, torn paper edges, or faux distress to the paper texture.
- **Don't** shrink measurement labels below legible thresholds just to force visualizations above the fold.
