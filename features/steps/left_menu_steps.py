from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_signin(context):
    context.app.openurl_page.open_signin()


@given('Type in Email')
def type_in_email(context):
    context.app.signin_page.email()


@then('Type in Password')
def type_in_email(context):
    context.app.signin_page.password()



@then('Log in to the page')
def log_in(context):
    context.app.signin_page.log_in()


@then('Click on off plan option at the left side menu')
def open_offplan(context):
    context.app.main_page.off_plan()


@when('Verify the right page opens')
def verify_offplan(context):
    context.app.main_page.verify_offplan_opened()


@then('Go to the final page using the pagination button')
def click_on_next_page(context):
    for i in range(51):
        context.app.main_page.next_page()


@then('Go back to the first page using the pagination button')
def click_on_prev_page(context):
    for i in range(51):
        context.app.main_page.previous_page()