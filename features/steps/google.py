from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("drivers/chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@step(u'I open BrancaStore')
def openUrl(context):
    context.driver.get("https://www.brancastore.com.ar/")
    context.driver.find_element_by_class_name("cross").click()
    context.driver.find_element_by_id("an_verification_yes").click()


@when(u'search fernet branca')
def search(context):
    hover = ActionChains(context.driver).move_to_element(context.driver.find_element_by_xpath("//nav[@id='cbp-hrmenu']//span[contains(text(),'Fernets')]"))
    hover.perform()
    context.driver.find_element_by_xpath("//nav[@id='cbp-hrmenu']//a[contains(text(),'Fernet Branca')]").click()

