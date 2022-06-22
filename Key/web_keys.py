'''
   关键词封装类：
        将常用的selenium进行二次封装
        1. 创建浏览器对象
        2. 访问url
        3. 输入
'''

from selenium import webdriver
from time import sleep


def open_browser(typeBro):
    try:
        return getattr(webdriver, typeBro)()  # 利用反射简化代码
    except Exception as e:
        print(e)
        return webdriver.chrome()


class Key:
    def __init__(self, method):
        self.drive = open_browser(method)

    def open(self, method):
        self.drive.get(method)

    # 元素定位
    def locate(self, name, value):
        return self.drive.find_element(name, value)

    def input(self, name, value, method):
        self.locate(name, value).send_keys(method)

    def click(self, name, value):
        self.locate(name, value).click()

    def sleep(self, method):
        sleep(method)

    def quit(self):
        self.drive.quit()

    def assert_text(self,name,value,expect):
        try:
            reality=self.locate(name,value).text
            assert reality ==expect,'{}不等于{}'.format(reality,expect)
            print("断言成功")
            return True
        except Exception as e:
            print(e)
            return  False