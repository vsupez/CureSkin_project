from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchDetails(Page):
    IMAGE = (By.CSS_SELECTOR, "modal-opener img")
    PRICE = (By.CSS_SELECTOR, "div.product__info-container div.price__sale")
    REVIEWS = (By.CSS_SELECTOR, "div.product__info-container div.jdgm-prev-badge")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div.product__info-container button[type='submit']")
    BUY_IT_NOW_BUTTON = (By.CSS_SELECTOR, "button[data-testid = Checkout-button]")


    def verify_UI_of_product(self):
        self.wait_for_element_appear(*self.IMAGE)
        self.wait_for_element_appear(*self.PRICE)
        self.wait_for_element_appear(*self.REVIEWS)
        self.wait_for_element_appear(*self.ADD_TO_CART_BUTTON)
        self.wait_for_element_appear(*self.BUY_IT_NOW_BUTTON)
