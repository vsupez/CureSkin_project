from behave import given, when, then


@given("Open cureskin homepage")
def open_cureskin(context):
    context.app.main_page.open_main()


@when("Search for {text}")
def search_for_product(context, text):
    context.app.main_page.search_for_product(text)


@when("Click on Shop All section")
def click_shop_all(context):
    context.app.main_page.click_shop_all()


@then("Identify the footer links: Terms of Service, Refund Policy, Privacy Policy, shipping policy and Verify each "
      "link navigates to correct pages")
def verify_footer_links(context):
    context.app.main_page.verify_footer_links()