from  selenium import  webdriver

drive=webdriver.Chrome()
drive.get("http://www.baidu.com")
el=drive.find_element('id','kw')
el.send_keys('大帅逼')
drive.find_element('id','su').click()