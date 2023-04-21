from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger


class SearchResults(Page):
    LOGO = (By.CSS_SELECTOR, "a img.small-hide")

    def click_logo(self):
        logger.info("Clicking logo on search results page")
        self.click(*self.LOGO)
