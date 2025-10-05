# Swag Labs - Test Automation Framework
---

## Introduction

BDD-based mobile test automation framework for Swag Labs Android app using Behave, Python, and Appium. This framework provides a scalable, maintainable approach to mobile testing with clean architecture patterns and comprehensive quality checks.

### Key Features

* **BDD Testing**: Business-readable test scenarios using Gherkin syntax enabling collaboration between business stakeholders and technical teams
* **Page Object Model**: Clean architecture separating test logic from UI implementation for enhanced maintainability and scalability
* **Cross-Platform Ready**: Built for Android with extensible architecture supporting iOS integration
* **Nox Sessions**: Automated task runner providing isolated, reproducible test environments and streamlined CI/CD workflows

### Project Structure

```
.
|-- business/                # Business logic layer
|   |-- app/                 # Specific folder to place your (APK/IPA)
|   |-- screens/             # Screen/Page Object Model classes
|-- config/                  # Configuration layer
|   |-- dto/                 # Data Transfer Objects
|   |-- drivers/             # Driver factory (Android/iOS)
|   |   |-- android_driver/  # Android-driver implementation
|   |   |-- ios_driver/      # iOS-driver implementation
|   |-- config_files/        # desired capabilities and settings
|   |-- utils/               # Reusable utilities across the framework
|-- tests/                   # Test layer
|   |-- features/            # BDD feature files and step definitions
|   |   |-- steps/           # Step definitions
|-- docs/                    # setup-guide, exploratory-testing, test-cases
|-- README.md/               # README first
|-- noxfile.py               # Nox automation sessions
|-- pyproject.toml           # Dependencies and tool configurations
```

---

## Documentation

- **[Setup Guide](docs/setup-guide.md)** - Complete installation guide
- **[Exploratory Testing](docs/exploratory_testing.md)** - Familiarization with the app. Findings and Ideas
- **[Test Cases](docs/test_cases.md)** - Test Case documentation

---

## Setup

### Prerequisites

Install required tools first: **[Setup Guide](docs/setup-guide.md)** - Python, Java, Node.js, Android SDK, and Appium

### Quick Start

```bash
# ommit if already cloned
git clone https://github.com/AlejandroAreiza/alejandro-areiza_betsson.git
cd alejandro-areiza_betsson
```

```bash
# Verify all requirements are installed (if not go to SetUp Guide):
nox -s verify_requirements

# Install project dependencies:
nox -s install

# Create Android emulator (Pixel API 35).
nox -s create_emulator

# Run tests
nox -s run_test

# Get Test Results
nox -s get_report
```

---


## Quick Tasks

```bash
nox -l               # list all tasks
nox -s format        # Format code with black & isort
nox -s quality_check # Run linter and type checking
nox -s clean         # Clean environent and reports
```

---

## Test Results

Test reports and logs are generated in `reports/` after each run

### Bonus: Allure Reports (Optional)

For enhanced reporting with interactive dashboards, charts, and test history:

**1. Install Allure CLI:**
```bash
# macOS
brew install allure

# Windows
scoop install allure
```

**2. Generate and view reports:**
```bash
# Run tests
nox -s run_test

# Generate static HTML report
nox -s allure_generate

# Auto-generate and serve report (opens in browser)
nox -s allure_serve
```

**Features:**
- Interactive test execution timeline
- Step-by-step test breakdown with Allure decorators
- Automatic failure screenshots
- Test history and trends
- Detailed error stack traces

---

## Advanced Test Execution

Run specific tests using nox with Behave parameters:

```bash
# Run all tests
nox -s run_test

# Run specific feature file
nox -s run_test -- user_authentication.feature

# Run tests with tags
nox -s run_test -- --tags=@regression
nox -s run_test -- --tags=@smoke

# Run specific scenario by name
nox -s run_test -- -n "Login attempt with invalid credentials"
```

---

## Known Bugs 🐛

During testing, the following bugs were identified in the Swag Labs application:

### 1. Typo in Order Confirmation Message - Priority Low
**Severity:** Low
**Description:** The order confirmation popup displays "THANK YOU FOR YOU ORDER" instead of the grammatically correct "THANK YOU FOR YOUR ORDER".
**Location:** Checkout Overview screen
**Expected:** "THANK YOU FOR YOUR ORDER"
**Actual:** "THANK YOU FOR YOU ORDER"

### 2. Checkout Allows Empty Cart Purchase - Priority Critical
**Severity:** Critical
**Description:** The checkout process completes successfully even when all products are removed from the cart during the checkout overview step. The system should prevent order completion when the cart is empty.
**Steps to Reproduce:**
1. Add products to cart
2. Proceed to checkout and fill in shipping information
3. On the checkout overview screen, remove all products by swiping left
4. Tap "Finish" button
5. Order completes successfully with confirmation popup

**Expected:** Order should fail or display error when cart is empty
**Actual:** Order completes successfully and displays "THANK YOU FOR YOU ORDER" popup

---

## Future Improvements

Ideas to enhance the test automation framework:

### 1. Docker Integration
- Containerize test environment for complete isolation
- Include Appium server, Android emulator, and dependencies in Docker Compose
- Enable consistent execution in CICD

### 2. Jira Integration
- Automatic bug creation on test failures with screenshots and logs
- Link test cases to Jira requirements for traceability

### 3. Enhanced Logging with Observer Pattern
- Implement subscriber pattern for centralized log management
- Real-time log streaming to multiple outputs (console, file, external services)

### 4. Method Chaining for Fluent API
- Implement chainable methods in screen classes for improved readability
- Example: `login_screen.enter_username("user").enter_password("pass").tap_login()`
- Reduce code verbosity and enhance test maintainability

### 5. iOS Driver Implementation
- Complete cross-platform support with iOS driver
- Platform-specific configurations with unified test layer

---

## Author

**Alejandro Areiza**
Test Automation Framework - Betsson Technical Assessment
