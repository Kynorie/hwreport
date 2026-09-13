from constants import ORANGE, RESET, FOOTER_TEXT, GITHUB_REPO_URL


def print_line(label, value):
    print(f"{label} | {value}")


def print_footer():
    # prints the orange footer line, clickable in terminals that support it
    # this uses an osc 8 escape sequence for the hyperlink
    # terminals that do not support it will just show the plain text instead
    link_start = f"\033]8;;{GITHUB_REPO_URL}\033\\"
    link_end = "\033]8;;\033\\"

    print()
    print(f"{ORANGE}{link_start}{FOOTER_TEXT}{link_end}{RESET}")
