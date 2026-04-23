# Knowledge Field Layout Guardrails

## Question

How do we eliminate overlap-style regressions in the knowledge graph UI so that the atlas, sidebar, and supporting cards never compete for the same space again?

## Findings

- The original failure mode came from treating support cards as visual overlays inside the same stage plane as the graph canvas.
- The page shell also relied on a hand-synchronized pair of values: a fixed sidebar width and a separate content padding offset.
- The stage responded to `window.resize`, but not to container-only reflow caused by wrapping text, zoom, or sidebar state changes.

## Decision

We will prevent overlap structurally instead of cosmetically.

1. Move both graph pages onto a two-column application shell with a sticky rail instead of a fixed rail plus manual content padding.
2. Keep `Knowledge Field` in normal document flow:
   `stage-chrome -> stage-canvas-shell -> stage-briefs`
3. Switch stage internals to container-based responsive behavior, so narrow stage widths collapse even when the overall viewport is still “desktop”.
4. Watch the canvas container with `ResizeObserver` and rebuild the graph layout when the container changes size.
5. Keep screenshot-based regression tests for the exact failure class:
   sidebar/content overlap, chrome/canvas overlap, canvas/insight overlap, and card/card overlap.

## Why This Is Safer

- The graph canvas no longer owns the same physical layer as explanatory cards.
- Sidebar width is expressed once by the layout grid, instead of being duplicated in multiple CSS rules.
- Breakpoints follow the actual stage width, not a guessed viewport width.
- Reflow from text wrapping or zoom triggers a layout recalculation before the canvas drifts out of sync.

## Next Actions

- Keep graph and reader shells visually aligned by reusing the same spacing tokens and sticky-rail behavior.
- Expand screenshot coverage to mobile once a stable browser runner is available in CI.
