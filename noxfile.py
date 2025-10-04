import nox
import os
import platform
from pathlib import Path


@nox.session(python=False)
def install(session):
    """Install project dependencies."""
    session.run("python3", "-m", "venv", ".venv", silent=True)
    session.run(".venv/bin/pip", "install", "--upgrade", "pip", silent=True)
    session.run(".venv/bin/pip", "install", "-e", ".[dev]")


@nox.session(python=False)
def verify_requirements(session):
    """Verify all system requirements (Node, Java, Python, Android SDK, Appium)."""
    print("=" * 40)
    print("Verifying System Requirements...")
    print("=" * 40)
    print()

    requirements = {
        "Python": ["python3", "--version"],
        "Java JDK": ["java", "-version"],
        "Node.js": ["node", "--version"],
        "npm": ["npm", "--version"],
        "Appium": ["appium", "--version"],
        "adb": ["adb", "--version"],
    }

    for name, cmd in requirements.items():
        print(f"Checking {name}...")
        try:
            session.run(*cmd, silent=True, external=True)
            print(f"✅ {name} installed")
        except Exception:
            print(f"❌ {name} not found")
            session.error(f"{name} is required")
        print()

    # Check UIAutomator2 driver
    print("Checking Appium UIAutomator2 driver...")
    try:
        result = session.run(
            "appium", "driver", "list", "--installed",
            silent=True, external=True
        )
        if "uiautomator2" in str(result).lower():
            print("✅ UIAutomator2 driver installed")
        else:
            print("❌ UIAutomator2 driver not found")
            print("Install with: appium driver install uiautomator2")
            session.error("UIAutomator2 driver required")
    except Exception:
        print("❌ Failed to check UIAutomator2 driver")
        session.error("Appium driver check failed")
    print()

    # Check ANDROID_HOME
    print("Checking Android SDK (ANDROID_HOME)...")
    android_home = os.environ.get("ANDROID_HOME")
    if not android_home:
        print("❌ ANDROID_HOME not set")
        session.error("ANDROID_HOME environment variable required")
    if not Path(android_home).exists():
        print(f"❌ ANDROID_HOME directory does not exist: {android_home}")
        session.error("ANDROID_HOME directory not found")
    print(f"✅ ANDROID_HOME set: {android_home}")
    print()

    print("=" * 40)
    print("✅ All requirements verified!")
    print("=" * 40)

@nox.session(python=False)
def create_emulator(session):
    """Create Android emulator (Pixel API 35)."""
    print("=" * 40)
    print("Creating Android Emulator (Pixel API 35)...")
    print("=" * 40)
    print()

    print("Detecting system architecture...")
    arch = platform.machine().lower()

    if arch in ["arm64", "aarch64"]:
        system_arch = "arm64-v8a"
        print("✅ Detected ARM64 (Apple Silicon/ARM)")
    elif arch in ["x86_64", "amd64"]:
        system_arch = "x86_64"
        print("✅ Detected x86_64 (Intel)")
    else:
        print(f"❌ Unsupported architecture: {arch}")
        session.error("Unsupported system architecture")

    system_image = f"system-images;android-35;google_apis;{system_arch}"
    print(f"System image: {system_image}")
    print()

    print("Checking if system image is installed...")
    result = session.run(
        "sdkmanager", "--list_installed",
        silent=True, external=True
    )
    if system_image not in str(result):
        print(f"📦 Installing system image for API 35 ({system_arch})...")
        session.run("sdkmanager", system_image, external=True, silent=True)
    else:
        print("✅ System image already installed")
    print()

    print("Checking if emulator 'test_pixel_35' already exists...")
    result = session.run("avdmanager", "list", "avd", silent=True, external=True)
    if "test_pixel_35" in str(result):
        print("⚠️  Emulator 'test_pixel_35' already exists")
    else:
        print("Creating emulator 'test_pixel_35'...")
        session.run(
            "bash", "-c",
            f'echo "no" | avdmanager create avd -n test_pixel_35 -k "{system_image}" -d "pixel"',
            external=True, silent=True
        )
        print()
        print("=" * 40)
        print("✅ Emulator 'test_pixel_35' created!")
        print("=" * 40)
        print()
        print("To start the emulator, run:")
        print("  nox -s start_emulator")

