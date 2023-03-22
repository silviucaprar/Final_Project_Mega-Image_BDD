from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base_page):

    HOMEPAGE = "https://www.mega-image.ro/"
    PRODUCT_PRICE = (By.XPATH, '//div[@data-testid="product-block-price"]')
    PRICE = (By.XPATH, '(//div[@data-testid="product-block-price"])[1]')
    TOTAL_PRICE = (By.XPATH, '//span[@data-testid="total-price"]')
    ADD_ITEM = (By.XPATH, '//button[@data-testid="product-block-quantity-increase"]')
    REMOVE_ITEM = (By.XPATH, '//button[@data-testid="product-block-quantity-decrease"]')
    EMPTY_CART = (By.XPATH, '//div[@data-testid="text-container"]//span')
    SORTEAZA_DUPA = (By.XPATH, '//select[@data-testid="sort-select"]')
    FIRST_PRICE = (By.XPATH, '(//div[@data-testid="product-block-price"])[1]')
    SECOND_PRICE = (By.XPATH, '(//div[@data-testid="product-block-price"])[2]')

    def add_one_extra_apa_bucovina_to_cart(self):
        self.chrome.find_element(*self.ADD_ITEM).click()

    def check_if_total_price_is_correctly_displayed(self):
        price = self.chrome.find_element(*self.PRICE)
        price_text = price.text
        value = float(price_text.replace(' Lei', '').replace(',', '.'))
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.TOTAL_PRICE, "Lei 15,98"))
        actual_value = float(self.chrome.find_element(*self.TOTAL_PRICE).text.replace('Lei ', '').replace(',', '.'))
        expected_value = value * 2
        assert expected_value == actual_value, f"ERROR: Expected {expected_value}, Actual: {actual_value}"

    def remove_item_from_shopping_cart(self):
        self.chrome.find_element(*self.REMOVE_ITEM).click()

    def check_if_shopping_cart_is_empty(self):
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.TOTAL_PRICE, "Lei 0,00"))
        expected = "Cosul tau este gol"
        actual = self.chrome.find_element(*self.EMPTY_CART).text
        assert expected == actual, f"ERROR: Expected: {expected}, Actual: {actual}"

    def sort_products_in_shopping_cart(self):
        sort_price = Select(self.chrome.find_element(*self.SORTEAZA_DUPA))
        sort_price.select_by_visible_text("Pretul produsului")

    def check_if_products_in_shopping_cart_are_sorted_correctly(self):
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.FIRST_PRICE, "7,39 Lei"))
        prices = self.chrome.find_elements(*self.PRODUCT_PRICE)
        prices = [float(price.text.replace(' Lei', '').replace(',', '.')) for price in prices[:3]]
        assert prices == sorted(prices), f"ERROR: Expected: {prices}, Actual: {sorted(prices)}"

    def check_if_totalprice_for_sum_of_two_is_correct(self):
        first_price_text = self.chrome.find_element(*self.FIRST_PRICE).text
        firstprice = float(first_price_text.replace(' Lei', '').replace(',', '.'))
        second_price_text = self.chrome.find_element(*self.SECOND_PRICE).text
        secondprice = float(second_price_text.replace(' Lei', '').replace(',', '.'))
        sum_of_two = firstprice + secondprice
        total_text = self.chrome.find_element(*self.TOTAL_PRICE).text
        totalprice = float(total_text.replace('Lei ', '').replace(',', '.'))
        assert sum_of_two == totalprice, f"ERROR: Expected: {sum_of_two}, Actual: {totalprice}"

