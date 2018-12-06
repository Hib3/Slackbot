from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""オプション設定
options = Options()
options.add_argument('--headless')#ヘッドレスモードにより、裏で動かす
options.add_argument('--disable-gpu')#GPU使うようなページではオフにさせる
driver = webdriver.Chrome(options=options)
"""
driver = webdriver.Chrome("./chromedriver")
url = 'http://yume-uranai.jp/keyword.html'
words = input('スペース区切りで調べたいワードを入力してください')

driver.get(url)
sleep(1)

element = driver.find_element_by_name("keyword")
element.send_keys(words)
element.submit()#入力formの送信
sleep(1)

sleep(5)

driver.close()
