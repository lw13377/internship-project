from pages.base_page import Page


class UrlPage(Page):


    def open_main(self):
        self.open_url('https://soft.reelly.io/')


    def open_signin(self):
        self.open_url('https://soft.reelly.io/sign-in')