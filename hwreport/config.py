import os
import subprocess

from constants import CONFIG_DIR, CONFIG_PATH, COMPONENT_ORDER, DEFAULT_CONFIG


def ensure_config_exists():
    # make the config folder and file if they are not there yet
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(CONFIG_PATH):
        write_config(DEFAULT_CONFIG)


def load_config():
    # falls back to defaults for any key that is missing or broken
    ensure_config_exists()

    config = dict(DEFAULT_CONFIG)

    with open(CONFIG_PATH, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip().upper()
            value = value.strip()

            if key in COMPONENT_ORDER and value in ("0", "1"):
                config[key] = value

    return config


def write_config(config):
    lines = []
    for key in COMPONENT_ORDER:
        value = config.get(key, "1")
        lines.append(f"{key}={value}")

    with open(CONFIG_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")


def get_editor(editor_override=None):
    if editor_override:
        return editor_override

    if os.environ.get("EDITOR"):
        return os.environ["EDITOR"]

    if os.environ.get("VISUAL"):
        return os.environ["VISUAL"]

    return "nano"


def open_config_in_editor(editor_override=None):
    # opens the config file in a terminal text editor
    ensure_config_exists()
    editor = get_editor(editor_override)

    try:
        subprocess.run([editor, CONFIG_PATH])
    except FileNotFoundError:
        print(f"Could not find the editor '{editor}'. Is it installed?")
