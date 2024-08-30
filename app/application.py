from pages.base_page import Page
from pages.openurl_page import UrlPage
from pages.signin_page import SignInPage
from pages.main_page import MainPage



class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.openurl_page = UrlPage(driver)
        self.signin_page = SignInPage(driver)
        self.main_page = MainPage(driver)
