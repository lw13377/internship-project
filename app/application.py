from pages.base_page import Page
from pages.openurl_page import UrlPage
from pages.secondary_page import SecondaryPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.signin_page import SignInPage



class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.openurl_page = UrlPage(driver)
        self.signin_page = SignInPage(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.settings_page = SettingsPage(driver)
        self.secondary_page = SecondaryPage(driver)
