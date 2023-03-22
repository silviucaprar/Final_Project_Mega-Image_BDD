from selenium.webdriver.common.by import By
from browser import Browser

class Base_page(Browser):

    COOKIES_BUTTON = (By.XPATH, '//button[@data-testid="cookie-popup-accept"]')

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.COOKIES_BUTTON).click()
        except:
            pass

    def clear_cookies(self):
        self.chrome.delete_all_cookies()
