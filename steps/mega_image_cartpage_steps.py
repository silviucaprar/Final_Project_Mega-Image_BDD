from behave import *

@when('Cart page: The user adds one extra "Apa minerala naturala plata 5L" in the shopping cart')
def step_impl(context):
    context.cart_page_object.add_one_extra_apa_bucovina_to_cart()

@then('Cart page: The user checks if the total price is correctly displayed')
def step_impl(context):
    context.cart_page_object.check_if_total_price_is_correctly_displayed()

@when('Cart page: The user removes the product from shopping cart')
def step_impl(context):
    context.cart_page_object.remove_item_from_shopping_cart()

@then('Cart page: The user check if the shopping cart is empty')
def step_impl(context):
    context.cart_page_object.check_if_shopping_cart_is_empty()

@when('Cart page: The user sorts the products after "Pretul produsului"')
def step_impl(context):
    context.cart_page_object.sort_products_in_shopping_cart()

@then('Cart page: The user checks if the products were sorted correctly')
def step_impl(context):
    context.cart_page_object.check_if_products_in_shopping_cart_are_sorted_correctly()

@then('Cart page: The user check if the total price for the two products is correctly displayed')
def step_impl(context):
    context.cart_page_object.check_if_totalprice_for_sum_of_two_is_correct()



