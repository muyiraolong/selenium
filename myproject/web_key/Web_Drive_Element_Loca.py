from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


def open_browser(drive):
    try:
        return getattr(webdriver, drive)()
    except Exception as e:
        print("浏览器启动错误,错误是", e)
        return webdriver.Chrome()


class Web_Drive_Loca:

    def __init__(self, driver):
        self.driver = open_browser(driver)

    def print_name(self):
        print(self.driver.name)

    def open(self, url):
        self.driver.get(url)

    def set_size(self, x=0, y=0):
        if x == 0 and y == 0:
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(eval(x), eval(y))

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def loca(self, method, value):
        try:
            return self.driver.find_element(method, value)
        except NoSuchElementException as e:
            print(e)

    def print_attribute(self, method, value, attribute):
        attribute_info = self.loca(method, value).get_attribute(attribute)
        print(attribute_info)

    def print_text(self, method, value):
        text_info = self.loca(method, value).text
        print(text_info)

    def input(self, method, value, txt):
        self.loca(method, value).send_keys(txt)

    def click_element(self, method, value):
        self.loca(method, value).click()

    def print_size(self, method, value):
        size = self.loca(method, value).size
        for k, v in size.items():
            print(f'{k} : {"{:.2f}".format(v)}')

    def refresh(self):
        self.driver.refresh()

    def clear(self, method, value):
        self.loca(method, value).clear()

    def submit(self, method, value):
        self.loca(method, value).submit()

    def sleep(self, time):
        # 强制睡眠
        sleep(eval(time))

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(eval(time))

    def web_drive_wait(self, time):
        return WebDriverWait(self.driver, 5)

    def web_drive_wait_loca_element(self,method,value):
        return ec.presence_of_element_located(getattr(By,method),value)

    def web_drive_wait_find_element(self,time,method,value):
        return self.web_drive_wait(time).until(self.web_drive_wait_loca_element(method,value))

    def web_drive_wait_input(self,time,method,value,info):
        self.web_drive_wait_find_element(time,method,value).send_keys(txt)

    def close(self):
        '''关闭当前页面'''
        self.driver.close()

    def quit(self):
        '''退出浏览器'''
        self.driver.quit()

    def assert_text(self, method, value, expectation):
        try:
            reality = self.loca(method, value).text
            assert reality == expectation, '{}不等于{}'.format(reality, expectation)
            print("断言成功")
            return True
        except Exception as e:
            print(f"断言失败,错误为:{e}")
            return False
