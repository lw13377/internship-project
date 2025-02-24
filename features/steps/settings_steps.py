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

@then('Click on Verification')
def click_verification(context):
    context.app.settings_page.verification()

@then('Verify verification page opens')
def verify_verification(context):
    context.app.settings_page.verify_verification()

@then('Verify upload image and next step')
def verify_upload_image(context):
    context.app.settings_page.verify_photo_next_step()
