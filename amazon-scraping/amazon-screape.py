from base64 import a85encode
import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import datetime
import pandas as pd
import sys

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

    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)

        # Webサイトを開く
    driver.get("https://www.amazon.co.jp/dp/B08F725R4K/ref=zg_bs_kitchen_home_1?_encoding=UTF8&psc=1&refRID=69W2MBGRT6S8E3WYBSCH")
    time.sleep(5)

    while (True):
        # 今回はxpathを使って<span>内の要素をとってくる
        # 参考url: https://qiita.com/sf213471118/items/61014ffe06a6ebf704ea
        time.sleep(5)
        title_name = driver.find_element_by_xpath("//span[@class='a-size-large product-title-word-break']")
        # for name in title_name:
        print("商品名：{}".format(title_name.text))
        price = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-price priceBlockBuyingPriceString']") 
        print("価格：{}".format(price.text))
        deadline = driver.find_element_by_xpath("//div[@class='a-section a-spacing-mini']")
        print(deadline.text)

        # primeかどうか
        # 複数個あるときはelementsのsを忘れてはいけない
        prime_check = driver.find_elements_by_xpath("//div[@class='nav-line-1-container']")[1]
        # print(prime_check.text)
        # prime_label = False
        if prime_check.text != "今すぐ登録":
            # prime_label = True
            print("prime会員です。")
        print("prime会員ではありません")

        cur_url = driver.current_url
        front = cur_url.find("/dp")
        back =cur_url.find("/ref")
        print("ASIN番号：{}".format(cur_url[front+4:back]))

        

        break


if __name__ == "__main__":
    main()