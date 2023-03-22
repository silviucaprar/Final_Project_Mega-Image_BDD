from pages.mega_image_homepage import Home_page
from pages.mega_image_cartpage import Cart_page
from pages.mega_image_loginpage import Login_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.login_page_object = Login_page()
    context.cart_page_object = Cart_page()

def after_all(context):
    context.browser.close()