import os


def get_battery():
    # looks for a battery under /sys/class/power_supply
    # desktops usually have nothing here, laptops have something like BAT0 or BAT1
    power_supply_path = "/sys/class/power_supply"

    if not os.path.isdir(power_supply_path):
        return "N/A"

    for entry in os.listdir(power_supply_path):
        if entry.startswith("BAT"):
            capacity_path = os.path.join(power_supply_path, entry, "capacity")

            try:
                with open(capacity_path, "r") as f:
                    percent = f.read().strip()
                    return f"{percent}%"
            except (FileNotFoundError, ValueError):
                continue

    return "N/A"
