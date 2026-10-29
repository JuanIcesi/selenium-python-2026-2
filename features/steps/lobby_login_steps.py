from behave import given, when, then
from selenium import webdriver
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage
from selenium.webdriver.common.by import By

@given('El usuario se encuentra en la página de login')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://lobby-global.vercel.app/")
    context.lobby_login_page = LobbyLoginPage(context.driver)

@when('El usuario ingresa con el nombre "{username}"')
def step_when_user_logs_in(context, username):
    context.lobby_login_page.login(username)
    context.lobby_dashboard_page = LobbyDashboardPage(context.driver)

@then('El nombre del usuario "{username}" aparece en el dashboard')
def step_then_user_login(context, username):
    assert context.lobby_dashboard_page.find_username(username) is True

@then('El mensaje de error "{message}" aparece en el login')
def step_then_error_message(context, message):
    error_message = context.driver.find_element(By.CLASS_NAME, "error-message").text
    assert error_message == message

@when('El usuario ingresa con un nombre único')
def step_when_user_logs_in_with_unique_name(context):
    import uuid

    context.username = f"User{uuid.uuid4().hex[:8]}"
    context.lobby_login_page.login(context.username)
    context.lobby_dashboard_page = LobbyDashboardPage(context.driver)

@then('El nombre único del usuario aparece en el dashboard')
def step_then_unique_user_login(context):
    assert context.lobby_dashboard_page.find_username(context.username) is True
