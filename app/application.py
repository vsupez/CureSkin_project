from pages.search_results_page import SearchResults
from pages.main_page import MainPage
from pages.search_details_page import SearchDetails


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.search_results = SearchResults(driver)
        self.main_page = MainPage(driver)
        self.search_details = SearchDetails(driver)