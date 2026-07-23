from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def navigate(self, url:str):
        self.page.goto(url, wait_until="domcontentloaded")
    def get_title(self) -> str:
        return self.page.title()
    def get_url(self) -> str:
        return self.page.url
    def dismiss_cookie_banner(self):
        try:    
            cookie_btn = self.page.locator("#ensCloseBanner")
            cookie_btn.wait_for(state="visible", timeout=5000)
            cookie_btn.click()
        except PlaywrightTimeoutError:
            pass