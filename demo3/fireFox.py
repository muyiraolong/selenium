from lib2to3.pgen2 import driver
from selenium import webdriver

try:
    driver = webdriver.Firefox()
except Exception as e:
    print(e)
driver.get("https://cn.bing.com")
driver.find_element("id", "sb_form_q").send_keys("我是大帅逼")
driver.find_element(
    "id", "sb_form_go").click()
