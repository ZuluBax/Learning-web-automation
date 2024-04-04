import time

from behave import when, then, given
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@when("we visit google")
def step(context):
    context.browser.get("https://www.google.com")


@then('it does have a title "Google"')
def step(context):
    assert context.browser.title == "Google"


@given("I am on the google home page")
def step_impl(context):
    context.execute_steps(
        """
   when we visit google
   then it does have a title "Google"
   """
    )
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(lambda d: context.browser.find_element(By.ID, "L2AGLb")).is_displayed()
    context.browser.find_element(By.ID, "L2AGLb").click()


@when("I search for twitter")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(lambda d: context.browser.find_element(By.ID, "APjFqb")).is_displayed()
    context.browser.find_element(By.ID, "APjFqb").send_keys("twitter")
    context.browser.find_element(By.ID, "APjFqb").send_keys(Keys.RETURN)


@then("I see twitter in the search results")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(
        lambda d: context.browser.find_element(
            By.XPATH,
            '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a',
        )
    ).is_enabled()
    result_name = context.browser.find_element(
        By.XPATH,
        '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3',
    ).text
    assert result_name == "X. It's what's happening / X"


@given("I have searched for Twitter on google")
def step_impl(context):
    context.execute_steps(
        """
       given I am on the google home page
       when I search for twitter
       then I see twitter in the search results
       """
    )


@when("I click on Twitter in the search results")
def step_impl(context):
    context.browser.find_element(
        By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'
    ).click()


@then("I am on the Twitter home page")
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    wait.until(lambda d: context.browser.title is not None)
    title = context.browser.title
    assert title == "X. It’s what’s happening / X", "actual: " + title
