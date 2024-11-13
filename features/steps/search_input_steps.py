from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('searching {word}')
def search_word(context, word):
    context.app.main_page.search_word(word)
    sleep(5)

@then('Verify that {word} popped up')
def verify_word(context, word):
    context.app.main_page.verify_search_word(word)