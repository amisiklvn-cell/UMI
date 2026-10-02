UMI

UMI is a simple Python-based maintenance assistant for Termux on Android.

Features

- 🔄 Update Termux
- ⬆️ Upgrade Termux
- 🧹 Clean package cache
- 📦 Install Termux packages
- 👤 Change the UMI user's name
- 🔊 Voice announcements
- 🎨 UMI startup display
- 🌐 Internet connection checking

Requirements

- Android phone
- Termux
- Python
- Termux:API
- Internet connection for update, upgrade, and package installation

Installation

Clone the repository:

git clone https://github.com/amisiklvn-cell/UMI.git

Enter the UMI directory:

cd UMI

Run UMI:

python bot.py

Voice

UMI uses Termux:API for voice announcements.

Install the Termux API package:

pkg install termux-api

The Termux:API Android application is also required.

Privacy

UMI saves the user's chosen name locally in "umi_settings.json".

This personal settings file is excluded from Git using ".gitignore".

License

See the "LICENSE" file for license information.
