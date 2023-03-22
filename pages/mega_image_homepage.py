from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class Home_page(Base_page):

    HOMEPAGE = "https://www.mega-image.ro/"
    CONTUL_MEU_BUTTON = (By.XPATH, '//button[@data-testid="header-myhub-toggle"]')
    CLOSE_OFERTE_PERSONALIZATE = (By.XPATH, '//button[@data-testid="dialog-close-button"]')
    GREETING = (By.XPATH, '//h3[@data-testid="header-myhub-greeting"]')
    COSMETICE_INGRIJIRE = (By.XPATH, '//a[@href="/Cosmetice-si-ingrijire-personala/c/012"]')
    FILTER_OVER100RON = (By.XPATH, '(//input[@data-testid="facet-item-checkbox"])[6]')
    PRODUCT_PRICE = (By.XPATH, '//div[@data-testid="product-block-price"]')
    SEARCH_TEXTBOX = (By.XPATH, '//input[@aria-label="Cauta"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-testid="header-search-submit"]')
    APA_BUCOVINA = (By.XPATH, '(//a[@href="/Apa-si-sucuri/Apa/Apa-plata/Apa-minerala-naturala-plata-5L/p/31658"])[3]')
    DELIVERY_CLOSE_BUTTON = (By.XPATH, '(//button[@aria-label="Inchide"])[2]')
    ADAUGA_BUTTON = (By.XPATH, '(//button[@data-testid="product-block-add"])[1]')
    SHOPPING_CART = (By.XPATH, '//a[@data-testid="header-minibasket"]')
    PAINE_SECARA = (By.XPATH, '(//a[@href="/Paine-cafea-cereale-si-mic-dejun/Paine-si-specialitati/Paine/Paine-cu-secara-400g/p/90669"])[3]')
    CASCAVAL_DESENVIS = (By.XPATH, '(//a[@href="/Lactate-si-oua/Branzeturi/Cascaval/Cascaval-350g/p/82856"])[3]')
    BROASCA_SI_CALUT = (By.XPATH, '(//button[@data-testid="product-block-add"])[1]')

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE)

    def navigate_to_login_page(self):
        self.chrome.find_element(*self.CONTUL_MEU_BUTTON).click()

    def search_apa_bucovina(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("apa naturala 5l bucovina")
        try:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        except StaleElementReferenceException:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_if_product_searched_is_found(self):
        expected = "Apa minerala naturala plata 5L"
        actual = self.chrome.find_element(*self.APA_BUCOVINA).text
        assert expected == actual, f"ERROR: Expected: {expected}, Actual: {actual}"

    def add_apa_bucovina_to_cart(self):
        sleep(2)
        self.chrome.find_element(*self.ADAUGA_BUTTON).click()
        try:
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.DELIVERY_CLOSE_BUTTON))
            self.chrome.find_element(*self.DELIVERY_CLOSE_BUTTON).click()
        except:
            pass

    def navigate_to_shopping_cart(self):
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.SHOPPING_CART, "1"))
        self.chrome.find_element(*self.SHOPPING_CART).click()

    def navigate_to_cosmetice_si_ingrijire_personala(self):
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.COSMETICE_INGRIJIRE))
        self.chrome.find_element(*self.COSMETICE_INGRIJIRE).click()

    def check_over_100RON_filter(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_all_elements_located(self.PRODUCT_PRICE))
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(Keys.PAGE_DOWN)
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.FILTER_OVER100RON))
        self.chrome.find_element(*self.FILTER_OVER100RON).click()

    def check_if_prices_are_over_100RON(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_all_elements_located(self.PRODUCT_PRICE))
        price_elements = self.chrome.find_elements(*self.PRODUCT_PRICE)
        for price_element in price_elements:
            price_value = float(price_element.text.replace(' Lei', '').replace(',', '.'))
            assert price_value > 100, "Price is not greater than 100."

    def check_if_login_is_successfull(self):
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.CLOSE_OFERTE_PERSONALIZATE))
        self.chrome.find_element(*self.CLOSE_OFERTE_PERSONALIZATE).click()
        self.chrome.find_element(*self.CONTUL_MEU_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.GREETING, "Buna, Silviu"))
        expected = "Buna, Silviu"
        actual = self.chrome.find_element(*self.GREETING).text
        assert expected == actual, f"ERROR: Expected: {expected} Actual: {actual}"

    def search_for_apa_and_close_offers(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("apa naturala 5l bucovina")
        try:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        except StaleElementReferenceException:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()

        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.APA_BUCOVINA))
        self.chrome.find_element(*self.ADAUGA_BUTTON).click()
        try:
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.DELIVERY_CLOSE_BUTTON))
            self.chrome.find_element(*self.DELIVERY_CLOSE_BUTTON).click()
        except:
            pass
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.SHOPPING_CART, "1"))

    def search_for_paine_cu_secara_vita(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("paine cu secara 400g Vita")
        try:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        except StaleElementReferenceException:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.PAINE_SECARA))
        self.chrome.find_element(*self.ADAUGA_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.SHOPPING_CART, "2"))

    def search_for_cascaval_desenvis(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("cascaval 350g desenvis")
        try:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        except StaleElementReferenceException:
            self.chrome.find_element(*self.SEARCH_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.CASCAVAL_DESENVIS))
        self.chrome.find_element(*self.ADAUGA_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.SHOPPING_CART, "3"))
        self.chrome.find_element(*self.SHOPPING_CART).click()

    def add_broasca_calut_to_shopping_cart(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(Keys.PAGE_DOWN)
        self.chrome.find_element(*self.BROASCA_SI_CALUT).click()
        self.chrome.find_element(*self.BROASCA_SI_CALUT).click()
        try:
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.DELIVERY_CLOSE_BUTTON))
            self.chrome.find_element(*self.DELIVERY_CLOSE_BUTTON).click()
        except:
            pass
        WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(self.SHOPPING_CART, "2"))
        self.chrome.find_element(*self.SHOPPING_CART).click()

