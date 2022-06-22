from selenium import  webdriver

drive =webdriver.Chrome()
drive.get("http://cn.bing.com")#一定要带http/https
drive.find_element('id','sb_form_q').send_keys('我是大帅逼')#查找元素，然后输入
drive.find_element('id','su').click()#点击
# 实际，只使用find-element