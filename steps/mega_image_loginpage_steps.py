from behave import *

@when('Login page: The user enters an invalid email and clicks "Continua"')
def step_impl(context):
    context.login_page_object.enter_invalid_email()

@then('Login page: The user checks if the error for invalid email is displayed')
def step_impl(context):
    context.login_page_object.check_invalid_email_error()

@when('Login page: The user enters a valid email and clicks "Continua"')
def step_impl(context):
    context.login_page_object.enter_valid_email()

@when('Login page: The user enters an invalid password and clicks "Creeaza un cont nou"')
def step_impl(context):
    context.login_page_object.enter_invalid_password()

@then('Login page: The user checks if the error for invalid password is displayed')
def step_impl(context):
    context.login_page_object.check_invalid_password_error()

@when('Login page: The user enters a valid password and clicks "Creeaza un cont nou"')
def step_impl(context):
    context.login_page_object.enter_valid_password()

@then('Login page: The user checks if the error for not checking "Terms and Conditions" is displayed')
def step_impl(context):
    context.login_page_object.check_terms_and_conditions_error()

@when('Login page: The user enters an existing valid email and clicks "Continua"')
def step_impl(context):
    context.login_page_object.enter_existing_email()

@when('Login page: The user enters a valid password and clicks "Autentificare"')
def step_impl(context):
    context.login_page_object.enter_existing_password_and_login()
