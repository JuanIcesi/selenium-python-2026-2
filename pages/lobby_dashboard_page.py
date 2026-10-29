from selenium.webdriver.common.by import By
from .base_page import BasePage


class LobbyDashboardPage(BasePage):
    USERNAME = (By.CLASS_NAME, "participant-name")

    def find_username(self, username):
        usernames = self.find_elements(self.USERNAME)
        for user in usernames:
            if user.text == username:
                return True
        return False
