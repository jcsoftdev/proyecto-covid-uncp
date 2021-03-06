import pandas as pd
import re
import datetime
import os
import json
import sys
import numpy as np
import requests
# from dotenv import load_dotenv
import matplotlib.pyplot as plt
plt.style.use('bmh')

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


LOCATION = {'LIMA': {'lat': -12.0463731, 'lng': -77.042754}, 'EN INVESTIGACIÓN': {'lat': -12.0489682, 'lng': -77.04645649999999}, 'AREQUIPA': {'lat': -16.4090474, 'lng': -71.53745099999999}, 'CALLAO': {'lat': -12.0508491, 'lng': -77.1259843}, 'TRUJILLO': {'lat': -8.106042799999999, 'lng': -79.0329727}, 'CHICLAYO': {'lat': -6.7700798, 'lng': -79.8549907}, 'PIURA': {'lat': -5.1782884, 'lng': -80.6548882}, 'CORONEL PORTILLO': {'lat': -8.392826399999999, 'lng': -74.5826184}, 'SANTA': {'lat': -9.000741099999999, 'lng': -78.60014819999999}, 'ICA': {'lat': -14.07546, 'lng': -75.7341811}, 'MAYNAS': {'lat': -3.7700696, 'lng': -73.2625513}, 'CUSCO': {'lat': -13.53195, 'lng': -71.96746259999999}, 'HUANCAYO': {'lat': -12.0686357, 'lng': -75.21029759999999}, 'SULLANA': {'lat': -4.903638, 'lng': -80.68643229999999}, 'TACNA': {'lat': -18.0065679, 'lng': -70.2462741}, 'HUANUCO': {'lat': -9.920764799999999, 'lng': -76.2410843}, 'HUAMANGA': {'lat': -13.1638737, 'lng': -74.22356409999999}, 'HUAURA': {'lat': -11.0674409, 'lng': -77.59815789999999}, 'MARISCAL NIETO': {'lat': -17.1883246, 'lng': -70.93181799999999}, 'JAEN': {'lat': -5.709441200000001, 'lng': -78.7986181}, 'LAMBAYEQUE': {'lat': -6.7197666, 'lng': -79.9080757}, 'SAN MARTIN': {'lat': -7.244488100000001, 'lng': -76.8259652}, 'CAJAMARCA': {'lat': -7.1617465, 'lng': -78.51278549999999}, 'TAMBOPATA': {'lat': -12.5825295, 'lng': -69.19327620000001}, 'TUMBES': {'lat': -3.5564921, 'lng': -80.4270885}, 'HUARAL': {'lat': -11.4965172, 'lng': -77.21177329999999}, 'BAGUA': {'lat': -5.6361357, 'lng': -78.5307552}, 'HUARAZ': {'lat': -9.5261154, 'lng': -77.5287792}, 'CHINCHA': {'lat': -13.42553, 'lng': -76.13671099999999}, 'PISCO': {'lat': -13.7134562, 'lng': -76.1841701}, 'CAÑETE': {'lat': -12.779861, 'lng': -76.5565245}, 'BARRANCA': {'lat': -10.7525374, 'lng': -77.7599218}, 'SAN ROMAN': {'lat': -15.4998363, 'lng': -70.129655}, 'UTCUBAMBA': {'lat': -5.7587712, 'lng': -78.4463395}, 'ILO': {'lat': -17.6680839, 'lng': -71.3468091}, 'HUANCAVELICA': {'lat': -12.7861978, 'lng': -74.9764024}, 'PUNO': {'lat': -15.8402218, 'lng': -70.0218805}, 'PASCO': {'lat': -10.4475753, 'lng': -75.1545381}, 'PAITA': {'lat': -5.0938488, 'lng': -81.0962172}, 'MOYOBAMBA': {'lat': -6.0419882, 'lng': -76.97006689999999}, 'CHANCHAMAYO': {'lat': -11.0061643, 'lng': -75.36453689999999}, 'TALARA': {'lat': -4.581151999999999, 'lng': -81.26289609999999}, 'ALTO AMAZONAS': {'lat': -5.8846104, 'lng': -76.1304244}, 'LA CONVENCION': {'lat': -12.864972, 'lng': -72.6927338}, 'CHEPEN': {'lat': -7.2271893, 'lng': -79.42882569999999}, 'DATEM DEL MARAÑON': {'lat': -4.827869300000001, 'lng': -76.55362579999999}, 'CONDORCANQUI': {'lat': -4.5981329, 'lng': -77.8630458}, 'NAZCA': {'lat': -14.8358687, 'lng': -74.9327583}, 'FERREÑAFE': {'lat': -6.6340676, 'lng': -79.7869714}, 'ASCOPE': {'lat': -7.7141138, 'lng': -79.1072559}, 'ABANCAY': {'lat': -13.6391954, 'lng': -72.8929}, 'LORETO': {'lat': -4.232472899999999, 'lng': -74.21793260000001}, 'RIOJA': {'lat': -6.057048399999999, 'lng': -77.1657716}, 'HUAROCHIRI': {'lat': -12.1385796, 'lng': -76.22763370000001}, 'SATIPO': {'lat': -11.2555478, 'lng': -74.63943309999999}, 'ISLAY': {'lat': -17.0221667, 'lng': -72.0115217}, 'LEONCIO PRADO': {'lat': -9.2971053, 'lng': -75.9995756}, 'CAYLLOMA': {'lat': -15.1895112, 'lng': -71.7707989}, 'SAN IGNACIO': {'lat': -5.146268, 'lng': -79.0023523}, 'CHACHAPOYAS': {'lat': -6.230154700000001, 'lng': -77.87084779999999}, 'PADRE ABAD': {'lat': -9.0395542, 'lng': -75.5101255}, 'TOCACHE': {'lat': -8.1893672, 'lng': -76.5148645}, 'MARISCAL CACERES': {'lat': -7.179000699999999, 'lng': -76.73096439999999}, 'MORROPON': {'lat': -5.190889599999999, 'lng': -79.9668308}, 'ZARUMILLA': {'lat': -3.4949817, 'lng': -80.2711588}, 'VIRU': {'lat': -8.541058399999999, 'lng': -78.67578069999999}, 'LAMAS': {'lat': -6.424309099999999, 'lng': -76.5083562}, 'CHUPACA': {'lat': -12.0561522, 'lng': -75.2858208}, 'PALPA': {'lat': -14.5340655, 'lng': -75.1808035}, 'HUARMEY': {'lat': -10.0664169, 'lng': -78.1506824}, 'EL DORADO': {'lat': -6.6154684, 'lng': -76.6964251}, 'OXAPAMPA': {'lat': -10.5750237, 'lng': -75.40001099999999}, 'PACASMAYO': {'lat': -7.4040051, 'lng': -79.565078}, 'YAULI': {'lat': -11.669646, 'lng': -76.0880379}, 'BELLAVISTA': {'lat': -12.0570992, 'lng': -77.10740129999999}, 'HUANTA': {'lat': -12.9384113, 'lng': -74.25021219999999}, 'CASMA': {'lat': -9.4718308, 'lng': -78.3006626}, 'AYABACA': {'lat': -4.6389001, 'lng': -79.7147196}, 'TARMA': {'lat': -11.4193347, 'lng': -75.68894929999999}, 'MARISCAL RAMON CASTILLA': {'lat': -3.9091249, 'lng': -70.51718699999999}, 'ANDAHUAYLAS': {'lat': -13.6616515, 'lng': -73.3767641}, 'TAYACAJA': {'lat': -12.3996495, 'lng': -74.8674997}, 'SECHURA': {'lat': -5.5622396, 'lng': -80.8187744}, 'PUERTO INCA': {'lat': -9.3789658, 'lng': -74.96539659999999}, 'HUALGAYOC': {'lat': -6.7638136, 'lng': -78.6068528}, 'ANGARAES': {'lat': -12.9900984, 'lng': -74.6868815}, 'TAHUAMANU': {'lat': -11.40422, 'lng': -69.4878456}, 'CAMANA': {'lat': -16.6235522, 'lng': -72.7104708}, 'JAUJA': {'lat': -11.7806236, 'lng': -75.4869033}, 'HUAYLAS': {'lat': -8.8710472, 'lng': -77.8924608}, 'CANCHIS': {'lat': -14.2705516, 'lng': -71.2285624}, 'REQUENA': {'lat': -5.0641652, 'lng': -73.8507279}, 'CHOTA': {'lat': -6.558192999999999, 'lng': -78.64838429999999}, 'CONCEPCION': {'lat': -11.9187621, 'lng': -75.3149796}, 'ACOBAMBA': {'lat': -12.8435129, 'lng': -74.569682}, 'PATAZ': {'lat': -7.7877469, 'lng': -77.5948946}, 'PICOTA': {'lat': -6.9162465, 'lng': -76.3316169}, 'HUALLAGA': {'lat': -6.937041799999999, 'lng': -76.7722076}, 'CARAVELI': {'lat': -15.7734675, 'lng': -73.36714119999999}, 'LUCANAS': {'lat': -14.6199392, 'lng': -74.23194079999999}, 'HUAMALIES': {'lat': -9.5504091, 'lng': -76.81647029999999}, 'MANU': {'lat': -12.9076075, 'lng': -70.3625}, 'CANTA': {'lat': -11.4691392, 'lng': -76.62322019999999}, 'CHUCUITO': {'lat': -15.9039696, 'lng': -69.8865431}, 'AMBO': {'lat': -10.1202456, 'lng': -76.2044549}, 'LUYA': {'lat': -6.5726739, 'lng': -77.86574879999999}, 'CONTRALMIRANTE VILLAR': {'lat': -3.9805969, 'lng': -80.9756708}, 'LA MAR': {'lat': -12.1133027, 'lng': -77.0452667}, 'JUNIN': {'lat': -11.1581925, 'lng': -75.9926306}, 'AZANGARO': {'lat': -14.9164287, 'lng': -70.196185}, 'GENERAL SANCHEZ CERRO': {'lat': -16.6733758, 'lng': -70.9705535}, 'CUTERVO': {'lat': -6.376045299999999, 'lng': -78.821275}, 'SANTIAGO DE CHUCO': {'lat': -8.146883599999999, 'lng': -78.1721189}, 'DANIEL ALCIDES CARRION': {'lat': -12.0349963, 'lng': -76.99400729999999}, 'SANCHEZ CARRION': {'lat': -7.8143595, 'lng': -78.0435462}, 'SAN MIGUEL': {'lat': -12.0774344, 'lng': -77.0934137}, 'OTUZCO': {'lat': -7.9050794, 'lng': -78.5605941}, 'CAJABAMBA': {'lat': -7.620956899999999, 'lng': -78.0452217}, 'HUANCABAMBA': {'lat': -5.238991299999999, 'lng': -79.4506989}, 'GRAN CHIMU': {'lat': -7.4792712, 'lng': -78.8189809}, 'PARINACOCHAS': {'lat': -15.0172316, 'lng': -73.781235}, 'ANTA': {'lat': -13.4622252, 'lng': -72.1494902}, 'SANTA CRUZ': {'lat': -6.6264487, 'lng': -78.94452}, 'HUANCANE': {'lat': -15.2053189, 'lng': -69.76145679999999}, 'QUISPICANCHI': {'lat': -13.6862236, 'lng': -71.62393999999999}, 'EL COLLAO': {'lat': -16.0799062, 'lng': -69.637632}, 'DOS DE MAYO': {'lat': -9.6779763, 'lng': -76.7052267}, 'URUBAMBA': {'lat': -13.3057641, 'lng': -72.1156281}, 'MELGAR': {'lat': -14.8821885, 'lng': -70.5905977}, 'YUNGAY': {'lat': -9.1384166, 'lng': -77.7423469}, 'CASTILLA': {'lat': -5.1141844, 'lng': -80.49938569999999}, 'UCAYALI': {'lat': -9.8251183, 'lng': -73.087749}, 'CELENDIN': {'lat': -6.8666512, 'lng': -78.1421905}, 'CARHUAZ': {'lat': -9.281744, 'lng': -77.6450215}, 'POMABAMBA': {'lat': -8.8202492, 'lng': -77.46159229999999}, 'PACHITEA': {'lat': -9.8977124, 'lng': -75.9934818}, 'RECUAY': {'lat': -9.7231582, 'lng': -77.45442109999999}, 'ATALAYA': {'lat': -10.7317689, 'lng': -73.7585828}, 'COTABAMBAS': {'lat': -13.75711, 'lng': -72.363632}, 'HUARI': {'lat': -9.3483845, 'lng': -77.1708039}, 'BONGARA': {'lat': -5.9467286, 'lng': -77.9789692}, 'PUTUMAYO': {'lat': -2.5779366, 'lng': -72.8042797}, 'CALCA': {'lat': -13.324084, 'lng': -71.9549533}, 'YAUYOS': {'lat': -12.4600538, 'lng': -75.9167047}, 'HUAYTARA': {'lat': -13.6040212, 'lng': -75.3532422}, 'SAN MARCOS': {'lat': -7.332225999999999, 'lng': -78.1706939}, 'CARABAYA': {'lat': -14.0691337, 'lng': -70.4281661}, 'CHURCAMPA': {'lat': -12.7396025, 'lng': -74.3871012}, 'CASTROVIRREYNA': {'lat': -13.2772535, 'lng': -75.31696090000001}, 'CONTUMAZA': {'lat': -7.366643400000001, 'lng': -78.8051114}, 'YUNGUYO': {'lat': -16.2494365, 'lng': -69.08808189999999}, 'SANDIA': {'lat': -14.2377128, 'lng': -69.4381162}, 'ESPINAR': {'lat': -14.7895845, 'lng': -71.412125}, 'JORGE BASADRE': {'lat': -12.0315285, 'lng': -77.0730882}, 'LAMPA': {'lat': -15.3636353, 'lng': -70.36675919999999}, 'SAN ANTONIO DE PUTINA': {'lat': -14.91256, 'lng': -69.874893}, 'CHINCHEROS': {'lat': -13.3964033, 'lng': -72.0514291}, 'SIHUAS': {'lat': -8.5547681, 'lng': -77.6292697}, 'CHUMBIVILCAS': {'lat': -14.4501924, 'lng': -72.0819794}, 'CANGALLO': {'lat': -13.6291421, 'lng': -74.1438375}, 'BOLOGNESI': {'lat': -9.8974616, 'lng': -76.9416139}, 'SAN PABLO': {'lat': -7.1143481, 'lng': -78.8226909}, 'YAROWILCA': {'lat': -9.9109324, 'lng': -76.6054151}, 'VICTOR FAJARDO': {'lat': -13.8495891, 'lng': -73.94946999999999}, 'PAUCARTAMBO': {'lat': -10.7599544, 'lng': -75.737149}, 'OYON': {'lat': -10.6671279, 'lng': -76.7697201}, 'CONDESUYOS': {'lat': -15.8391766, 'lng': -72.6524364}, 'AYMARAES': {'lat': -14.2957746, 'lng': -73.2423779}, 'RODRIGUEZ DE MENDOZA': {'lat': -6.3941102, 'lng': -77.4855682}, 'MARISCAL LUZURIAGA': {'lat': -8.865037599999999, 'lng': -77.35736729999999}, 'CANAS': {'lat': -14.4942232, 'lng': -71.1539136}, 'JULCAN': {'lat': -8.0435356, 'lng': -78.4863068}, 'ACOMAYO': {'lat': -13.9194933, 'lng': -71.6833925}, 'AIJA': {'lat': -9.780802999999999, 'lng': -77.6092188}, 'PARURO': {'lat': -13.7607869, 'lng': -71.846825}, 'GRAU': {'lat': -14.2507573, 'lng': -72.6809696}, 'VILCAS HUAMAN': {'lat': -13.6541087, 'lng': -73.9521468}, 'PURUS': {'lat': -9.7715865, 'lng': -70.709413}, 'LA UNION': {'lat': -9.82645, 'lng': -76.80157360000001}, 'PALLASCA': {'lat': -8.25, 'lng': -78.016667}, 'ANTONIO RAIMONDI': {'lat': -12.0738752, 'lng': -76.9512878}, 'LAURICOCHA': {'lat': -10.0761171, 'lng': -76.7352198}, 'OCROS': {'lat': -10.4031418, 'lng': -77.3977529}, 'MOHO': {'lat': -15.3575208, 'lng': -69.5007996}, 'ANTABAMBA': {'lat': -14.3647468, 'lng': -72.87858299999999}, 'CAJATAMBO': {'lat': -10.4698775, 'lng': -76.9948825}, 'PAUCAR DEL SARA SARA': {'lat': -15.1799054, 'lng': -73.1854901}, 'CORONGO': {'lat': -8.5697207, 'lng': -77.89689160000002}, 'TARATA': {'lat': -17.4776078, 'lng': -70.0339387}, 'CANDARAVE': {'lat': -17.2695445, 'lng': -70.2526074}, 'HUANCA SANCOS': {'lat': -13.9202424, 'lng': -74.3345526}, 'HUACAYBAMBA': {'lat': -9.0950407, 'lng': -76.83688959999999}, 'SUCRE': {'lat': -14.0100232, 'lng': -73.8376451}, 'MARAÑON': {'lat': -5.0654867, 'lng': -76.00139899999999}, 'CARLOS FERMIN FITZCARRALD': {'lat': -8.9928645, 'lng': -77.2904855}, 'ASUNCION': {'lat': -9.1790237, 'lng': -77.42008229999999}, 'BOLIVAR': {'lat': -7.1540803, 'lng': -77.7021603}}


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
    
        # def df_to_dict_b(df):
        #     if df.ndim == 1:
        #         return df.to_dict()

        #     ret = {}
        #     for key in df.index.get_level_values(0):
        #         sub_df = df.xs(key)
        #         ret[key] = df_to_dict_b(sub_df)
        #     return ret
            

        # def get_province_distr_back(df):
        #     # print(df[['PROVINCIA', 'DISTRITO']])
        #     newDF = df[['PROVINCIA', 'DISTRITO','CANTIDAD']].groupby(["PROVINCIA", "DISTRITO"])[
        #         ['CANTIDAD','PROVINCIA']].sum().sort_values(by=['CANTIDAD'],ascending=False)
        #     data = df_to_dict(newDF)
        #     r = json.dumps(data,  indent=4)
        #     loaded_r = json.loads(r)
        #     # json.dumps(parsed, indent=4)
        #     return r 







