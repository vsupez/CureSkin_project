from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH = (By.CSS_SELECTOR, "search-modal.header__search")
    SEARCH_BOX = (By.ID, "Search-In-Modal")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.predictive-search__item--term")
    SHOP_ALL = (By.CSS_SELECTOR, "nav.cure_header a[href='/collections/all']")
    PR_PAGES = (By.CSS_SELECTOR, "ul.pagination__list li")
    product_pages = 0

    def open_main(self):
        self.open_url("https://shop.cureskin.com/")

    def search_for_product(self, text):
        self.click(*self.SEARCH)
        self.input_text(text, *self.SEARCH_BOX)
        self.click(*self.SEARCH_BUTTON)


    def verify_main_page_opened(self):
        print("************************************")
        url = self.driver.current_url
        print(str(url))
        assert (url == "https://shop.cureskin.com/")

    def click_shop_all(self):
        self.click(*self.SHOP_ALL)
        product_pages = self.find_elements(*self.PR_PAGES)
        pages = len(product_pages)
        print(f"Previous range product pages are {pages}")
