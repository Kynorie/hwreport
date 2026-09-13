def get_cpu():
    # reads the cpu model name out of /proc/cpuinfo
    # this file exists on basically every linux system
    try:
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if line.lower().startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except FileNotFoundError:
        pass

    return "N/A"
