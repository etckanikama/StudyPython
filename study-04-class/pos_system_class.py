import pandas as pd

class Pos():
    def __init__(self,excel_path):
        self.df = pd.read_csv(excel_path)
        pd.set_option('display.unicode.east_asian_width',True)

    def calculate(self):
        print(self.df)

if __name__ == "__main__":
    cst = Pos("order.csv")
    print(cst.calculate())
