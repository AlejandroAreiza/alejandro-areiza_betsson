# Swag Labs Test Automation Framework

Cross-platform test automation framework for Swag Labs Android application using Behave, Python, and Appium.

## Features

- **BDD Testing**: Behave framework with Gherkin syntax
- **Cross-Platform**: Supports Android and iOS
- **Page Object Model**: Clean separation of concerns
- **Data-Driven**: JSON-based test data
- **Code Quality**: Black, Flake8, MyPy integration
- **Scalable**: Modular architecture for easy expansion
- **MakeFile**: List of instructions to easlily build project and run tests

## Project Structure

```
.
|-- app/                 # Android/iOS app files (APK/IPA)
|-- config/              # Configuration files (capabilities, settings)
|-- drivers/             # Driver factory and desired capabilities
|-- features/            # BDD feature files and step definitions
|   |-- steps/           # Step definitions
|   |-- test_data/       # Test data (JSON files)
|-- pages/               # Page Object Model classes
|-- utils/               # Utility functions and helpers
|-- reports/             # Test reports (git-ignored)
|-- Makefile             # Common commands
|-- pyproject.toml       # Dependencies and tool configurations
```

## Prerequisites

- Python 3.10+
- Node.js & npm 18+
- Appium Server 3+
- Android SDK with platform-tools
- Java JDK 11+
- Make

## Installation

#### 1. Download repo
```bash
git clone https://github.com/AlejandroAreiza/alejandro-areiza_betsson.git

cd alejandro-areiza_betsson
```

#### 2. Install Make
```bash

#for macOS
xcode-select --install

#for Windows
choco install make
```

#### 3. Verify Requirements
```bash
# check what requirements are needed / you missed
make verify-requirements
```


⚠️ **If any requirement is missing, install them as follows:**

##### - Install Python 3.10+
```bash
# macOS (using Homebrew)
brew install python@3.10

# Windows (using Chocolatey)
choco install python --version=3.10
```

##### - Install Java JDK 11+
```bash
# macOS (using Homebrew)
brew install openjdk@11

# Windows (using Chocolatey)
choco install openjdk11
```

##### - Install Node.js & npm 18+
```bash
# macOS (using Homebrew)
brew install node@18

# Windows (using Chocolatey)
choco install nodejs --version=18.0.0
```

##### - Install Appium 3+
```bash
# macOS/Linux
npm install -g appium

# Windows
npm install -g appium

# Install UIAutomator2 driver for Android (all platforms)
appium driver install uiautomator2
```

##### - Install Android Studio (includes Android SDK)
Download Android Studio from:
https://developer.android.com/studio

```bash
# macOS
# 1. Download Android Studio for macOS (.dmg file)
# 2. Install Android Studio by dragging it to Applications folder
# 3. Launch Android Studio and follow the setup wizard
# 4. During setup, ensure "Android SDK" and "Android SDK Platform" are selected
# 5. After installation, add to ~/.zshrc or ~/.bashrc:
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_HOME/emulator

# Windows
# 1. Download Android Studio for Windows (.exe file)
# 2. Run the installer and follow the setup wizard
# 3. During setup, ensure "Android SDK" and "Android SDK Platform" are selected
# 4. After installation, set environment variables (System Properties > Environment Variables):
#    ANDROID_HOME=C:\Users\<YourUsername>\AppData\Local\Android\Sdk
# 5. Add to PATH:
#    %ANDROID_HOME%\platform-tools
#    %ANDROID_HOME%\cmdline-tools\latest\bin
#    %ANDROID_HOME%\emulator

# Verify installation (after adding to PATH and restarting terminal):
adb --version
sdkmanager --version
```


#### 4. Install Python Project Dependencies
```bash
make install
```

This will:
1. Create a virtual environment (.venv)
2. Install all dependencies from pyproject.toml

## Setup Android Emulator

#### Create Emulator: 
```bash
# Creates a Pixel device with Android API 35 (auto-detects OS)
make create-emulator
```

#### Start/Stop Emulator
```bash
make start-emulator              # Normal mode
make start-emulator HEADLESS=true # Headless mode

# stopsemulator
make stop-emulator
```

## Appium Server

#### Start/Stop Appium Server
```bash
# starts Appium server on http://127.0.0.1:4723
make start-appium

# stops appium server
make stop-appium
```


## TAF Configuration

#### APK Location
Android APK is already located in the `app/` folder:
```
app/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk
```

#### Desired Capabilities
Edit `drivers/desired_capabilities.json` to configure your app settings.

**Template:**
```json
{
  "platformName": "Android",
  "automationName": "UiAutomator2",
  "deviceName": "<emulator_name>",
  "app": "/absolute/path/to/your/app.apk",
  "appPackage": "com.yourapp.package",
  "appActivity": "com.yourapp.MainActivity",
  "noReset": false,
  "fullReset": false,
  "newCommandTimeout": 300,
  "autoGrantPermissions": true
}
```

**Configuration Guide:**
- `platformName`: Target platform (Android/iOS)
- `automationName`: Automation engine (UiAutomator2 for Android, XCUITest for iOS)
- `deviceName`: Name of your emulator (e.g., "test_pixel_35")
- `app`: **Absolute path** to your APK/IPA file
- `appPackage`: Android app package identifier
- `appActivity`: Main activity to launch
- `noReset`: Keep app data between sessions
- `fullReset`: Uninstall app after session
- `newCommandTimeout`: Session timeout in seconds
- `autoGrantPermissions`: Auto-grant app permissions


#### Run Test
```bash
# run all the tests in the features folder
make run-test
```

## Utils

#### Code Quality

```bash
make lint          # Run flake8 linter (check only)
make format        # Format code with black (modifies files)
make type-check    # Run mypy type checking
make quality-check # Run all checks (lint + type-check)
```

#### Clean Environment
```bash
# Removes cache, reports, logs, and .venv
make clean
```
