import sys

import config
import output
import settings
from collectors import cpu, gpu, ram, display, battery, system


def run_report():
    # loads the config and prints a line for every component that is turned on
    # the order here always matches COMPONENT_ORDER in constants.py
    user_config = config.load_config()

    if user_config["CPU"] == "1":
        output.print_line("CPU", cpu.get_cpu())

    if user_config["GPU"] == "1":
        output.print_line("GPU", gpu.get_gpu())

    if user_config["RAM"] == "1":
        output.print_line("RAM", ram.get_ram())

    if user_config["DISPLAY"] == "1":
        for display_line in display.get_displays():
            output.print_line("DISPLAY", display_line)

    if user_config["BATTERY"] == "1":
        output.print_line("BATTERY", battery.get_battery())

    if user_config["OS"] == "1":
        output.print_line("OS", system.get_os())

    if user_config["KERNEL"] == "1":
        output.print_line("KERNEL", system.get_kernel())

    output.print_footer()


def main():
    args = sys.argv[1:]

    if not args:
        run_report()
        return

    if args[0] == "--config":
        config.open_config_in_editor()
        return

    if args[0] == "--config-editor":
        if len(args) < 2:
            print("Please name an editor, for example: hwreport --config-editor nano")
            return
        config.open_config_in_editor(editor_override=args[1])
        return

    if args[0] == "--settings":
        settings.run_settings_menu()
        return

    print(f"Unknown option: {args[0]}")


if __name__ == "__main__":
    main()
