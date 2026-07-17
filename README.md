# Forge Neo Theme

A modular visual theme for Forge/WebUI — flat cards, accent colors, restyled dropdowns,
scrollbars, tables, tag-autocomplete and more, assembled from toggleable CSS modules.

Structurally a fork of [anxety-theme](https://github.com/anxety-solo/anxety-theme) (MIT
licensed): same "base flavor + opt-in modules" architecture, most module CSS carried over
close to verbatim. See [LICENSE](LICENSE) for the full attribution.

## Install

Add this repo's URL in WebUI's **Extensions → Install from URL**, or clone it into your
`extensions/` folder. Restart WebUI. Configure under **Settings → Forge Neo Theme**.

## Compatibility with sd-civitai-browser-neo

The `Extra-Network-Pane` module restyles the native txt2img/img2img checkpoint & LoRA cards
(rounded corners, hover-reveal action buttons, name pill). If you also use
[sd-civitai-browser-neo](https://github.com/eduardoabreu81/sd-civitai-browser-neo) with its
own opt-in **"CivitAI-style card theme"** turned on, that extension adds a
`civitai-neo-card-theme` class to `<body>` — every rule in this module is scoped under
`body:not(.civitai-neo-card-theme)`, so it automatically goes inert whenever that theme is
active instead of fighting over the same cards. No configuration needed on either side; you
can leave both extensions' card styling enabled and whichever one is "on" wins cleanly.

This extension never touches `.card` / `.button-row` / `.actions` outside that one module,
so disabling `Extra-Network-Pane` in **Settings → Forge Neo Theme → Enabled Modules** removes
all card-related styling from this theme entirely if you'd rather sd-civitai-browser-neo (or
nothing) own that area unconditionally.

## Modules

| Module | What it styles |
|---|---|
| `Extra-Network-Pane` | Checkpoint/LoRA cards (see compatibility note above) |
| `Fluent Dropdown` | Gradio dropdown menus |
| `Fluent ToastError` | Error toast notifications |
| `Image Viewer` | Lightbox/image modal |
| `ScrollBar` | Custom scrollbar styling |
| `Table` | Generic HTML tables |
| `TagComplete` | [Tag Autocomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) dropdown |
| `sd-hub` | [SD-Hub](https://github.com/lllyasviel/sd-hub) tab styling |

Toggle modules individually in Settings — changes apply without a restart.

## Accent color

Pick a preset (`default`, `blue`, `green`, `peach`, `pink`, `red`, `yellow`) or enter a
custom hex color in Settings. Can also be set at launch with `--forge-neo-theme-accent
<color>`.
