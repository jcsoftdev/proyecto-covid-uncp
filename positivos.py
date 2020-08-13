import pandas as pd 
import datetime

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return f"{day}{month}{year}"


def read_csv():
    date = get_date()
    name = f"./positivos{date}data.csv"
    pd.read_csv(name, encoding = 'latin-1')

if __name__ == "__main__":
    read_csv()