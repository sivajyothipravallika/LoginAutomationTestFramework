import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import HEADLESS, BASE_URL

@pytest.fixture(params=["chromium", "firefox", "webkit"],scope="session")
def browser(request):
    with sync_playwright() as pw:
        browser_type = getattr(pw, request.param)
        browser = browser_type.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"reports/{request.node.name}.png")
        context.tracing.stop(path=f"reports/{request.node.name}-trace.zip")
    context.close()


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
