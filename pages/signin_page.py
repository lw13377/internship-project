from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    LOG_IN = By.CSS_SELECTOR, "[wized='loginButton']"
    EMAIL = By.ID, "email-2"
    PASSWORD = By.ID, "field"


    def email(self):
        self.input_text('testforcareerist@gmail.com', *self.EMAIL)

    def password(self):
        self.input_text('testerikcareerist', *self.PASSWORD)

    def log_in(self):
        self.click(*self.LOG_IN)
