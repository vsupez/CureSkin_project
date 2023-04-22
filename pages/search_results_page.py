from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger


class SearchResults(Page):
    LOGO = (By.CSS_SELECTOR, "a img.small-hide")
    PRODUCT = (By.CSS_SELECTOR, "ul#product-grid li")

    def click_logo(self):
        logger.info("Clicking logo on search results page")
        self.click(*self.LOGO)

    def click_on_product(self):
        logger.info("Clicking on the first product")
        self.click(*self.PRODUCT)
