import pandas as pd 
import re
import datetime
import os
import json

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
    name = f"{os.getcwd()}/data/positivos{date}data.csv"
    df = pd.read_csv(name, encoding = 'latin-1')
    # data["FECHA_RESULTADO"] = re.split("[\d][\d][\d][\d]", data["FECHA_RESULTADO"])
    # pd.to_datetime(data["FECHA_RESULTADO"])
    # print(df.dtypes)
    # print(data["FECHA_RESULTADO"])
    # departamentos completados

    df['CANTIDAD'] = 1


    df_departments = df.groupby(['DEPARTAMENTO','PROVINCIA','DISTRITO'])[['CANTIDAD']].sum()

    print(df_departments)

    # df = df(['DEPARTAMENTO', 'PROVINCIA'])
    # print(df)
    # result = df.to_json(orient="index")
    # parsed = json.loads(result)
    # json.dumps(parsed, indent=4)
    # print(json.dumps(parsed, indent=4))







    data_per_days_department = df.groupby('DEPARTAMENTO')['FECHA_RESULTADO'].count()

    # data_per_days_province = df.groupby(['DEPARTAMENTO','PROVINCIA'])['FECHA_RESULTADO'].count()
    departments = df.filter(items=['DEPARTAMENTO']).groupby('DEPARTAMENTO')['DEPARTAMENTO'].count()


    provinces = df.filter(items=['PROVINCIA', 'DEPARTAMENTO']).groupby(['DEPARTAMENTO','PROVINCIA'])['DEPARTAMENTO'].count()
    # print(provinces)
    # provinces.columns = ['POSITIVOS']
    # provinces.rename(columns={'DEPARTAMENTO':'POSITIVOS'}, inplace=True)


    distritos = df.filter(items=['DISTRITO', 'PROVINCIA']).groupby('DISTRITO')['PROVINCIA'].count()
    # print(departments)
    positives_per_day = df.filter(items=['DEPARTAMENTO', 'FECHA_RESULTADO']).groupby('FECHA_RESULTADO')['DEPARTAMENTO'].count()

    departments_per_day = df.filter(items=['DEPARTAMENTO', 'FECHA_RESULTADO']).groupby(['DEPARTAMENTO','FECHA_RESULTADO'])['DEPARTAMENTO'].count()
    # print(departments_per_day)

    # result = provinces.to_json(orient="index")
    # parsed = json.loads(result)
    # json.dumps(parsed, indent=4)
    # print(json.dumps(parsed, indent=4))
    # departments.to_json(f'{os.getcwd()}/src/server/positivos_departments.json')
    # provinces.to_json(f'{os.getcwd()}/src/server/positivos_provinces.json')
    # distritos.to_json(f'{os.getcwd()}/src/server/positivos_distritos.json')
    # provinces.to_json(f'{os.getcwd()}/src/server/positivos_departments_per_day.json')
    # for d in data:
    #     for dep in data["DEPARTAMENTO"]:
    #         if dep == "JUNIN":
    #             print(dep)
        # print(d)
    # print(df.DEPARTAMENTO)
    # return parsed

if __name__ == "__main__":
    read_csv()
