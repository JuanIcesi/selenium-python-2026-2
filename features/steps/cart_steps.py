from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

@given("I am logged in on the inventory page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(context.driver)
    login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)

@when('I add the product "{product_name}" to the cart')
def step_impl(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)

@then("I should see 1 item in the cart")
def step_impl(context):
    time.sleep(1)
    cart_count = context.inventory_page.get_cart_count()
    assert cart_count == "1"
    context.driver.quit()
