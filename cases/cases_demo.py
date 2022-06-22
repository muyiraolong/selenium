import sys
sys.path.append('..')
from  demo02.web_keys import Key

key= Key("Chrome")
key.open('http://www.baidu.com')
key.input('id','kw','大帅逼')
key.click('id','su')