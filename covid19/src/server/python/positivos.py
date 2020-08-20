import pandas as pd 
import re
import datetime

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # production
    # return f"{day}{month}{year}"
    # dev
    return f"{day}{month}{year}"


def read_csv():
    date = get_date()
    name = f"./data/positivos{date}data.csv"
    data = pd.read_csv(name, encoding = 'latin-1')
    # data["FECHA_RESULTADO"] = re.split("[\d][\d][\d][\d]", data["FECHA_RESULTADO"])
    # pd.to_datetime(data["FECHA_RESULTADO"])
    # print(data.dtypes)
    # print(data["FECHA_RESULTADO"])
    # departamentos completados
    data_per_days_department = data.groupby('DEPARTAMENTO')['FECHA_RESULTADO'].count()

    # data_per_days_province = data.groupby(['DEPARTAMENTO','PROVINCIA'])['FECHA_RESULTADO'].count()
    departments = data.filter(items=['DEPARTAMENTO']).groupby('DEPARTAMENTO')['DEPARTAMENTO'].count()
    provinces = data.filter(items=['PROVINCIA', 'DEPARTAMENTO']).groupby('PROVINCIA')['DEPARTAMENTO'].count().head(40)
    distritos = data.filter(items=['DISTRITO', 'PROVINCIA']).groupby('DISTRITO')['PROVINCIA'].count().head(20)
    # print(departments)
    positives_per_day = data.filter(items=['DEPARTAMENTO', 'FECHA_RESULTADO']).groupby('FECHA_RESULTADO')['DEPARTAMENTO'].count()

    departments_per_day = data.filter(items=['DEPARTAMENTO', 'FECHA_RESULTADO']).groupby(['DEPARTAMENTO','FECHA_RESULTADO'])['DEPARTAMENTO'].count().head(40)
    print(departments_per_day)
    # for d in data:
    #     for dep in data["DEPARTAMENTO"]:
    #         if dep == "JUNIN":
    #             print(dep)
        # print(d)
    # print(data.DEPARTAMENTO)

if __name__ == "__main__":
    read_csv()