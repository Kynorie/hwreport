import re
import subprocess


def _get_screen_inches(width_mm, height_mm):
    if width_mm <= 0 or height_mm <= 0:
        return None

    diagonal_mm = (width_mm ** 2 + height_mm ** 2) ** 0.5
    inches = diagonal_mm / 25.4
    return round(inches, 1)


def get_displays():
    try:
        result = subprocess.run(
            ["xrandr", "--verbose"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ["N/A"]

    displays = []
    current_name = None
    width_mm = 0
    height_mm = 0

    connected_pattern = re.compile(
        r"^(\S+) connected.*?(\d+)mm x (\d+)mm"
    )
    mode_pattern = re.compile(
        r"^\s+(\d+)x(\d+)\s+([\d.]+)\*"
    )

    for line in result.stdout.splitlines():
        connected_match = connected_pattern.match(line)
        if connected_match:
            if current_name:
                displays.append(
                    _format_display(current_name, width_mm, height_mm, None, None, None)
                )

            current_name = connected_match.group(1)
            width_mm = int(connected_match.group(2))
            height_mm = int(connected_match.group(3))
            continue

        mode_match = mode_pattern.match(line)
        if mode_match and current_name:
            res_width = mode_match.group(1)
            res_height = mode_match.group(2)
            refresh = mode_match.group(3)

            displays.append(
                _format_display(current_name, width_mm, height_mm, res_width, res_height, refresh)
            )
            current_name = None

    if current_name:
        displays.append(
            _format_display(current_name, width_mm, height_mm, None, None, None)
        )

    if not displays:
        return ["N/A"]

    return displays


def _format_display(name, width_mm, height_mm, res_width, res_height, refresh):
    inches = _get_screen_inches(width_mm, height_mm)
    inches_str = f'{inches}"' if inches else "N/A"

    if res_width and res_height:
        resolution_str = f"{res_width}x{res_height}"
    else:
        resolution_str = "N/A"

    if refresh:
        refresh_str = f"{round(float(refresh))}Hz"
    else:
        refresh_str = "N/A"

    return f"{name} - {resolution_str} - {inches_str} - {refresh_str}"
