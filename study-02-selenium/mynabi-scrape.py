from base64 import a85encode
import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
import sys
# import chromedriver_binary
# Chromeを起動する関数

args = sys.argv

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

# main処理


def main():
    search_keyword = args[1]
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')

    # 検索窓に入力
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()
        # ページ終了まで繰り返し取得

    exp_name_list = []
    exp_catcopy_list = []
    exp_date_list = []


    while(True):



        # 検索結果の一番上の会社名を取得
        name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
        # キャッチコピーを取得
        catcopy_list = driver.find_elements_by_class_name("labelCondition")
        # 更新日時を取得
        date_list = driver.find_elements_by_class_name("cassetteRecruit__updateDate")

        # 1ページ分繰り返し
        for name,catcopy,date in zip(name_list,catcopy_list,date_list):
            exp_name_list.append(name.text)
            exp_catcopy_list.append(catcopy.text)
            exp_date_list.append(date.text)
            print(name.text)
            print(catcopy.text)
            print(date.text)
        


        # # 画面遷移のclassを取得
        try:
            next_url_class = driver.find_element_by_class_name("iconFont--arrowLeft")
            next_url_href = next_url_class.get_attribute("href")
            # # # 二ページ目の
            driver.get(f'{next_url_href}')
            time.sleep(5)
        except:
            print("存在しない")
            break


    




# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()