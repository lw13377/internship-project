from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingsPage(Page):
    SETTINGS = By.XPATH, "//div[text()='Settings']"
    SETTINGS_ELEMENTS = By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']"
    CONNECT_THE_COMPANY = By.XPATH, "//div[text()='Connect the company']"

    def settings(self):
        self.click(*self.SETTINGS)

    def verify_settings_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://soft.reelly.io/settings"
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_settings_elements(self):
        elements = self.driver.find_elements(*self.SETTINGS_ELEMENTS)
        assert len(elements) == 12, f'Expected 12 but got {len(elements)}'

    def connect_the_company(self):
        self.wait_until_clickable(*self.CONNECT_THE_COMPANY)

