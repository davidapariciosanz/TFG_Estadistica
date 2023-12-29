import streamlit as st
import streamlit_highcharts as hg
import pprint

# st.write("## Example")
# selSample=st.selectbox("Choose a sample",[hg.SAMPLE11,hg.SAMPLE,hg.SAMPLE2,hg.SAMPLE3,hg.SAMPLE4,hg.SAMPLE5,hg.SAMPLE6,hg.SAMPLE7,hg.SAMPLE8,hg.SAMPLE9,hg.SAMPLE10],format_func=lambda x: str(x["title"]["text"])
# )
# value = hg.streamlit_highcharts(selSample,640)
# with st.expander("Show code...",expanded=False):
    
#     var=pprint.pformat(selSample,width=40,indent=2)
#     st.code("import streamlit as st \
#              \r\nimport streamlit_highcharts as hg \
#              \r\n\r\nchartDef="+
#             var + "\r\n\r\n\r\n" +
#             "hg.streamlit_highcharts(chartDef,640)"
#             ,language="python")

# --------- D.A.S. ---------
import os
import pandas as pd
import pickle

UNIVERSITY = "uva"
PATH_CDATA = './cdata/' + UNIVERSITY

with open(os.path.join(PATH_CDATA, 'all_degrees.pkl'), 'rb') as file:
    all_degrees = pickle.load(file)

df_degrees_counts = pd.read_csv(os.path.join(PATH_CDATA, 'df_degrees_counts.csv'), encoding='latin1')

st.title("D.A.S.")
degrees = st.multiselect('Selecciona las opciones:', all_degrees)

# Lista de diccionarios vacía para almacenar las series seleccionadas
series_dict = []

# Generar la lista de diccionarios basada en las opciones seleccionadas
for degree in degrees:
    
    data = df_degrees_counts.loc[df_degrees_counts["Titulacion"] == degree].drop(columns=["Titulacion"]).values.tolist()[0]
    
    serie = {
        "type": "spline",
        "name": degree,
        "data": data
    }
    
    series_dict.append(serie)
    
as_str = {
    "chart": {
        "type": "spline"
    },
    "credits": {
        "enabled": False
    },
    "title": {
        "text": "Número de estudiantes por titulación"
    },
    "subtitle": {
        "text": 'Fuente: <a href="https://www.universidata.es/" target="_blank">UniversiDATA.es</a>'
    },
    "xAxis": {
        "categories": ["2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"],
        "accessibility": {
            "description": 'Months of the year'
        }
    },
    "yAxis": {
        "title": {
            "text": 'Número de estudiantes'
        }
    },
    "tooltip": {
        "crosshairs": True,
        "shared": True
    },
    "plotOptions": {
        "spline": {
            "marker": {
                "radius": 4,
                "lineColor": '#666666',
                "lineWidth": 1,
                "enable": False
            }
        }
    },
    "series": series_dict
}

hg.streamlit_highcharts(as_str, 640)
