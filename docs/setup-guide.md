# Complete Setup-Guide

**Installation and configuration guide for the Swag Labs Test Automation Framework**

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Android Emulator Setup](#android-emulator-setup)
- [Appium Server Configuration](#appium-server-configuration)
- [TAF Configuration](#taf-configuration)
- [Running Tests](#running-tests)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Python** 3.10+
- **Nox** (Task automation)
- **Node.js & npm** 18+
- **Appium Server** 3+
- **Android SDK** with platform-tools
- **Java JDK** 11+

---

## Installation Steps
⚠️ **Only for Windows users**: Open PowerShell as Administrator
```powershell
# Install Chocolatey (Windows Package Manager)
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
    [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Verify installation
choco --version
```
### 1. Clone this repository:

**Precondition:** Install git

```bash
git clone https://github.com/AlejandroAreiza/alejandro-areiza_betsson.git
cd alejandro-areiza_betsson
```

### 2. Install Python 3.10+

**macOS (using Homebrew):**
```bash
brew install python
```

**Windows (using Chocolatey):**
```bash
choco install python
```

**Verify installation:**
```bash
python --version  # 3.10+ required
```

### 3. Install Nox

**All platforms:**
```bash
# task automation tool
pip install nox

nox --version
```

### 4. Verify Requirements

```bash
# Check what requirements are needed/missing
nox -s verify_requirements
```

⚠️ **If any requirement is missing, install them using the instructions below**

---

### 1. Install Java JDK 11+

**macOS (using Homebrew):**
```bash
brew install openjdk@11
```

**Windows (using Chocolatey):**
```bash
choco install openjdk11
```

**Verify installation:**
```bash
java -version  # Should show version 11 or higher
```

---

### 2. Install Node.js & npm

**macOS (using Homebrew):**
```bash
#Install Node.js (LTS) & npm
brew install node
```

**Windows (using Chocolatey):**
```bash
#Install Node.js (LTS) & npm
choco install nodejs-lts
```

**Verify installation:**
```bash
node --version && npm --version
```

---

### 3. Install Appium 3+

**All platforms:**
```bash
npm install -g appium
```

**Install driver for Android:**
```bash
appium driver install uiautomator2
```

**Install driver for iOS:**
```bash
appium driver install xcuitest
```

**Verify installation:**
```bash
appium --version  # Should show 3.x.x
```

---

### 4. Install Android Studio & Android SDK

Download Android Studio from: https://developer.android.com/studio

#### macOS Installation

1. Download Android Studio for macOS (.dmg file)
2. Install by dragging to Applications folder
3. Launch Android Studio and follow the setup wizard
4. Ensure "Android SDK" and "Android SDK Platform" are selected during setup
5. After installation, add environment variables to `~/.zshrc` or `~/.bashrc`:

```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_HOME/emulator
```

6. Reload your shell configuration:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

#### Windows Installation

1. Download Android Studio for Windows (.exe file)
2. Run the installer and follow the setup wizard
3. Ensure "Android SDK" and "Android SDK Platform" are selected during setup
4. After installation, set environment variables via System Properties > Environment Variables:
   - Create `ANDROID_HOME` variable: `C:\Users\<YourUsername>\AppData\Local\Android\Sdk`
   - Add to PATH:
     - `%ANDROID_HOME%\platform-tools`
     - `%ANDROID_HOME%\cmdline-tools\latest\bin`
     - `%ANDROID_HOME%\emulator`

#### Verify Android SDK Installation

```bash
adb --version
sdkmanager --version
```
---

## Android Emulator Setup

### Create Emulator
Create android emulator manual -> https://developer.android.com/studio/run/managing-avds

or for simplicity use **nox automation tasks**
```bash
# Creates a Pixel device with Android API 35 (auto-detects OS)
nox -s create_emulator
```

### Start Emulator

```bash
# Normal mode with GUI
nox -s start_emulator

# Headless mode (no GUI)
nox -s start_emulator -- --headless
```

### Stop Emulator

```bash
nox -s stop_emulator
```

### Verify Emulator is Running

```bash
adb devices  # Should list your emulator
```

---

## Appium Server Configuration

### Start Appium Server

```bash
# Starts Appium server on http://127.0.0.1:4723
nox -s start_appium
```

### Stop Appium Server

```bash
nox -s stop_appium
```

---

## TAF Configuration

### APK/IPA Location

**⚠️ Place your APK/IPA always in the app folder**

The Android APK is already included in the repository:
```
business/app/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk
```

### Desired Capabilities

Edit `drivers/desired_capabilities.json` to configure your app settings.

**Template Android Configuration:**
```json
{
  "platformName": "Android",
  "automationName": "UiAutomator2",
  "deviceName": "<emulator_name>",
  "app": "app.apk",
  "appPackage": "com.yourapp.package",
  "appActivity": "com.yourapp.MainActivity",
  "noReset": false,
  "fullReset": false,
  "newCommandTimeout": 300,
  "autoGrantPermissions": true
}
```

**Configuration Parameters:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `platformName` | Target platform | `"Android"` or `"iOS"` |
| `automationName` | Automation engine | `"UiAutomator2"` (Android), `"XCUITest"` (iOS) |
| `deviceName` | Emulator/device name | `"test_pixel_35"`|
| `app` | place your APK/IPA in app folder| `"app.apk"` |
| `appPackage` | Android app package ID | `"com.swaglabsmobileapp"` |
| `appActivity` | Main activity to launch | `"com.swaglabsmobileapp.MainActivity"` |
| `noReset` | Keep app data between sessions | `false` or `true` |
| `fullReset` | Uninstall app after session | `false` or `true` |
| `newCommandTimeout` | Session timeout (seconds) | `300` |
| `autoGrantPermissions` | Auto-grant app permissions | `true` |

---

## Troubleshooting

### Common Issues

**1. Emulator not starting:**
- Verify Android emulator is started: `nox -s start-emulator`
- Verify Android SDK is installed: `adb --version`
- Check available emulators: `emulator -list-avds`

**2. Appium connection errors:**
- Verify appium server is started: `nox -s start-appium`
- Verify Appium is running: Check `http://127.0.0.1:4723/status`
- Ensure UIAutomator2 driver is installed: `appium driver list`
- Check device is connected: `adb devices`

**3. Test execution failures:**
- Verify desired capabilities
- Check app package and activity names
- Check logs in reports/logs

**4. Python dependency issues:**
- Delete `.venv` folder and reinstall: `nox -s clean` `nox -s install`
- Verify Python version: `python --version`

**5. Android SDK not found:**
- Verify `ANDROID_HOME` is set: `echo $ANDROID_HOME`
- Verify `adb` is accessible: `adb --version`

---

**Setup complete?** Return to [README](../README.md) for Quick Start instructions.
