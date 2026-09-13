def get_ram():
    # reads total memory out of /proc/meminfo, which is in kb
    # then converts it to gb for a cleaner display
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal"):
                    parts = line.split()
                    kb = int(parts[1])
                    gb = kb / 1024 / 1024
                    return f"{gb:.1f} GB"
    except (FileNotFoundError, ValueError, IndexError):
        pass

    return "N/A"
