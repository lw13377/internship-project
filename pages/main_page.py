from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

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
    SALES_FILTER = By.ID, "Location-2"
    OUT_OF_STOCK = By.CSS_SELECTOR, "option[value='Out of stock']"
    ANNOUNCED = By.CSS_SELECTOR, "option[value='Announced']"
    STATUS_VERIFY = By.CSS_SELECTOR, "[wized='projectStatus']"
    CLICK_MARKET = By.CSS_SELECTOR, "a[href='/market-companies']"
    ADD_COMPANY = By.CSS_SELECTOR, "[class='add-company-button w-inline-block']"
    PUBLISH = By.CSS_SELECTOR, "[class='publish-button _1 w-button']"


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

    def filter_out_stock(self):
        self.click(*self.SALES_FILTER)
        self.wait_and_click(*self.OUT_OF_STOCK)

    def verify_out_of_stock_tag(self):
        sleep(10)
        product_status = self.driver.find_elements(*self.STATUS_VERIFY)
        for status in product_status:
            tag_text = status.text
            assert "Out of stock" in tag_text, f"Product missing 'Out of stock' tag: {tag_text}"

    def filter_announced(self):
        self.click(*self.SALES_FILTER)
        self.wait_and_click(*self.ANNOUNCED)

    def verify_announced(self):
        sleep(10)
        product_status = self.driver.find_elements(*self.STATUS_VERIFY)
        for status in product_status:
            tag_text = status.text
            assert "Announced" in tag_text, f"Product missing 'Announced' tag: {tag_text}"

    def market(self):
        self.wait_and_click(*self.CLICK_MARKET)

    def verify_market(self):
        expected_url = 'https://soft.reelly.io/market-companies'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def add_company(self):
        self.click(*self.ADD_COMPANY)

    def verify_add_company(self):
        expected_url = 'https://soft.reelly.io/presentation-for-the-agency'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_publish_company(self):
        self.wait_until_clickable(*self.PUBLISH)

    # def wait_until_clickable(self, *PUBLISH):
    #     self.wait.until(
    #         EC.element_to_be_clickable(*PUBLISH),
    #         message=f'Element by locator {PUBLISH} not clickable'
    #     )













