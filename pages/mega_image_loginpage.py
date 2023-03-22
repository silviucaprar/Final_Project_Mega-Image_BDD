from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page(Base_page):

    LOGIN_PAGE = "https://www.mega-image.ro/reg/welcome"
    CONTUL_MEU_BUTTON = (By.XPATH, '//button[@data-testid="header-myhub-toggle"]')
    CONTUL_MEU_INPUT = (By.ID, "emailOrPhoneNumber")
    CONTINUA_BUTTON = (By.XPATH, '//button[@name="sumbit"]')
    FORM_ERR_MSG = (By.XPATH, '//p[@data-testid="form-error-message"]')
    PASSWORD_INPUT = (By.ID, "new-password")
    PASSWORD_ERR_MSG = (By.XPATH, '//p[@data-testid="password-error-message"]')
    CREEAZA_CONT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    TERMS_AND_CONDITIONS = (By.XPATH, '//input[@data-testid="save-card-checkbox"]')
    TERMS_ERR_MSG = (By.XPATH, '//p[@data-testid="checkbox__error-message"]')
    CURRENT_PASSWORD = (By.XPATH, '//input[@id="current-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-testid="login-button"]')

    def navigate_to_login_page(self):
        self.chrome.get(self.LOGIN_PAGE)

    def enter_invalid_email(self):
        self.chrome.find_element(*self.CONTUL_MEU_INPUT).send_keys("silviu,caprar@gmail.com")
        self.chrome.find_element(*self.CONTINUA_BUTTON).click()

    def check_invalid_email_error(self):
        expected = "Te rugam sa introduci un format valid"
        actual = self.chrome.find_element(*self.FORM_ERR_MSG).text
        assert expected == actual, f"ERROR: Expected: {expected} Actual: {actual}"

    def enter_valid_email(self):
        self.chrome.find_element(*self.CONTUL_MEU_INPUT).send_keys("silviu@gmail.com")
        sleep(2)
        self.chrome.find_element(*self.CONTINUA_BUTTON).click()

    def enter_invalid_password(self):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys("Pass123")
        self.chrome.find_element(*self.CREEAZA_CONT_BUTTON).click()

    def check_invalid_password_error(self):
        expected = "Te rugam sa introduci o parola care indeplineste conditiile"
        actual = self.chrome.find_element(*self.PASSWORD_ERR_MSG).text
        assert expected == actual, f"ERROR: Expected: {expected}, Actual: {actual}"

    def enter_valid_password(self):
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys("Pass123!")
        self.chrome.find_element(*self.CREEAZA_CONT_BUTTON).click()

    def check_terms_and_conditions_error(self):
        expected = "Te rugam sa accepti termenii si conditiile"
        actual = self.chrome.find_element(*self.TERMS_ERR_MSG).text
        assert expected == actual, f"ERROR: Expected: {expected}, Actual: {actual}"

    def enter_existing_email(self):
        self.chrome.find_element(*self.CONTUL_MEU_INPUT).send_keys("silviu.caprar@gmail.com")
        sleep(3)
        self.chrome.find_element(*self.CONTINUA_BUTTON).click()

    def enter_existing_password_and_login(self):
        self.chrome.find_element(*self.CURRENT_PASSWORD).send_keys("Pass123!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
