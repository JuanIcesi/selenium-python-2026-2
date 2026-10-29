from selenium.webdriver.common.by import By
import time
from .base_page import BasePage


class LobbyLoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    LOGIN_BTN = (By.ID, "btn-login")

    def login(self, username):
        self.enter_text(self.USERNAME_FIELD, username)
        self.click(self.LOGIN_BTN)
