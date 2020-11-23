import eel
import time
import search
import desktop


# フォルダ名
app_name = "html"
end_point = "index.html"
size = (700,600)
# eel.start("index.html")




time.sleep(2)
# @eel.expose
# def write_log_py(text):
#     eel.write_log("hello")

@eel.expose
def kimetu_search(word):
    # search.pyの関数を呼び出すための関数
    search.kimetu_search(word)


desktop.start(app_name,end_point,size)