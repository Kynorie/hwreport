import os
import shutil
import urllib.request
import json
import zipfile
import tempfile

from constants import (
    GITHUB_API_RELEASES,
    RELEASE_ASSET_NAME,
    INSTALL_BIN_PATH,
    INSTALL_LIB_PATH,
    CONFIG_DIR,
)
from version import VERSION


def is_root():
    # checks if the script is being run with sudo
    return os.geteuid() == 0


def get_latest_release():
    # hits the github api and returns the latest release info as a dict
    # returns None if the request fails for any reason
    try:
        with urllib.request.urlopen(GITHUB_API_RELEASES) as response:
            releases = json.loads(response.read())
    except Exception:
        return None

    if not releases:
        return None

    return releases[0]


def get_release_by_tag(tag):
    try:
        with urllib.request.urlopen(GITHUB_API_RELEASES) as response:
            releases = json.loads(response.read())
    except Exception:
        return None

    for release in releases:
        if release.get("tag_name") == tag:
            return release

    return None


def download_release_zip(release):
    assets = release.get("assets", [])

    download_url = None
    for asset in assets:
        if asset.get("name") == RELEASE_ASSET_NAME:
            download_url = asset.get("browser_download_url")
            break

    if not download_url:
        return None

    temp_path = os.path.join(tempfile.gettempdir(), RELEASE_ASSET_NAME)

    try:
        urllib.request.urlretrieve(download_url, temp_path)
    except Exception:
        return None

    return temp_path


def install_from_zip(zip_path):
    extract_dir = tempfile.mkdtemp()

    try:
        with zipfile.ZipFile(zip_path, "r") as zip_file:
            zip_file.extractall(extract_dir)
    except zipfile.BadZipFile:
        print("The downloaded file was not a valid zip. Aborting.")
        return False

    if os.path.exists(INSTALL_LIB_PATH):
        shutil.rmtree(INSTALL_LIB_PATH)

    shutil.copytree(extract_dir, INSTALL_LIB_PATH)
    shutil.rmtree(extract_dir)

    return True


def repair():
    if not is_root():
        print("Run this with sudo!")
        return

    tag = f"v{VERSION}"
    print(f"Looking for release {tag}...")

    release = get_release_by_tag(tag)

    if not release:
        print(f"Could not find a release tagged {tag} on GitHub.")
        return

    zip_path = download_release_zip(release)

    if not zip_path:
        print(f"Could not find {RELEASE_ASSET_NAME} in that release.")
        return

    print("Reinstalling files...")
    success = install_from_zip(zip_path)

    if success:
        print("Repair complete.")
    else:
        print("Repair failed.")


def uninstall():
    if not is_root():
        print("Run this with sudo!")
        return

    if os.path.exists(INSTALL_BIN_PATH):
        os.remove(INSTALL_BIN_PATH)

    if os.path.exists(INSTALL_LIB_PATH):
        shutil.rmtree(INSTALL_LIB_PATH)

    print("hwreport has been uninstalled.")

    answer = input("Do you want to uninstall the configurations? [Y/N] ").strip().lower()

    if answer == "y":
        if os.path.exists(CONFIG_DIR):
            shutil.rmtree(CONFIG_DIR)
        print("Configuration files removed.")
    else:
        print("Configuration files kept.")


def check_for_updates():
    if not is_root():
        print("Run this with sudo!")
        return

    release = get_latest_release()

    if not release:
        print("Could not check for updates right now.")
        return

    latest_tag = release.get("tag_name", "")
    latest_version = latest_tag.lstrip("v")

    if latest_version == VERSION:
        print("Your version of hwreport is up to date.")
        return

    answer = input(
        f"There's a new version of hwreport available! ({latest_tag}), "
        f"do you want to install it?\n\nY/N "
    ).strip().lower()

    if answer != "y":
        return

    zip_path = download_release_zip(release)

    if not zip_path:
        print(f"Could not find {RELEASE_ASSET_NAME} in that release.")
        return

    print("Installing update...")
    success = install_from_zip(zip_path)

    if success:
        print("Update complete.")
    else:
        print("Update failed.")


def run_settings_menu():
    print("1. Repair")
    print("2. Uninstall")
    print("3. Check For Updates")
    print()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        repair()
    elif choice == "2":
        uninstall()
    elif choice == "3":
        check_for_updates()
    else:
        print("Not a valid option.")
