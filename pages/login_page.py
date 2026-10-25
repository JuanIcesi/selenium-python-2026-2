from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        time.sleep(3)
        self.click(self.LOGIN_BUTTON)
