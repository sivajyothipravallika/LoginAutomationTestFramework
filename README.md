# Login Automation Test Framework

A Python-based UI test automation framework for login functionality, built with [Playwright](https://playwright.dev/python/) and [pytest](https://pytest.org/).

## Features

- Cross-browser testing: **Chromium**, **Firefox**, and **WebKit**
- Page Object Model (POM) design pattern
- Automatic screenshot capture on test failure
- Playwright tracing (screenshots + snapshots) for failed tests
- HTML test reports via `pytest-html`
- Environment-based configuration via `.env` file

## Project Structure

```
LoginAutomationTestFramework/
├── conftest.py              # pytest fixtures (browser, page, login_page)
├── pytest.ini               # pytest configuration
├── requirements.txt         # Python dependencies
├── pages/
│   ├── __init__.py
│   ├── base_page.py         # Base page with common browser actions
│   └── login_page.py        # Login page object
├── tests/
│   ├── __init__.py
│   └── test_login.py        # Login test cases
├── utils/
│   ├── __init__.py
│   └── config.py            # Environment variable loader
└── reports/                 # Test artifacts (screenshots, traces, HTML report)
```

## Prerequisites

- Python 3.8+
- pip

## Setup

1. **Clone the repository** and navigate to the project root.

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

4. **Create a `.env` file** in the project root with the following variables:
   ```env
   BASE_URL=https://your-app-url.com
   LOGIN_USERNAME=your_username
   LOGIN_PASSWORD=your_password
   HEADLESS=true
   DEFAULT_TIMEOUT=10000
   NAVIGATION_TIMEOUT=30000
   ```

## Running Tests

**Run all tests (all browsers):**
```bash
pytest tests/
```

**Run on a specific browser:**
```bash
pytest tests/ --browser chromium
pytest tests/ --browser firefox
pytest tests/ --browser webkit
```

**Run with HTML report:**
```bash
pytest tests/ --html=reports/report.html --self-contained-html -v
```

**Run in headed mode (visible browser):**
Set `HEADLESS=false` in your `.env` file, then run normally.

## Test Cases

| Test | Description |
|------|-------------|
| `test_login_page_loads` | Verifies the login page renders with the username input visible |
| `test_valid_login` | Logs in with valid credentials and asserts successful navigation |
| `test_invalid_login` | Logs in with wrong credentials and asserts the error message |

## Failure Artifacts

On test failure, the framework automatically saves:
- **Screenshot** → `reports/<test_name>.png`
- **Playwright trace** → `reports/<test_name>-trace.zip`

To inspect a trace:
```bash
playwright show-trace reports/<test_name>-trace.zip
```

## Dependencies

| Package | Version |
|---------|---------|
| playwright | 1.44.0 |
| pytest-playwright | 0.5.0 |
| pytest | 8.2.0 |
| python-dotenv | 1.0.1 |
| pytest-html | 4.1.1 |
