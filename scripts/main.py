"""Forge Neo Theme — a modular visual theme for Forge/WebUI.

Ported from anxety-theme (MIT license, https://github.com/anxety-solo/anxety-theme):
same "flavor + toggleable modules assembled into style.css" architecture, ACCENTS list,
and most module CSS carried over close to verbatim. See LICENSE for the original copyright
notice.

Deliberately excludes the original Extra-Network-Pane behavior... actually it INCLUDES an
adapted Extra-Network-Pane module, but every one of its rules is scoped under
`body:not(.civitai-neo-card-theme)` so it goes inert whenever sd-civitai-browser-neo's own
card theme is active — see modules/Extra-Network-Pane.css for the full rationale. This
extension does not otherwise touch `.card` / `.button-row` / `.actions` anywhere.
"""

import gradio as gr
import shutil
import re
from pathlib import Path

from modules.shared import OptionInfo, opts, cmd_opts
from modules.script_callbacks import on_ui_settings
from modules.scripts import basedir


# --- CONSTANTS ---
SECTION = ('fnt', 'Forge Neo Theme')
ACCENTS = (
    'blue',
    'green',
    'peach',
    'pink',
    'red',
    'rose',
    'yellow'
)
SCRIPT_PATH = Path(basedir())
MODULES_DIR = SCRIPT_PATH / 'modules'
STYLE_CSS = SCRIPT_PATH / 'style.css'


# --- LOGGER ---
class Logger:
    PREFIX = '[Forge-Neo-Theme]'

    @staticmethod
    def error(message: str):
        print(f"\033[31m{Logger.PREFIX}\033[0m - {message}")

    @staticmethod
    def warning(message: str):
        print(f"\033[33m{Logger.PREFIX}\033[0m - {message}")

    @staticmethod
    def info(message: str):
        print(f"\033[34m{Logger.PREFIX}\033[0m - {message}")

logger = Logger()


# --- UTILS ---
def validate_hex_color(color: str) -> str:
    """Validate and normalize hex color format"""
    if not color:
        return ''

    color = color.strip().lstrip('#')

    if len(color) == 3:
        color = ''.join([c + c for c in color])
    elif len(color) != 6:
        return ''

    if not all(c in '0123456789ABCDEFabcdef' for c in color):
        return ''

    return f"#{color.upper()}"

def get_module_names():
    """Return a list of available module names (CSS files) in the modules directory"""
    if MODULES_DIR.exists():
        return [f.stem for f in MODULES_DIR.glob('*.css') if f.is_file()]
    return []

def is_sd_ux():
    """Check if SD-UX is installed by scanning extensions-builtin directory"""
    try:
        extensions_dir = SCRIPT_PATH.parent
        ui_root = extensions_dir.parent

        extensions_builtin = ui_root / 'extensions-builtin'
        sd_ux_path = extensions_builtin / 'sd-webui-ux'

        return sd_ux_path.exists() and sd_ux_path.is_dir()
    except Exception as e:
        logger.warning(f"Error checking for SD-UX: {e}")
        return False

def select_base_css():
    """Select and return the appropriate base CSS file path"""
    if is_sd_ux():
        return SCRIPT_PATH / 'flavors/forge-neo-ux.css'
    elif gr.__version__ >= '4.0.0':
        return SCRIPT_PATH / 'flavors/forge-neo-gr4.css'
    else:
        return SCRIPT_PATH / 'flavors/forge-neo-legacy.css'

