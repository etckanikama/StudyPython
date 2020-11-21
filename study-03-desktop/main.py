import eel
import time
import desktop


# フォルダ名
app_name = "html"
end_point = "index.html"
size = (700,600)
# eel.start("index.html")




time.sleep(10)
@eel.expose
def write_log_py(text):
    eel.write_log("hello")


desktop.start(app_name,end_point,size)