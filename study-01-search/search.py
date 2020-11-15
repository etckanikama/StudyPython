### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    sample = read_csv_hoge('data.csv')
    for item in sample:
        source.append(item)

    ### ここに検索ロジックを書く
    if word in source:
      print("{}が見つかりした".format(word))
    else:
      print("{}はいません".format(word))
      source.append(word)
    # print(source)




# csvファイル読み込み
def read_csv_hoge(data):
    size=0
    with open('data.csv') as f:
        for line in csv.reader(f):
            size = len(line)
    return line

        
        
if __name__ == "__main__":
    search()