@nox.session(python=False)
def start_emulator(session):
    """Start Android emulator."""
    print("=" * 40)
    print("Starting Android Emulator...")
    print("=" * 40)
    print()

    print("Checking for running emulators...")
    result = session.run("adb", "devices", silent=True, external=True)
    if "emulator" in str(result):
        print("✅ Emulator already running!")
        session.run("adb", "devices", external=True)
        print()
        print("To stop it, run: nox -s stop_emulator")
        return

    print("No emulator running.")
    print()
    print("Starting emulator 'test_pixel_35'...")

    headless = "--headless" in session.posargs
    if headless:
        print("Starting in HEADLESS mode...")
        session.run(
            "bash", "-c",
            "emulator -avd test_pixel_35 -no-window -no-audio -no-boot-anim > /dev/null 2>&1 &",
            external=True, silent=True
        )
    else:
        print("Starting emulator...")
        session.run(
            "bash", "-c",
            "emulator -avd test_pixel_35 > /dev/null 2>&1 &",
            external=True, silent=True
        )

    print()
    print("Waiting for emulator to boot...")
    session.run("adb", "wait-for-device", external=True, silent=True)
    session.run("sleep", "5", external=True, silent=True)

    result = session.run(
        "adb", "shell", "getprop", "sys.boot_completed",
        silent=True, external=True
    )
    if "1" in str(result):
        print("✅ Emulator is fully booted!")
    else:
        print("⚠️  Emulator starting (may take a few more seconds)...")

    print()
    print("Running emulators:")
    session.run("adb", "devices", external=True)
    print()
    print("To stop emulator: nox -s stop_emulator")

@nox.session(python=False)
def stop_emulator(session):
    """Stop running Android emulator."""
    print("=" * 40)
    print("Stopping Android Emulator...")
    print("=" * 40)
    print()

    result = session.run("adb", "devices", silent=True, external=True)
    if "emulator" not in str(result):
        print("✅ No emulator running (already stopped)")
        return

    print("Running emulators:")
    session.run("bash", "-c", "adb devices | grep emulator", external=True)
    print()

    session.run(
        "bash", "-c",
        "for device in $(adb devices | grep emulator | awk '{print $1}'); do adb -s $device emu kill 2>/dev/null; done",
        external=True, silent=True
    )
    session.run("sleep", "2", external=True, silent=True)
    print()
    print("✅ Emulator(s) stopped!")

@nox.session(python=False)
def start_appium(session):
    """Start Appium server."""
    print("=" * 40)
    print("Starting Appium Server...")
    print("=" * 40)
    print()

    result = session.run(
        "pgrep", "-f", "appium",
        silent=True, external=True, success_codes=[0, 1]
    )
    if result and result.strip():
        print("✅ Appium server already running!")
        print("To stop it, run: nox -s stop_appium")
        return

    print("Starting Appium server on http://127.0.0.1:4723...")
    Path("reports/logs").mkdir(parents=True, exist_ok=True)

    session.run(
        "bash", "-c",
        "appium > reports/logs/appium.log 2>&1 & echo $! > /tmp/appium.pid",
        external=True, silent=True
    )
    session.run("sleep", "3", external=True, silent=True)

    result = session.run(
        "pgrep", "-f", "appium",
        silent=True, external=True, success_codes=[0, 1]
    )
    if result and result.strip():
        print()
        print("✅ Appium server started successfully!")
        print("   URL: http://127.0.0.1:4723")
        print("   Logs: reports/logs/appium.log")
        print()
        print("To stop server: nox -s stop_appium")
    else:
        print("❌ Failed to start Appium server")
        print("Check logs: reports/logs/appium.log")
        session.error("Appium server failed to start")

