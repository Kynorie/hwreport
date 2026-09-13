import platform


def get_os():
    # reads the pretty name out of /etc/os-release
    # this is the standard way to get a distro name on linux
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    # the value is wrapped in quotes, strip those off
                    return line.split("=", 1)[1].strip().strip('"')
    except FileNotFoundError:
        pass

    return "N/A"


def get_kernel():
    # platform.release() gives the kernel version, works without any external tools
    kernel = platform.release()
    return kernel if kernel else "N/A"
