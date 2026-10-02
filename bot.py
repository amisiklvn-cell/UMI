import subprocess
import socket
import os
import json


SETTINGS_FILE = "umi_settings.json"
USER_NAME = "User"


def load_settings():
    global USER_NAME

    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as file:
                settings = json.load(file)

            USER_NAME = settings.get("name", "User")

        except:
            USER_NAME = "User"


def save_settings():
    settings = {
        "name": USER_NAME
    }

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file)

def change_name():
    global USER_NAME

    print(f"\nCurrent name: {USER_NAME}")

    new_name = input("Enter new name: ").strip()

    if not new_name:
        print("❌ Name cannot be empty.")
        speak("Name was not changed.")
        return

    USER_NAME = new_name
    save_settings()

    print(f"\n✅ Name changed to {USER_NAME}.")
    speak("Your name has been changed.")


# ==========================
# UMI VOICE
# ==========================

def speak(message):
    full_message = f"{USER_NAME}, {message}"

    subprocess.Popen(
        ["termux-tts-speak", full_message],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


# ==========================
# INTERNET CHECK
# ==========================

def internet_available():
    try:
        socket.create_connection(
            ("1.1.1.1", 53),
            timeout=3
        )
        return True
    except OSError:
        return False


# ==========================
# UPDATE
# ==========================

def update():
    print("\n🔄 Updating Termux...\n")

    if not internet_available():
        print("❌ No internet connection.")
        speak("Update failed. No internet connection.")
        return

    result = subprocess.run(
        ["pkg", "update", "-y"]
    )

    if result.returncode == 0:
        print("\n✅ Update finished.")
        speak("Update finished.")
    else:
        print("\n❌ Update failed.")
        speak("Update failed.")


# ==========================
# UPGRADE
# ==========================

def upgrade():
    print("\n⬆️ Upgrading Termux...\n")

    if not internet_available():
        print("❌ No internet connection.")
        speak("Upgrade failed. No internet connection.")
        return

    result = subprocess.run(
        ["pkg", "upgrade", "-y"]
    )

    if result.returncode == 0:
        print("\n✅ Upgrade finished.")
        speak("Upgrade finished.")
    else:
        print("\n❌ Upgrade failed.")
        speak("Upgrade failed.")


# ==========================
# CLEAN
# ==========================

def clean():
    print("\n🧹 Cleaning Termux...\n")

    result = subprocess.run(
        ["apt", "clean"]
    )

    if result.returncode == 0:
        print("\n✅ Clean finished.")
        speak("Clean finished.")
    else:
        print("\n❌ Clean failed.")
        speak("Clean failed.")


# ==========================
# INSTALL PACKAGE
# ==========================

def install_package():
    package = input("\n📦 Enter package name: ").strip()

    if not package:
        print("❌ No package name entered.")
        speak("No package name entered.")
        return

    # Check if package is already installed
    installed = subprocess.run(
        ["dpkg", "-s", package],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if installed.returncode == 0:
        print(f"\n✅ {package} is already installed.")
        speak(f"{package} is already installed.")
        return

    # Check internet connection
    if not internet_available():
        print("❌ No internet connection.")
        speak("Package installation failed. No internet connection.")
        return

    print(f"\n📦 Installing {package}...\n")

    result = subprocess.run(
        ["pkg", "install", package, "-y"]
    )

    if result.returncode == 0:
        print(f"\n✅ {package} installation finished.")
        speak(f"{package} installation finished.")
    else:
        print(f"\n❌ {package} installation failed.")
        speak(f"{package} installation failed.")
    # Check if package is already installed
    installed = subprocess.run(
        ["dpkg", "-s", package],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if installed.returncode == 0:
        print(
            f"\n✅ {package} is already installed."
        )
        speak(
            f"{package} is already installed."
        )
        return

    # Check internet before installing
    if not internet_available():
        print(
            "\n❌ No internet connection."
        )
        speak(
            "Package installation failed. "
            "No internet connection."
        )
        return

    print(
        f"\n📦 Installing {package}...\n"
    )

    result = subprocess.run(
        ["pkg", "install", package, "-y"]
    )

    if result.returncode == 0:
        print(
            f"\n✅ {package} installation finished."
        )
        speak(
            f"{package} installation finished."
        )
    else:
        print(
            f"\n❌ {package} installation failed."
        )
        speak(
            f"{package} installation failed."
        )


# ==========================
# MAIN MENU
# ==========================

def main():

    load_settings()

    if not os.path.exists(SETTINGS_FILE):
        global USER_NAME

        USER_NAME = input("Enter your name: ").strip()

        if not USER_NAME:
            USER_NAME = "User"

        save_settings()

    # Startup display
    subprocess.run(
        ["figlet", "UMI"]
    )

    # Startup announcement
    speak("UMI started")

    while True:
        print("\n")
        print("==========================")
        print("          🤖 UMI")
        print("==========================")
        print("1. 🔄 Update")
        print("2. ⬆️ Upgrade")
        print("3. 🧹 Clean")
        print("4. 📦 Install Package")
        print("5. 👤 Change Name")
        print("6. 🚪 Exit")
        print("==========================")

        choice = input(
            "Choose: "
        ).strip()

        if choice == "1":
            update()

        elif choice == "2":
            upgrade()

        elif choice == "3":
            clean()

        elif choice == "4":
            install_package()

        elif choice == "5":
            change_name()

        elif choice == "6":
            print("\n👋 UMI stopped.")
            speak("UMI stopped")
            break

        else:
            print("\n❌ Invalid choice.")
            speak("Invalid choice")




# ==========================
# START UMI
# ==========================

if __name__ == "__main__":
    main()
