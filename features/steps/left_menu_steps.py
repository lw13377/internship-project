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
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        context.app.main_page.next_page()


@then('Go back to the first page using the pagination button')
def click_on_prev_page(context):
    for i in range(51):
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        context.app.main_page.previous_page()

@then('Filter by sale status of “Announced”.')
def filter_announced(context):
    context.app.main_page.filter_announced()


@then('Verify each product contains the Announced tag.')
def verify_announced(context):
    context.app.main_page.verify_announced()


@when('Click on market')
def click_market(context):
    context.app.main_page.market()

@then('Verify the market page opens.')
def verify_market(context):
    context.app.main_page.verify_market()

@then('Click on “Add Company” button.')
def click_add_company(context):
    context.app.main_page.add_company()

@then('Verify the right page opens.')
def verify_add_company(context):
    context.app.main_page.verify_add_company()

@when('Verify the button “Publish my company” is available.')
def verify_publish_company(context):
    context.app.main_page.verify_publish_company()

@then('Scroll down and click on the button “View Page Template”')
def view_template(context):
    context.app.main_page.view_template()
@then('Verify the button “Send my CV” button is available.')
def send_cv(context):
    context.app.main_page.verify_send_cv()

@when('Filter by sale status to presale')
def filter_presale(context):
    context.app.main_page.filter_presale()

@then('Verify each product contains the presale tag')
def verify_presale(context):
    context.app.main_page.verify_presale_tag()




