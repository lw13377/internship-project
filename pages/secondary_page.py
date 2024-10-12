from pages.base_page import Page
from selenium.webdriver.common.by import By



class SecondaryPage(Page):
    SECONDARY_PAGE = By.XPATH , "//div[@class='div-block-28']//div[text()='Secondary']"
    NEXT_PAGE = By.CSS_SELECTOR , "[class='pagination__button w-inline-block']"
    PREVIOUS_PAGE = By.CSS_SELECTOR , "[class='pagination__button']"

    def click_on_secondary_left(self):
        self.click(*self.SECONDARY_PAGE)

    def verify_secondary_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://soft.reelly.io/secondary-listings"
        assert self.driver.current_url == expected_url, f"expected {expected_url}, but got {self.driver.current_url}"

    def next_page(self):
        self.click(*self.NEXT_PAGE)

    def prev_page(self):
        self.click(*self.PREVIOUS_PAGE)


