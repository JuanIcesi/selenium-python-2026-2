from selenium.webdriver.common.by import By
from .base_page import BasePage


class ImdbSearchPage(BasePage):
    SEARCH_FIELD = (By.ID, "suggestion-search")
    FIRST_RESULT = (
        By.CSS_SELECTOR,
        "#react-autowhatever-navSuggestionSearch--item-0 a",
    )

    def open(self):
        urls = (
            "https://www.imdb.com/",
            "https://www.imdb.com/?ref_=nv_home",
            "https://www.imdb.com/?ref_=nv_sr_home",
        )
        for url in urls:
            self.driver.get(url)
            if self.is_visible(self.SEARCH_FIELD):
                return
        raise AssertionError("La página principal de IMDb no cargó correctamente")

    def search_movie(self, movie):
        self.enter_text(self.SEARCH_FIELD, movie)

    def open_first_result(self):
        self.click(self.FIRST_RESULT)