# =====================================================================================
# ===================Esta parte es para traer todas las ubicaciones en lat y lng de un lugar
# ==============================================================================================
# def get_province_lat_lng(province):
#     from pathlib import Path  # Python 3.6+ only
#     env_path = Path('.') / '.env'
#     load_dotenv(dotenv_path=env_path)
#     API_KEY = os.getenv("API_KEY")
#     # print(API_KEY)
#     province = f"{province} PERU"
#     url = f'https://maps.googleapis.com/maps/api/geocode/json?address={province}&key={API_KEY}'
#     headers = {
#         "Content-Type": "text/json"}
#     r = requests.get(url, headers=headers)
#     data = r.content
#     data_dict = json.loads(data)
#     # data_df = pd.DataFrame(data_dict['incidents'])
#     # print(data_dict["results"][0]["geometry"]["location"])
#     return data_dict["results"][0]["geometry"]["location"]


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
    return dep_prov_to_dict(df, newDF)


# ==============Complement to the another function ==================
# def get_provinces_location(df):
#     new_df = df[['PROVINCIA','CANTIDAD']].groupby(["PROVINCIA"])[
#         ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)

#     provinces = {}

#     for index, item in enumerate(new_df.index.get_level_values(0)):
#         # provinces[item] = int(new_df["CANTIDAD"][index])
#         provinces[item] = get_province_lat_lng(item)
#     # print(provinces)
#     return provinces
# =======================================================================



