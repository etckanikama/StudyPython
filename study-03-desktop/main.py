import eel
import time

# フォルダ名
eel.init("html")
eel.start("index.html")




time.sleep(10)
@eel.expose
def write_log_py(text):
    eel.write_log("hello")


eel.start("sample.html")