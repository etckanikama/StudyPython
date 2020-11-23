import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,text):
    # 検索対象取得
    df=pd.read_csv("./{}".format(text), encoding="shift-jis")
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.write_log("{}はいます。".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.write_log("{}はいません".format(word))
        eel.write_log("{}を追加".format(word))

        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(text),encoding="shift-jis")
    print(source)