def update_accent_in_css():
    """Update the accent color variable in the main CSS file"""
    current_accent = getattr(opts, 'fnt_accent_color', 'blue')
    custom_hex = getattr(opts, 'fnt_custom_hex_color', '')

    if custom_hex:
        validated_hex = validate_hex_color(custom_hex)
        if validated_hex:
            accent_value = validated_hex
            logger.info(f"Using custom hex color: {validated_hex}")
        else:
            accent_value = f"var(--fnt-{current_accent})"
            logger.warning(f"Invalid hex color '{custom_hex}'. Using predefined accent '{current_accent}'.")
    else:
        accent_value = f"var(--fnt-{current_accent})"

    with open(STYLE_CSS, 'r+', encoding='utf-8') as file:
        pattern = re.compile(r'--fnt-accent:\s*(.*)')
        text = re.sub(
            pattern,
            f"--fnt-accent: {accent_value};",
            file.read(),
            count=1,
        )
        file.seek(0)
        file.write(text)
        file.truncate()

def append_active_modules():
    """Append the CSS of all active modules to the main style file"""
    active_modules = getattr(opts, 'fnt_active_modules', [])
    with open(STYLE_CSS, 'a', encoding='utf-8') as main_css:
        for module_name in active_modules:
            module_path = MODULES_DIR / f"{module_name}.css"
            if module_path.is_file():
                main_css.write(f"\n\n/* Module: {module_name} */\n")
                with open(module_path, 'r', encoding='utf-8') as mod_file:
                    main_css.write(mod_file.read())

def handle_cmd_accent():
    """Handle accent color selection from command line arguments"""
    if hasattr(cmd_opts, 'forge_neo_theme_accent') and cmd_opts.forge_neo_theme_accent:
        arg_color = cmd_opts.forge_neo_theme_accent.lower()
        if arg_color in ACCENTS:
            opts.fnt_accent_color = arg_color
            logger.info(f"Using command line accent color: {arg_color}")
        else:
            opts.fnt_accent_color = 'blue'
            logger.warning(f"Invalid command line color '{cmd_opts.forge_neo_theme_accent}'. Defaulting to 'blue'.")
            logger.info(f"Available accent colors: {', '.join(ACCENTS)}")


def apply_theme():
    if not getattr(opts, 'fnt_enable_theme', True):
        with open(STYLE_CSS, 'w', encoding='utf-8') as file:
            file.write('/* Forge Neo Theme */\n')
        logger.info('Theme disabled')
        return

    handle_cmd_accent()
    shutil.copy(select_base_css(), STYLE_CSS)
    update_accent_in_css()
    append_active_modules()


def on_settings():
    """Create settings UI elements"""
    opts.add_option(
        'fnt_enable_theme',
        OptionInfo(
            default=True,
            label='Enable Theme',
            component=gr.Checkbox,
            component_args={},
            onchange=apply_theme,
            section=SECTION,
            category_id='ui',
        ).info('When disabled, the theme will be turned off')
    )

    opts.add_option(
        'fnt_accent_color',
        OptionInfo(
            default='blue',
            label='Accent Color',
            component=gr.Radio,
            component_args={'choices': ACCENTS},
            onchange=update_accent_in_css,
            section=SECTION,
            category_id='ui',
        ).info('Note: Not available when custom hex color is set')
    )

    opts.add_option(
        'fnt_custom_hex_color',
        OptionInfo(
            default='',
            label='Custom Hex Color',
            component=gr.Textbox,
            component_args={'placeholder': 'Enter hex color (e.g. #ff00ff, #123abc, #FAA)'},
            onchange=update_accent_in_css,
            section=SECTION,
            category_id='ui',
        ).info('UI restart recommended')
    )

    module_names = get_module_names()
    opts.add_option(
        'fnt_active_modules',
        OptionInfo(
            default=module_names,
            label='Enabled Modules',
            component=gr.CheckboxGroup,
            component_args={'choices': module_names},
            onchange=apply_theme,
            section=SECTION,
            category_id='ui',
        ).info(
            'Select which modules should be enabled in the interface. '
            'Extra-Network-Pane restyles the txt2img/img2img checkpoint & LoRA cards, but '
            'automatically stays off whenever sd-civitai-browser-neo\'s own "CivitAI-style '
            'card theme" is turned on, so it is safe to leave enabled either way.'
        )
    )

    apply_theme()

on_ui_settings(on_settings)
