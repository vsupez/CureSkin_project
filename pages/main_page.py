from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH = (By.CSS_SELECTOR, "search-modal.header__search")
    SEARCH_BOX = (By.ID, "Search-In-Modal")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.predictive-search__item--term")
    SHOP_ALL = (By.CSS_SELECTOR, "nav.cure_header a[href='/collections/all']")
    PR_PAGES = (By.CSS_SELECTOR, "ul.pagination__list li")
    product_pages = 0
    FOOTER_LN = (By.XPATH, "//footer-accordion[3]//a")
    HEADER = (By.XPATH, "//div//h1")
    LOGO = (By.CSS_SELECTOR, "a.header__heading-link.focus-inset")

    def open_main(self):
        self.open_url("https://shop.cureskin.com/")

    def search_for_product(self, text):
        self.click(*self.SEARCH)
        self.input_text(text, *self.SEARCH_BOX)
        self.wait_for_element_click(*self.SEARCH_BUTTON)



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

    def verify_footer_links(self):
        # headless
        footer_links = self.find_elements(*self.FOOTER_LN)
        link_count = len(footer_links)

        for i in range(link_count):
            link_to_click = self.find_elements(*self.FOOTER_LN)[i]
            link_text = link_to_click.text
            link_to_click.click()

            page_header_text = self.find_element(*self.HEADER).text
            print(f"Clicked link {i}")
            print(link_text)
            print(page_header_text)
            assert link_text.lower() == page_header_text.lower(), "Correct page isn't opened after clicking footer link"

            self.click(*self.LOGO)  # Go bak to home page


