from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Filter by sale status to out of stock')
def filter_out_stock(context):
    context.app.main_page.filter_out_stock()

@then('Verify each product contains the Out of Stocks tag')
def verify_product_out_stock(context):
    context.app.main_page.verify_out_of_stock_tag()