import time

from behave import when, then
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@when('we visit google')
def step(context):
   context.browser.get('https://www.google.com')

@then('it should have a title "Google"')
def step(context):
   assert context.browser.title == "Google"
   wait = WebDriverWait(context.browser, timeout=10)

   wait.until(lambda d: context.browser.find_element(By.ID, 'L2AGLb')).is_displayed()
   context.browser.find_element(By.ID, 'L2AGLb').click()

   wait.until(lambda d: context.browser.find_element(By.ID, 'APjFqb')).is_displayed()
   context.browser.find_element(By.ID, 'APjFqb').send_keys('twitter')
   context.browser.find_element(By.ID, 'APjFqb').send_keys(Keys.RETURN)

   wait.until(lambda d: context.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')).is_enabled()
   context.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a').click()

   assert context.browser.title == "X. It’s what’s happening / X"