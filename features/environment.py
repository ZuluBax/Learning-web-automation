from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    context.browser = webdriver.Chrome(options=options)


def after_all(context):
    context.browser.quit()
