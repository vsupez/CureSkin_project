from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pages.main_page import MainPage


class ShoppingPage(MainPage):
    SLIDER_LOW = (By.CSS_SELECTOR, "div.is-lower")
    SLIDER_HIGH = (By.CSS_SELECTOR, "div.is-upper")
    PRODUCTS = (By.CSS_SELECTOR, "div.collection ul li")
    PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, "ul#product-grid li")
    NEXT = (By.CSS_SELECTOR, "li a.pagination__item--prev")

    def adjust_price_filter(self):
        price_slider = self.driver.find_element(*self.SLIDER_LOW)
        actions = ActionChains(self.driver)
        actions.click_and_hold(price_slider).move_by_offset(100, 0).release().perform()
        sleep(5)

    def verify_number_of_product_changed(self):
        new_products = self.find_elements(*self.PR_PAGES)
        print(f"New product pages are {len(new_products)}")
        assert new_products != self.product_pages, "Products did not changed after adjusting the slider"

    def verify_price_within_range(self):
        # lowest price
        low_price = (self.find_element(*self.SLIDER_LOW)).get_attribute("aria-valuenow")
        low_price = int(low_price[4:])
        print(f"Low price range selected is {low_price}")

        # Highest price
        high_price = self.find_element(*self.SLIDER_HIGH).get_attribute("aria-valuenow")
        high_price = int(high_price[4:])
        print(f"High price range selected is {high_price}")

        # Get products on current page
        products_on_page = self.find_elements(*self.PRODUCTS)
        print(f"Products on this page are {len(products_on_page)}")

        while 1:
            products = self.find_elements(*self.PRODUCTS_ON_PAGE)

            for product in products:
                price = product.find_element(By.CSS_SELECTOR, "bdi").get_attribute("outerText")
                price = int(price[3:6])
                print(f"Price is {price}")
                assert low_price <= price <= high_price, "Filtered products price not in the specified range"

            try:
                self.click(*self.NEXT)
            except:
                break
