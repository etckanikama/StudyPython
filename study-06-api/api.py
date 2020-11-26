import requests
import urllib
import pprint

from requests.api import get


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)

    json_list = get_api(url)
    for num in range(len(json_list['Items'])):
        print("商品価格：{}\n 商品名：{}\n ".format(json_list['Items'][num]['Item']['itemPrice'],json_list['Items'][num]['Item']['itemName']))
    
    # print(len(json_list['Items']))
    # print(get_api(url))
    # pprint.pprint(get_api(url))


main()

