from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open search results page Search: 18 results found for {search_word}")
def open_search_results_page(context, search_word):
    context.driver.get("https://shop.cureskin.com/search?q=cure")


@when("Click on CureSkin logo in the header")
def click_logo(context):
    context.app.search_results.click_logo()




@when("Click on the product from Search Results")
def click_on_product(context):
    context.app.search_results.click_on_product()


@when("Adjust the Price Filter such that there is a change in number of products")
def adjust_price_filter(context):
    context.app.shopping_page.adjust_price_filter()


@then("Verify user is taken to the main page")
def verify_main_opened(context):
    context.app.main_page.verify_main_page_opened()


@then("Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button")
def verify_UI_product_page(context):
    context.app.search_details.verify_UI_of_product()


@then("Verify that number of products changes")
def verify_number_of_product_changed(context):
    context.app.shopping_page.verify_number_of_product_changed()


@then("Verify that products displayed are within the Price filter")
def verify_price_within_range(context):
    context.app.shopping_page.verify_price_within_range()