import eel


@eel.expose
def python_function(val):
    print(val + " from Javascript")

# フォルダ名
eel.init("html")
eel.start("index.html")