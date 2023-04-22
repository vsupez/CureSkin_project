from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH = (By.CSS_SELECTOR, "search-modal.header__search")
    SEARCH_BOX = (By.ID, "Search-In-Modal")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.predictive-search__item--term")
    def open_main(self):
        self.open_url("https://shop.cureskin.com/")

    def search_for_product(self,text):
        self.click(*self.SEARCH)
        self.input_text(text, *self.SEARCH_BOX)
        self.click(*self.SEARCH_BUTTON)


    def verify_main_page_opened(self):
        print("************************************")
        url = self.driver.current_url
        print(str(url))
        assert (url == "https://shop.cureskin.com/")

