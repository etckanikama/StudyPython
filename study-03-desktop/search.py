import csv
CSV_PATH = 'data.csv'

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# csvファイル読み込み
def read_csv_hoge(data):
    with open(CSV_PATH, encoding="utf-8_sig") as f:
        for line in csv.reader(f):
            pass
    return line



## 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    csv_array = read_csv_hoge(CSV_PATH)
    ### ここに検索ロジックを書く
    if word in csv_array:
        print("{}が見つかりした".format(word))
    else:
        print("{}はいません".format(word))
        csv_array.append(word)
        with open(CSV_PATH,'w') as f:
            writer = csv.writer(f)
            writer.writerow(csv_array)

    # a = read_csv_hoge(CSV_PATH)
    # print(a)


        
        
if __name__ == "__main__":
    search()