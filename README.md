# hwreport

  <a href="#what-it-shows">What it Displays when ran</a> •
  <a href="#installation">Install</a> •
  <a href="#usage">How to Use</a> •
  <a href="#edit-the-config">Edit Configuration File</a> •
  <a href="#use-a-specific-editor">Choose a specific editor to change config</a> •
  <a href="#settings-menu">Settings menu</a>
</p>

A simple CLI tool that shows your computer's hardware and system info.

Run one command and see your CPU, GPU, RAM, display, battery, OS, and kernel version. No digging through system settings.

## What it shows

- CPU
- GPU
- RAM
- Display (resolution, screen size, refresh rate)
- Battery (shows N/A if you are on a desktop with no battery)
- OS
- Kernel
- And more in the future!

You can turn any of these on or off in the config file.

## Installation

1. Download and unzip hwreport.
2. Open a terminal and go into the hwreport folder.
3. Run the install script with sudo.

```bash
cd hwreport
sudo ./install.sh
```

4. Now you can run it from anywhere.

```bash
hwreport
```

### If you get "command not found"

If `sudo ./install.sh` says something like `command not found`, the install script probably is not marked as runnable yet. Fix it with this command, then try again.

```bash
chmod +x install.sh
sudo ./install.sh
```

If it still does not work after that, you can run it through bash directly instead.

```bash
sudo bash install.sh
```

## Usage

Just run the command with nothing after it to see your hardware info.

```bash
hwreport
```

### Edit the config

Turn components on or off, or change which one shows first. This opens the config file in your default terminal text editor.

```bash
hwreport --config
```

### Use a specific editor

If you want to pick the editor yourself, name it after this flag. For example, to use Nano;

```bash
hwreport --config-editor nano
```

### Settings menu

Opens a menu to repair, uninstall, or check for updates.

```bash
hwreport --settings
```

This will ask for sudo when you pick an option, since it changes files outside your user folder.

## The config file

The config file lives here:

```
~/.config/hwreport/hwreport.conf
```

Each line is a component, set to 1 to show it or 0 to hide it.

```
CPU=1
GPU=1
RAM=1
DISPLAY=1
BATTERY=1
OS=1
KERNEL=1
```

## Something wrong?

If something is showing wrong, or not showing at all? Let me know.
