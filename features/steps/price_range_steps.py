from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Filter the range from 120k-200k")
def price_range(context):
    context.app.main_page.filter_range()

@then("Verify all the results have the correct price range")
def verify_price(context):
    context.app.main_page.verify_price_range()

