# CEF embed (deferred)

Use [Energy](https://github.com/energye/energy) only if you need a **full Chromium Embedded Framework** panel inside a custom Go binary — e.g. live preview while editing research notes.

**Not part of Tier 1.** The CLI uses **chromedp** (headless). Wails was removed from the plan; there is no desktop shell to embed CEF into unless you build one separately.

Implement here when/if that need appears: `internal/screen/cef/screen.go` calling Energy APIs.