def get_provinces(df):
    new_df = df[['PROVINCIA','CANTIDAD']].groupby(["PROVINCIA"])[
        ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)

    provinces = {"provinces":[]}
    for index, item in enumerate(new_df.index.get_level_values(0)):
        provinces["provinces"].append(
            {"nombre":item,"cantidad": int(new_df["CANTIDAD"][index]), "location" : LOCATION[item]}
        )
    ret = json.dumps(provinces,  indent=4)
    loaded_r = json.loads(ret)
    return ret

# =====================??????????=========================
    # def get_provinces(df):
    #     new_df = df[['PROVINCIA','CANTIDAD']].groupby(["PROVINCIA"])[
    #         ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)

    #     provinces = {"provinces":[]}
    #     for index, item in enumerate(new_df.index.get_level_values(0)):
    #         provinces["provinces"].append(
    #             {"nombre":item,"cantidad": int(new_df["CANTIDAD"][index]), "location" : LOCATION[item]}
    #         )
    #     ret = json.dumps(provinces,  indent=4)
    #     loaded_r = json.loads(ret)
    #     return ret
# =====================??????????=========================



def get_provinces(df):
    new_df = df[['PROVINCIA','CANTIDAD']].groupby(["PROVINCIA"])[
        ['CANTIDAD']].sum().sort_values(by=['CANTIDAD'],ascending=False)

    provinces = {"type":"FeatureCollection","features":[]}
    for index, item in enumerate(new_df.index.get_level_values(0)):
        provinces["features"].append(
            {
                "type": "Feature",
                "properties": {
                    "nombre":item,
                    "cantidad": int(new_df["CANTIDAD"][index])
                },
                "geometry":{"type": "Point","coordinates" : [LOCATION[item]["lng"],LOCATION[item]["lat"]]}
            }
        )
    ret = json.dumps(provinces,  indent=4)
    loaded_r = json.loads(ret)
    return ret
