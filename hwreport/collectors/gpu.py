import subprocess


def get_gpu():
    # uses lspci to find the graphics card
    # this works for nvidia, amd, and intel without needing extra tools installed
    try:
        result = subprocess.run(
            ["lspci"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "N/A"

    for line in result.stdout.splitlines():
        lower_line = line.lower()
        if "vga" in lower_line or "3d controller" in lower_line:
            # the line looks like "01:00.0 VGA compatible controller: NVIDIA Corporation ..."
            # we just want the part after the last colon
            if ":" in line:
                parts = line.split(":")
                return parts[-1].strip()

    return "N/A"
