from base64 import a85encode
import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import datetime
import pandas as pd
import sys

# データ格納配列
custom_name_list = []
custom_url_list = []
detail_name = []
detail_price = []
detail_deadline = []
detail_ansi = []



def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)


def main():

    FIST_URL = "https://www.amazon.co.jp/gp/bestsellers/kitchen/ref=zg_bs_kitchen_home_all?"
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)

        # Webサイトを開く
    driver.get(FIST_URL)
    time.sleep(5)

    while (True):
        


        # 商品名
        custom_name_get = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']")
        for name in custom_name_get:
            custom_name_list.append(name.text)
            # print(name.text)
        print(len(custom_name_list))
        
        # 商品url
        url_xpath = driver.find_elements_by_xpath("//span[@class='aok-inline-block zg-item']/a[@class='a-link-normal']")
        for i in range(len(url_xpath)):
            detail_url = url_xpath[i].get_attribute("href")
            detail_info(driver,detail_url)
            time.sleep(5)
            # これだけ
            driver.implicitly_wait(10)
            # 仮説：以下で再度urlを更新した際にforの外でとったurl_xpathの情報がなかったことになってしまうため
            driver.get(FIST_URL)
            time.sleep(10)
            custom_url_list.append(detail_url)
            # print(url_xpath[i].get_attribute("href"))
        # print(len(custom_url_list))




        try:
            element = driver.find_element_by_class_name("a-last")
            aTag = element.find_element_by_tag_name("a")
            next_url = aTag.get_attribute("href")
            driver.get(f'{next_url}')
            time.sleep(5)

        except:
            print("商品ページはこれ以上存在しません")
            break


    colum = ['商品名','商品url','価格','ANSI番号']
    # df作成
    df = pd.DataFrame(list(zip(custom_name_list,custom_url_list,detail_price,detail_ansi)),columns=colum)
    df.to_csv("custom_info.csv",encoding="utf-8_sig")
    
#　詳細画面 
def detail_info(driver,detail_url):

        # ☆おそらくここgetがメソッドとして認識されていない
        driver.get(f'{detail_url}')
        time.sleep(5)
        title_name = driver.find_element_by_xpath("//span[@class='a-size-large product-title-word-break']")
        # for name in title_name:
        print("商品名：{}".format(title_name.text))
        detail_name.append(title_name.text)
        
        price = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-price priceBlockBuyingPriceString']") 
        print("価格：{}".format(price.text))
        detail_price.append(price.text)
        
        deadline = driver.find_element_by_xpath("//div[@class='a-section a-spacing-mini']")
        print(deadline.text)
        detail_deadline.append(deadline.text)

        # primeかどうか
        # 複数個あるときはelementsのsを忘れてはいけない
        prime_check = driver.find_elements_by_xpath("//div[@class='nav-line-1-container']")[1]

        if prime_check.text != "今すぐ登録":
            # prime_label = True
            print("prime会員です。")
        print("prime会員ではありません")

        cur_url = driver.current_url
        front = cur_url.find("/dp")
        back =cur_url.find("/ref")
        print("ASIN番号：{}".format(cur_url[front+4:back]))
        detail_ansi.append(cur_url[front+4:back])
        
        time.sleep(5)





if __name__ == "__main__":
    main()