def predict(df):
    # df["FECHA"]=df["FECHA_RESULTADO"]
    n_df = df[["FECHA_RESULTADO", "CANTIDAD"]].groupby(["FECHA_RESULTADO"]).sum().sort_values(by=['FECHA_RESULTADO'],ascending=True)

    # crear variaable para predecir 'x' dias en el futuro
    future_days = 50
    # creacion de una nueva columna (target)
    # my_df = n_df["CANTIDAD"]


    n_df['PREDICTION'] = n_df[['CANTIDAD']].shift(-future_days)
    # n_df['PREDICTION'] = n_df[['CANTIDAD']]




    # X = np.array(n_df.drop(['PREDICTION'], 1))[:-future_days]
    # y = np.array(n_df['PREDICTION'])[:-future_days]
    # print(n_df[100:])
    X = np.array(n_df.drop(['PREDICTION'], 1))[:-future_days]
    y = np.array(n_df['PREDICTION'])[:-future_days]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)
    # print(X,y)
    #Create the decision tree regressor model
    tree = DecisionTreeRegressor().fit(x_train, y_train)
    #Create the linear regression model
    lr = LinearRegression().fit(x_train, y_train)

    #Get the feature data, 
    #AKA all the rows from the original data set except the last 'x' days
    x_future = n_df.drop(['PREDICTION'], 1)[:-future_days]

    #Get the last 'x' rows
    x_future = x_future.tail(future_days) 
    # print("x_future", x_future)
    #Convert the data set into a numpy array
    x_future = np.array(x_future)
    
    # print(tree.score(x_test,y_test))
    #Show the model tree prediction
    tree_prediction = tree.predict(x_future)
    #Show the model linear regression prediction
    lr_prediction = lr.predict(x_future)


    #Visualize the data
    # predictions = tree_prediction
    pd.options.mode.chained_assignment = None 

    valid =  n_df[X.shape[0]:]
    valid['Predictions'] = tree_prediction 

    valid.drop('PREDICTION', axis='columns', inplace=True)

    # plt.figure(figsize=(16,8))
    # plt.title('Modelo de predicción de casos nuevos de coronavirus en los últimos 30 días en el Perú')
    # plt.xlabel('Días',fontsize=18)
    # plt.ylabel('Cantidad',fontsize=18)
    # plt.plot(n_df['CANTIDAD'])
    # plt.plot(valid[['CANTIDAD','Predictions']])
    # plt.legend(['Train', 'Val', 'Prediction' ], loc='best')
    # plt.show()  
    data_predicted = {"data":[]}
    for index in valid.index.get_level_values(0):
        fecha = f"{str(index)[:4]}-{str(index)[4:6]}-{str(index)[6:8]}"
        data_predicted["data"].append(
            {
                "fecha":fecha,
                "cantidadReal":int(valid["CANTIDAD"][index]),
                "cantidadPredecida": int(valid['Predictions'][index])
                
                
            }
        )
        
    ret = json.dumps(data_predicted,  indent=4)
    loaded_r = json.loads(ret)
    return ret

if __name__ == "__main__":
    df = get_dataframe()
    # get_department_province
    # get_positives require an index 
    # get_provinces
    switcher = {
        "get_department_province": get_department_province,
        "get_positives": get_positives,
        "get_provinces": get_provinces,
        "predict": predict
    }
    # Get the function from switcher dictionary
    func = switcher.get(sys.argv[1], lambda: "Invalid month")
    # Execute the function
    if len(sys.argv) == 3:
        print(func(df, sys.argv[2]))
    else:
        print(func(df))

    # print(sys.argv[1](df, sys.argv[1]))
