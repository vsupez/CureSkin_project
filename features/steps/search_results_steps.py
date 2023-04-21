from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open search results page Search: 18 results found for {search_word}")
def open_search_results_page(context, search_word):
    context.driver.get("https://shop.cureskin.com/search?q=cure")


@when("Click on CureSkin logo in the header")
def click_logo(context):
    context.app.search_results.click_logo()


@then("Verify user is taken to the main page")
def verify_main_opened(context):
    context.app.main_page.verify_main_page_opened()
