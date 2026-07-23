from playwright.sync_api import expect
from utils.config import BASE_URL, LOGIN_USERNAME, LOGIN_PASSWORD
from pages.login_page import LoginPage
import re

class TestLogin:
    def test_login_page_loads(self, login_page):
        assert login_page.is_login_page()
    
    def test_valid_login(self, login_page):
        login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        login_page.page.wait_for_url(lambda url:"/login" not in url, timeout=15000)
        assert  "Experian" in login_page.get_title()
        
    def test_invalid_login(self, login_page):
        login_page.login("wrong@email.com", "wrongpassword")
        login_page.page.wait_for_selector(LoginPage.ERROR_MESSAGE)
        assert login_page.get_error_message() == "Invalid username or password"
    
    