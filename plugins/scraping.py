from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#オプション設定
options = Options()
options.add_argument('--headless')#ヘッドレスモードにより、裏で動かす
options.add_argument('--disable-gpu')#GPU使うようなページではオフにさせる(現状必須？)
driver = webdriver.Chrome("./chromedriver",chrome_options=options)#seleniumのドライバーはこのようにして設定可能

def sel():#完成

    words = input('スペース区切りで調べたいワードを入力してください:')
    driver.get("http://yume-uranai.jp/keyword.html")
    #sleep(1)

    element = driver.find_element_by_name("keyword")
    element.send_keys(words)
    element.submit()#入力formの送信
    #sleep(1)
    html = driver.page_source
    #sleep(5)

    #print(html)
    driver.close()
    return(html)

def scraping():#未完成
    html = sel()#seleniumの起動、htmlの取得
    soup = BeautifulSoup(html,'html.parser')
    raw_title = soup.find_all("strong",style="color:#C84B00;font-size: 16px;")
    raw_contents = soup.find_all("div",style="font-size: 14px;background-color: #ffcc70;border: thin solid #c36a2e;margin: 10px;padding: 10px;")

    #print(raw_title)
    #titleのデータをタグ付きのまま取得してしまったので、中身を取り出す
    title=[i.text for i in raw_title]
    contents =[i.text.strip() for i in raw_contents]#/nも消す

    print(title)
    print(contents)
scraping()
