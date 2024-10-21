from pages.base_page import Page
from selenium.webdriver.common.by import By



class SecondaryPage(Page):
    SECONDARY_PAGE = By.XPATH , "//div[@class='div-block-28']//div[text()='Secondary']"
    NEXT_PAGE = By.CSS_SELECTOR , "[class='pagination__button w-inline-block']"
    PREVIOUS_PAGE = By.CSS_SELECTOR , "[class='pagination__button']"
    TOTAL_PAGE = By.CSS_SELECTOR , "[wized='totalPageProperties']"
    CURRENT_PAGE = By.CSS_SELECTOR , "[wized='currentPageProperties']"

    def click_on_secondary_left(self):
        self.click(*self.SECONDARY_PAGE)

    def verify_secondary_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://soft.reelly.io/secondary-listings"
        assert actual_url == expected_url, f"expected {expected_url}, but got {actual_url}"

    def next_page(self):
        total_page = int(self.find_element(*self.TOTAL_PAGE).text)
        while True:
            current_page = int(self.find_element(*self.CURRENT_PAGE).text)
            if current_page >= total_page:
                break
            self.wait_and_click(*self.NEXT_PAGE)

    def prev_page(self):
        while True:
            current_page = int(self.find_element(*self.CURRENT_PAGE).text)
            if current_page <= 1:
                break
            self.wait_and_click(*self.PREVIOUS_PAGE)



