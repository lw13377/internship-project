from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Open Secondary Page from the left")
def secondary_steps(context):
    context.app.secondary_page.click_on_secondary_left()

@when("Verify that Secondary Page Opened")
def verify_secondary_opened(context):
    context.app.secondary_page.verify_secondary_url()
    sleep(2)

@then("Click on Next Page to the end")
def next_page(context):
    for i in range (98):
        context.app.secondary_page.next_page()

@then("Click on Previous page to the end")
def previous_page(context):
    for i in range (98):
        context.app.secondary_page.prev_page()




