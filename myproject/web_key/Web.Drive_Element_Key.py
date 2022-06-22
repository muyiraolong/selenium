#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : XueWei He
# @Time     : 2022/6/4 20:38
# @File     : Web.Drive_Element_Key.py
# @Project  : pythonproject


from Web_Drive_Element_Loca import Web_Drive_Loca
from selenium.webdriver.common.keys import Keys


class Web_Drive_Key(Web_Drive_Loca):
    def __init__(self, driver):
        super().__init__(driver)
