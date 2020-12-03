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
    # データ格納配列
    custom_name_list = []
    custom_url_list = []

    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)

        # Webサイトを開く
    driver.get("https://www.amazon.co.jp/gp/bestsellers/kitchen/ref=zg_bs_kitchen_home_all?")
    time.sleep(5)

    while (True):

        # 商品URLを取得
        # url_xpath = driver.find_elements_by_xpath("//div[@class='a-row']/a[@class='a-link-normal a-text-normal']")
        # for i in range(len(url_xpath)):
        #     custom_url_list.append(url_xpath[i].get_attribute("href"))
        #     # print(url_xpath[i].get_attribute("href"))
        # print(len(custom_url_list))

        url_xpath = driver.find_elements_by_xpath("//span[@class='aok-inline-block zg-item']/a[@class='a-link-normal']")
        for i in range(len(url_xpath)):
            custom_url_list.append(url_xpath[i].get_attribute("href"))
            # print(url_xpath[i].get_attribute("href"))
        print(len(custom_url_list))
        



        custom_name_get = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']")
        #　商品名を取得してくる
        for name in custom_name_get:
            custom_name_list.append(name.text)
            # print(name.text)
        print(len(custom_name_list))




        try:
            element = driver.find_element_by_class_name("a-last")
            aTag = element.find_element_by_tag_name("a")
            next_url = aTag.get_attribute("href")
            driver.get(f'{next_url}')
            time.sleep(5)

        except:
            print("商品ページはこれ以上存在しません")
            break
    colum = ['商品名','商品url']
    # df作成
    df = pd.DataFrame(list(zip(custom_name_list,custom_url_list)),columns=colum)
    df.to_csv("custom_info.csv",encoding="utf-8_sig")




if __name__ == "__main__":
    main()