from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open the Cureskin Application")
def open_cureskin(context):
    context.app.main_page.open_main()


@given("Open search results page Search: 18 results found for {search_word}")
def open_search_results_page(context, search_word):
    context.driver.get("https://shop.cureskin.com/search?q=cure")


@when("Click on CureSkin logo in the header")
def click_logo(context):
    context.app.search_results.click_logo()


@when("Search for {text}")
def search_for_product(context, text):
    context.app.main_page.search_for_product(text)


@when("Click on the product from Search Results")
def click_on_product(context):
    context.app.search_results.click_on_product()


@then("Verify user is taken to the main page")
def verify_main_opened(context):
    context.app.main_page.verify_main_page_opened()


@then("Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button")
def verify_UI_product_page(context):
    context.app.search_details.verify_UI_of_product()
