# Excalidraw Ato Capsule

- Upstream: `excalidraw/excalidraw`
- Pinned upstream commit: `7c0b3295760d3492a980f2f6416a36c9ef592103`
- License: MIT (`LICENSE`)
- Surface: Web
- Authentication: none
- External services: disabled

Every fresh browser opens a bundled `Ato product flow` scene containing Idea,
Design, and Ship nodes. The seed is materialized by Excalidraw's own
`convertToExcalidrawElements` API and does not depend on localStorage or a
remote scene backend. All normal drawing, selection, movement, and undo/redo
tools remain available.

The Capsule serves a committed production build with Sentry and tracking
disabled and a same-origin-only CSP. It performs no runtime dependency
download.
