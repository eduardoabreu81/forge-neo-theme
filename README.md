# 🎨 Forge Neo Theme

<div align="center">

[![Forge Neo](https://img.shields.io/badge/Forge-Neo-blue)](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Extension for [Stable Diffusion WebUI Forge - Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)**

</div>

A modular visual theme for Forge Neo — flat cards, accent colors, and a set of toggleable
modules restyling dropdowns, scrollbars, tables, tag-autocomplete, and more. Built to sit
alongside [sd-civitai-browser-neo](https://github.com/eduardoabreu81/sd-civitai-browser-neo)
without fighting it over the Extra Networks cards.

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Modules](#-modules)
- [Accent Color](#-accent-color)
- [Compatibility with sd-civitai-browser-neo](#-compatibility-with-sd-civitai-browser-neo)
- [Credits](#-credits)

---

## 🎯 Features

- **Flat, modern card design** for the native Extra Networks grid (checkpoints, LoRAs) — rounded corners, hover-reveal action row, blurred name pill
- **7 accent colors** (default, blue, green, peach, pink, red, yellow) plus custom hex, applied across buttons, links, tabs, sliders, and every module
- **Toggleable modules** — turn each restyled component on/off independently in Settings, no restart required
- **3 base flavors** — auto-selected for Gradio 4, SD-UX, or legacy Gradio, so the right variables load for your setup
- **Zero-conflict card styling** — automatically steps aside when sd-civitai-browser-neo's own card theme is active (see [Compatibility](#-compatibility-with-sd-civitai-browser-neo))

---

## 📦 Installation

1. Open Forge Neo WebUI
2. Go to **Extensions** → **Install from URL**
3. Paste: `https://github.com/eduardoabreu81/forge-neo-theme`
4. Click **Install** and reload the WebUI
5. Configure under **Settings → Forge Neo Theme**

---

## 🧩 Modules

Each module is a standalone CSS file, toggled independently under **Settings → Forge Neo
Theme → Enabled Modules**. All are enabled by default.

| Module | What it styles |
|---|---|
| Extra-Network-Pane | Checkpoint/LoRA cards — rounded corners, hover-reveal buttons, name pill *(see compatibility note below)* |
| Fluent Dropdown | Gradio dropdown menus |
| Fluent ToastError | Error toast notifications |
| Image Viewer | Lightbox / image modal |
| ScrollBar | Custom scrollbar styling |
| Table | Generic HTML tables |
| TagComplete | [Tag Autocomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) dropdown |
| sd-hub | [SD-Hub](https://github.com/lllyasviel/sd-hub) tab styling |

---

## 🎨 Accent Color

Pick a preset (`default`, `blue`, `green`, `peach`, `pink`, `red`, `yellow`) or enter a
custom hex color in Settings — applies instantly across every module. Can also be set at
launch with `--forge-neo-theme-accent <color>`.

---

## 🔗 Compatibility with sd-civitai-browser-neo

The `Extra-Network-Pane` module restyles the same native txt2img/img2img checkpoint & LoRA
cards that [sd-civitai-browser-neo](https://github.com/eduardoabreu81/sd-civitai-browser-neo)
can optionally restyle with its own **"CivitAI-style card theme"** setting.

When that setting is on, sd-civitai-browser-neo adds a `civitai-neo-card-theme` class to
`<body>`. Every rule in `Extra-Network-Pane` is scoped under
`body:not(.civitai-neo-card-theme)`, so this module automatically goes inert the moment that
theme is active — no manual toggling needed on either side, and no risk of the two layouts
overlapping. If you don't use sd-civitai-browser-neo at all, the class is never present and
this module behaves normally.

If you'd rather sd-civitai-browser-neo (or nothing) own card styling unconditionally, disable
`Extra-Network-Pane` in **Settings → Forge Neo Theme → Enabled Modules** — every other module
here never touches `.card` / `.button-row` / `.actions` at all.

---

## 📄 Credits

- **[anxety-theme](https://github.com/anxety-solo/anxety-theme)** by anxety-solo — this
  extension is a structural fork: the flavor+modules architecture, the settings assembly
  script, and most module CSS are ported directly from their work (MIT licensed). Full credit
  for the original design goes to them.
- **[Forge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)** by Haoming02

---

## 📜 License

MIT — see [LICENSE](LICENSE)

---

<div align="center">

Made with ❤️ for the Stable Diffusion community

**[Report Bug](https://github.com/eduardoabreu81/forge-neo-theme/issues)** • **[Request Feature](https://github.com/eduardoabreu81/forge-neo-theme/issues)** • **[☕ Ko-fi](https://ko-fi.com/eduardoabreu81)**

</div>
