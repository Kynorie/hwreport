import os

GITHUB_USER = "kynorie"
GITHUB_REPO = "hwreport"
GITHUB_API_RELEASES = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases"
GITHUB_REPO_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}"

RELEASE_ASSET_NAME = "hwreport.zip"

# where the config file lives, one per user
CONFIG_DIR = os.path.expanduser("~/.config/hwreport")
CONFIG_PATH = os.path.join(CONFIG_DIR, "hwreport.conf")

# where hwreport gets installed on the system
INSTALL_BIN_PATH = "/usr/local/bin/hwreport"
INSTALL_LIB_PATH = "/usr/local/lib/hwreport"

# the order components print in when hwreport runs
COMPONENT_ORDER = [
    "CPU",
    "GPU",
    "RAM",
    "DISPLAY",
    "BATTERY",
    "OS",
    "KERNEL",
]

DEFAULT_CONFIG = {key: "1" for key in COMPONENT_ORDER}

# ansi color codes for the footer text
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

FOOTER_TEXT = "If something here isn't correct, or isn't displaying. Let me know!"
