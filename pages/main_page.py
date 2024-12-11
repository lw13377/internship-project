from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    OFF_PLAN = (By.CSS_SELECTOR, "[class='menu-text-link-leaderboard w--current']")
    NEXT_PAGE = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "[wized='previousPageProperties']")
    VERIFY_OFFPLAN = (By.XPATH, "//a[contains(text(), 'Off-plan')]")
    SEARCH_INPUT = (By.ID, "searchInput")
    TEXT_VERIFY = By.CSS_SELECTOR, "[class='project-name']"
    FILTER = By.CSS_SELECTOR, "[class='filter-button w-inline-block']"
    MIN_RANGE = By.CSS_SELECTOR, "[wized='unitPriceFromFilter']"
    MAX_RANGE = By.CSS_SELECTOR, "[wized='unitPriceToFilter']"
    APPLY_FILTER = By.CSS_SELECTOR, "[wized='applyFilterButton']"
    PRICE = By.CSS_SELECTOR, "[class='price-class']"


    def off_plan(self):
        self.click(*self.OFF_PLAN)

    def next_page(self):
        self.wait_and_click(*self.NEXT_PAGE)

    def previous_page(self):
        self.wait_and_click(*self.PREVIOUS_PAGE)

    def verify_offplan_opened(self):
        self.wait_for_element_appear(*self.VERIFY_OFFPLAN)

    def search_word(self, word):
        self.input_text(word, *self.SEARCH_INPUT)

    def verify_search_word(self, word):
        self.verify_partial_text(word,*self.TEXT_VERIFY)

    def filter_range(self):
        self.click(*self.FILTER)
        self.input_text(1200000, *self.MIN_RANGE)
        self.input_text(2000000, *self.MAX_RANGE)
        self.wait_and_click(*self.APPLY_FILTER)

    def verify_price_range(self):
        price_elements = self.find_elements(*self.PRICE)

        prices = [int(price.text.replace(',', '').replace(' AED', '').strip()) for price in price_elements]

        for price in prices:
            assert 1200000 <= price <= 2000000, f"Price {price} is out of range!"







