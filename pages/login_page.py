from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = "input[id='username']"
    PASSWORD_INPUT = "input[type='password']"
    SUBMIT_BUTTON = "button[type='submit']"
    # ERROR_MESSAGE = "[class*='error'], [role='alert']"
    ERROR_MESSAGE = ".alert-message"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def open(self):
        self.navigate(BASE_URL)
        self.dismiss_cookie_banner()
        return self

    def enter_username(self, username:str):
        self.page.wait_for_selector(self.USERNAME_INPUT)
        self.page.fill(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password:str):
        self.page.wait_for_selector(self.PASSWORD_INPUT)
        self.page.fill(self.PASSWORD_INPUT, password)
        return self
    
    def click_submit(self):
        self.page.click(self.SUBMIT_BUTTON)
        #self.page.wait_for_load_state("domcontentloaded")
        return self
    
    def login(self, username:str, password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        return self

    def get_error_message(self) -> str:
        el = self.page.locator(self.ERROR_MESSAGE)
        return el.inner_text() if el.is_visible() else ""

    def is_login_page(self) -> bool:
        return self.page.locator(self.USERNAME_INPUT).is_visible()
