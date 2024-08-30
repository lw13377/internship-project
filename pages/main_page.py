from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    OFF_PLAN = (By.CSS_SELECTOR, "[class='_1-link-menu w-inline-block w--current']")
    NEXT_PAGE = (By.CSS_SELECTOR, "[class='pagination__button w-inline-block']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "[class='pagination__button']")
    VERIFY_OFFPLAN = (By.XPATH, "//a[contains(text(), 'Off-plan')]")


    def off_plan(self):
        self.click(*self.OFF_PLAN)

    def next_page(self):
        self.click(*self.NEXT_PAGE)

    def previous_page(self):
        self.click(*self.PREVIOUS_PAGE)

    def verify_offplan_opened(self):
        self.wait_for_element_appear(*self.VERIFY_OFFPLAN)