import eel
import time
import search
import desktop


# フォルダ名
app_name = "html"
end_point = "index.html"
size = (700,600)
# eel.start("index.html")





# @eel.expose
# def write_log_py(text):
#     eel.write_log("hello")

@eel.expose
def kimetsu_search(word,text):
    # search.pyの関数を呼び出すための関数
    search.kimetsu_search(word,text)


desktop.start(app_name,end_point,size)