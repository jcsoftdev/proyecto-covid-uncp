import pandas as pd 
import datetime

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return f"{day}{month}{year}"


def read_csv():
    date = get_date()
    name = f"./data/positivos{date}data.csv"
    data = pd.read_csv(name, encoding = 'latin-1')
    for d in data:
        for dep in data["DEPARTAMENTO"]:
            if dep == "JUNIN":
                print(dep)
        # print(d)
    # print(data.DEPARTAMENTO)

if __name__ == "__main__":
    read_csv()