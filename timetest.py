import datetime

path = "test.text"
num = 1
def datetime_write():
    now = datetime.datetime.now()
    with open(path, 'a') as f:
        print("時間:{},ページ：{}".format(now,num), file=f)

if __name__ == "__main__":
    while (num <= 10):
        datetime_write()
        num += 1