@nox.session(python=False)
def stop_appium(session):
    """Stop Appium server."""
    print("=" * 40)
    print("Stopping Appium Server...")
    print("=" * 40)
    print()

    result = session.run(
        "bash", "-c", "pgrep -f appium 2>/dev/null || true",
        silent=True, external=True
    )
    if not result or not result.strip():
        print("✅ Appium server not running (already stopped)")
        return

    print("Stopping Appium server...")
    session.run(
        "bash", "-c",
        "pkill -f appium 2>/dev/null || true; rm -f /tmp/appium.pid; sleep 1",
        external=True, silent=True
    )
    print()
    print("✅ Appium server stopped!")

@nox.session(python=False)
def lint(session):
    """Run flake8 linter."""
    print("=" * 40)
    print("Running Flake8 Linter...")
    print("=" * 40)
    session.run(".venv/bin/flake8", "config/")
    print("✅ Linting passed!")

@nox.session(python=False)
def format(session):
    """Format code with isort and black."""
    print("=" * 40)
    print("Formatting Code...")
    print("=" * 40)
    print("\n📦 Sorting imports with isort...")
    session.run(".venv/bin/isort", "config/", "business/", "tests/")
    print("\n🎨 Formatting with black...")
    session.run(".venv/bin/black", "config/", "business/", "tests/")
    print("✅ Formatting complete!")

@nox.session(python=False)
def type_check(session):
    """Run mypy type checking."""
    print("=" * 40)
    print("Running MyPy Type Checking...")
    print("=" * 40)
    session.run(".venv/bin/mypy", "--explicit-package-bases", "config/")
    print("✅ Type checking passed!")

@nox.session(python=False)
def quality_check(session):
    """Run all quality checks (lint + type-check)."""
    session.notify("lint")
    session.notify("type_check")
    print()
    print("=" * 40)
    print("✅ All quality checks passed!")
    print("=" * 40)

@nox.session(python=False)
def run_test(session):
    """
    Run tests.

    Usage:
        nox -s run_test                                    # Run all tests
        nox -s run_test -- basic                           # Run basic.feature
        nox -s run_test -- basic "Launch app"              # Run specific scenario by name
        nox -s run_test -- login "Successful login"        # Run specific scenario in login.feature
    """
    if session.posargs:
        # Get test name from arguments
        test_name = session.posargs[0]

        # Add .feature extension if not present
        if not test_name.endswith('.feature'):
            test_name = f"{test_name}.feature"

        test_path = f"tests/features/{test_name}"

        # Check if scenario name is provided
        if len(session.posargs) > 1:
            scenario_name = session.posargs[1]
            print(f"Running scenario '{scenario_name}' in {test_path}")
            session.run(".venv/bin/behave", test_path, "-n", scenario_name, "-v", "--no-capture")
        else:
            print(f"Running test: {test_path}")
            session.run(".venv/bin/behave", test_path, "-v", "--no-capture")
    else:
        print("Running all tests...")
        session.run(".venv/bin/behave", "tests/features/", "-v", "--no-capture")


@nox.session(python=False)
def clean(session):
    """Clean the environment, removes reports and logs."""
    print("Cleaning environment...")

    session.run(
        "bash", "-c",
        'find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true',
        external=True, silent=True
    )
    session.run(
        "bash", "-c",
        'find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true',
        external=True, silent=True
    )
    session.run(
        "bash", "-c",
        'find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true',
        external=True, silent=True
    )
    session.run(
        "bash", "-c",
        "rm -rf reports/ allure-results/ allure-report/",
        external=True, silent=True
    )
    session.run(
        "bash", "-c",
        'find . -type f -name "*.pyc" -delete',
        external=True, silent=True
    )
    session.run(
        "bash", "-c",
        'find . -type f -name "*.log" -delete',
        external=True, silent=True
    )
    session.run("rm", "-rf", ".venv", external=True, silent=True)
    print("✅ Environment cleaned (including .venv)!")
