from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Click on settings option")
def click_settings(context):
    context.app.settings_page.settings()

@when("Verify the settings page opens")
def verify_settings_opened(context):
    context.app.settings_page.verify_settings_url()

@then("Verify there are 12 options for the settings")
def verify_12_options(context):
    context.app.settings_page.verify_settings_elements()

@then("Verify that connect the company button is available")
def verify_connect_button(context):
    context.app.settings_page.connect_the_company()
