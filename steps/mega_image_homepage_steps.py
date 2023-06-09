from behave import *

@given('Home page: The user is on https://www.mega-image.ro/')
def step_impl(context):
    context.home_page_object.clear_cookies()
    context.home_page_object.navigate_to_homepage()
    context.home_page_object.accept_cookies()

@when('Home page: The user clicks on "Contul meu"')
def step_impl(context):
    context.home_page_object.navigate_to_login_page()

@then('Home page: The user is logged in successfully')
def step_impl(context):
    context.home_page_object.check_if_login_is_successfull()

@when('Home page: The user searches for "{product_name}" in the search box')
def step_impl(context, product_name):
    context.home_page_object.insert_search_value(product_name)
    context.home_page_object.click_search_button()

@then('Home page: The user gets at least "{no_of_results}" results returned')
def step_impl(context, no_of_results):
    context.home_page_object.check_search_results(no_of_results)

@when('Home page: The user adds one "Apa minerala naturala plata 5L" to shopping cart')
def step_impl(context):
    context.home_page_object.add_apa_bucovina_to_cart()

@when('Home page: The user navigates to shopping cart')
def step_impl(context):
    context.home_page_object.navigate_to_shopping_cart()

@when('Home page: The user navigates to "Cosmetice si ingrijire personala"')
def step_impl(context):
    context.home_page_object.navigate_to_cosmetice_si_ingrijire_personala()

@when('Home page: The user checks the ">100RON" filter')
def step_impl(context):
    context.home_page_object.check_over_100RON_filter()

@then('Home page: The user checks if all filtered products prices are over 100 RON')
def step_impl(context):
    context.home_page_object.check_if_prices_are_over_100RON()

@when('Home page: The user searches for "apa naturala 5l bucovina" and adds it to shopping cart')
def step_impl(context):
    context.home_page_object.search_for_apa_and_close_offers()

@when('Home page: The user searches for "paine cu secara 400g Vita" and adds it to shopping cart')
def step_impl(context):
    context.home_page_object.search_for_paine_cu_secara_vita()

@when('Home page: The user searches for "cascaval 350g desenvis", adds it and navigates to shopping cart')
def step_impl(context):
    context.home_page_object.search_for_cascaval_desenvis()

@when('Home page: The user adds "Pesto cu busuioc", "Paste alimentare" and navigates to shopping cart')
def step_impl(context):
    context.home_page_object.add_pesto_si_paste_to_shopping_cart()



