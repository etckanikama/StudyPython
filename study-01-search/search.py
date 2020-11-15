import csv
CSV_PATH = 'data.csv'

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# csvファイル読み込み
def read_csv_hoge(data):
    with open(CSV_PATH) as f:
        for line in csv.reader(f):
            pass
    return line

# def write_csv(data,word):
#     with open(CSV_PATH,'a') as f:
#         writer = csv.writer(f)
#         writer.writerow([','+ word])
#     return writer

## 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    array = read_csv_hoge(CSV_PATH)
    ### ここに検索ロジックを書く
    if word in array:
        print("{}が見つかりした".format(word))
    else:
        print("{}はいません".format(word))
        # w = write_csv(CSV_PATH, word)
        # with open(CSV_PATH,'a') as f:
        #     writer = csv.writer(f, lineterminator=',')
        #     writer.writerow([word])
    # a = read_csv_hoge(CSV_PATH)
    # print(a)


        
        
if __name__ == "__main__":
    search()