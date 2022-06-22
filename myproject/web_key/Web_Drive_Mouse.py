#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : XueWei He
# @Time     : 2022/6/4 20:28
# @File     : Web_Drive_Mouse.py
# @Project  : pythonproject

from selenium.webdriver.common.action_chains import ActionChains
from Web_Drive_Element_Loca import Web_Drive_Loca


class Web_Drive_Mouse(Web_Drive_Loca):
    def __init__(self, driver):
        super().__init__(self, driver)

    def left_click(self,method,value):
        '''鼠标左击'''
        left=self.loca(method,value)
        ActionChains(self.driver).click(left).perform()

    def context_click(self,method,value):
        right = self.loca(method, value)
        ActionChains(self.driver).context_click(right).perform()

    def double_click(self,method,value):
        double = self.loca(method, value)
        ActionChains(self.driver).context_click(double).perform()

    def drag_and_drop(self,element_method,element_value,target_method,target_value):
        element = self.loca(element_method, element_value)
        target = self.loca(target_method,target_value)
        ActionChains(self.driver).drag_and_drop(element,target).perform()

    def move_to_element(self,method,value):
        element=self.loca(method, value)
        ActionChains(self.driver).move_to_element(element).perform()
