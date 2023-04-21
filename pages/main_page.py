from pages.base_page import Page


class MainPage(Page):
    def verify_main_page_opened(self):
        print("************************************")
        url = self.driver.current_url
        print(str(url))
        assert (url == "https://shop.cureskin.com/")

