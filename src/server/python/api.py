import pandas as pd
import re
import datetime
import os
import json
import sys
import numpy

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # production
    # return f"{day}{month}{year}"
    # dev
    return f"{day}{month}{year}"


def get_dataframe():
    date = get_date()
    name = f"{os.getcwd()}/data/positivos{date}data.csv"
    df = pd.read_csv(name, encoding='latin-1')
    df['CANTIDAD'] = 1
    return df




def get_positives(df, index):
    df_departments = df.groupby([index])[
        ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)
    result = df_departments.to_json(orient="table")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)
    
def df_to_dict_b(df):
    if df.ndim == 1:
        return df.to_dict()

    ret = {}
    for key in df.index.get_level_values(0):
        sub_df = df.xs(key)
        ret[key] = df_to_dict_b(sub_df)
    return ret
    

def get_province_distr_back(df):
    # print(df[['PROVINCIA', 'DISTRITO']])
    newDF = df[['PROVINCIA', 'DISTRITO','CANTIDAD']].groupby(["PROVINCIA", "DISTRITO"])[
        ['CANTIDAD','PROVINCIA']].sum().sort_values(by=['CANTIDAD'],ascending=False)
    data = df_to_dict(newDF)
    r = json.dumps(data,  indent=4)
    loaded_r = json.loads(r)
    # json.dumps(parsed, indent=4)
    return r 










def dep_prov_to_dict(df, newDF):
    if newDF.ndim == 1:
        return newDF.to_dict()
    myDF = df[["DEPARTAMENTO","CANTIDAD"]].groupby(["DEPARTAMENTO"])[['CANTIDAD']].sum()
    ret = {"department":[]}
    departments = []
    for id_dep, departamento in enumerate(newDF.index.get_level_values(0)):
        if {departamento:0, f"{departamento}_provincias":{}} not in (ret["department"]):
            # ret["department"].append({departamento:{}})
            ret["department"].append({departamento:0, f"{departamento}_provincias":{}})
            # ret["department"].append({departamento:int(newDF["CANTIDAD"][id_dep]),f"{departamento}_provincias":{}})
            departments.append(departamento)

    for departamento in (newDF.index.get_level_values(0)):
      
        sub_df_provincias = newDF.xs(departamento)
        # print('=======================')
        array_provincias = []

        for id_provincia, provincia in enumerate(sub_df_provincias.index.get_level_values(0)):
            
            array_provincias.append({provincia: int(sub_df_provincias["CANTIDAD"][id_provincia])})
            for id_dep, dep_item in enumerate(departments):
                # print(provincia)
                if dep_item == departamento:
                    
                    ret["department"][id_dep][departamento] = int(myDF["CANTIDAD"][id_dep])
                    ret["department"][id_dep][f"{dep_item}_provincias"] = array_provincias
                    break
    # ret = json.dumps(ret,  indent=4)
    # loaded_r = json.loads(ret)
    # print(json.dumps(ret,  indent=4))
    return json.dumps(ret,  indent=4)
    # return ret

def get_department_province(df):
    # print(df[['PROVINCIA', 'DISTRITO']])
    newDF = df[["DEPARTAMENTO", "PROVINCIA",'CANTIDAD']].groupby(["DEPARTAMENTO", "PROVINCIA"])[
        ['CANTIDAD','PROVINCIA']].sum()
    data = {
        
    }
    return dep_prov_to_dict(df, newDF)

def get_provinces(df):
    new_df = df[['PROVINCIA','CANTIDAD']].groupby(["PROVINCIA"])[
        ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)

    for item in new_df.index.get_level_values(0):
        print(item)
    return new_df

def get_provinces_lat_lng(df):
    

if __name__ == "__main__":
    df = get_dataframe()
    # api = Api()
    # get_department_province(df)
    # print(get_department_province(df))


    # print(get_provinces(df))
    get_provinces(df)

    # print(get_positives(df, sys.argv[1]))
