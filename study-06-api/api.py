import requests
import urllib
import pprint
import pandas as pd

from requests.api import get


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    genreid = "566403" #おそらくゲームかnintendoについてのgenreid
    search_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(keyword)
    product_url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={}&applicationId=1019079537947262807".format(keyword)

    ranking_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&genreId={}&applicationId=1019079537947262807".format(genreid)

    """課題1:最初の一ページ目にある商品名と価格を表示
    json_list = get_api(search_url)
    for data_num in range(len(json_list['Items'])):
        print("商品価格：{}\n 商品名：{}\n ".format(json_list['Items'][data_num]['Item']['itemPrice'],json_list['Items'][data_num]['Item']['itemName']))
    """
    # print(len(json_list['Items']))
    # print(get_api(url))
    # pprint.pprint(get_api(url))

    """課題2：任意の商品名を指定してあげて、それに該当する最安値、最高値を表示
    product_json_list = get_api(product_url)
    size = int(product_json_list['hits'])
    search_name = "バンダイ 鬼滅の刃ディフォルメシールウエハース 1枚"
    for num in range(size):
        if product_json_list['Products'][num]['Product']['productName'] == search_name:

            print("最安値：{}円".format(product_json_list['Products'][num]['Product']['minPrice']))
            print("最高値：{}円".format(product_json_list['Products'][num]['Product']['maxPrice']))
    """
    # 課題3：任意のジャンルIDからランキング一覧（順位、商品名、値段、商品url）
    ranking_json_list = get_api(ranking_url)
    size = len(ranking_json_list['Items'])
    # print(size)
    # リストをそれぞれ用意する
    id_list = []
    rank_list = []
    item_name_list = []
    item_price_list = []
    item_url_list = []
    


    for num in range(size):
        id_list.append(ranking_json_list['Items'][num]['Item']['genreId'])
        rank_list.append(ranking_json_list['Items'][num]['Item']['rank'])
        item_name_list.append(ranking_json_list['Items'][num]['Item']['itemName'])
        item_price_list.append(ranking_json_list['Items'][num]['Item']['itemPrice'])
        item_url_list.append(ranking_json_list['Items'][num]['Item']['itemUrl'])
        # print("ID:{} 順位：{} 商品名：{} 値段：{} 商品URL:{}".format(
        #     ranking_json_list['Items'][num]['Item']['genreId'],
        #     ranking_json_list['Items'][num]['Item']['rank'],
        #     ranking_json_list['Items'][num]['Item']['itemName'],
        #     ranking_json_list['Items'][num]['Item']['itemPrice'],
        #     ranking_json_list['Items'][num]['Item']['itemUrl'],
        #     ))
    colum = ['ID','順位','商品名','値段','商品URL']

    # df作成
    df = pd.DataFrame(list(zip(id_list,rank_list,item_name_list,item_price_list,item_url_list)),columns=colum)
    # csv出力
    df.to_csv("ranking.csv",encoding="utf-8_sig")
main()

