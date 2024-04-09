import os
import time

from behave import when, then, given
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv


load_dotenv()


@given("I am on the Jira login page")
def step(context):
    context.browser.get("https://mcmbot.atlassian.net/")


@when("I enter in my username and password")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(EC.element_to_be_clickable((By.ID, "username")))
    context.browser.find_element(By.ID, "username").send_keys(os.environ["USERNAME"])
    context.browser.find_element(By.ID, "login-submit").click()
    wait.until(EC.element_to_be_clickable((By.ID, "password")))
    context.browser.find_element(By.ID, "password").send_keys(os.environ["PASSWORD"])


@when("I click the login button")
def step_impl(context):
    context.browser.find_element(By.ID, "login-submit").click()


@then("I am on logged in")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(EC.title_is("Your work - Jira"))


@given("I am logged in")
def step_impl(context):
    context.execute_steps(
        """
        given I am on the Jira login page
        when I enter in my username and password
        when I click the login button
        then I am on logged in 
    """
    )


@when("I click to log out")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[aria-label="Your profile and settings"]')
        )
    ).click()

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "logout-submit"))).click()


@then("I am logged out")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(EC.title_is("Log in to continue - Log in with Atlassian account"))
