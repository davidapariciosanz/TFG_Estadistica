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
opciones_predeterminadas = ["Grado en Estadística", 'Grado en Física', 'Grado en Matemáticas']
degrees = st.multiselect('Selecciona las opciones:', all_degrees, default=opciones_predeterminadas)

# Define the available options for the selector
available_options = ['spline', 'line']
# Set the default value
default_value = 'spline'
# Add a selector with limited options to "spline" or "line"
selected_type = st.selectbox('Select a type:', available_options, index=available_options.index(default_value))

# Lista de diccionarios vacía para almacenar las series seleccionadas
series_dict = []

# Generar la lista de diccionarios basada en las opciones seleccionadas
for degree in degrees:
    
    data = df_degrees_counts.loc[df_degrees_counts["Titulacion"] == degree].drop(columns=["Titulacion"]).values.tolist()[0]
    
    serie = {
        "type": selected_type,
        "name": degree,
        "data": data
    }
    
    series_dict.append(serie)
    
as_str = {
    "chart": {
        "type": selected_type
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
        selected_type: {
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


plot_2 = {
   "chart":{
      "type": "boxplot"
   },
   "title":{
      "text": "Highcharts Box Plot Example"
   },
   "legend":{
      "enabled":False
   },
   "xAxis":{
      "categories":[
         "1",
         "2",
         "3",
         "4",
         "5"
      ],
      "title":{
         "text":"Experiment No."
      }
   },
   "yAxis":{
      "title":{
         "text":"Observations"
      },
      "plotLines":[
         {
            "value":932,
            "color":"red",
            "width":1,
            "label":{
               "text":"Theoretical mean: 932",
               "align":"center",
               "style":{
                  "color":"gray"
               }
            }
         }
      ]
   },
   "series":[
      {
         "name":"Observations",
         "data":[
            [
               760,
               801,
               848,
               895,
               965
            ],
            [
               733,
               853,
               939,
               980,
               1080
            ],
            [
               714,
               762,
               817,
               870,
               918
            ],
            [
               724,
               802,
               806,
               871,
               950
            ],
            [
               834,
               836,
               864,
               882,
               910
            ]
         ]
      },
      {
         "name":"Outliers",
         "color":"black",
         "type":"scatter",
         "data":[
            [
               0,
               644
            ],
            [
               4,
               718
            ],
            [
               4,
               951
            ],
            [
               4,
               969
            ]
         ],
         "marker":{
            "fillColor":"white",
            "lineWidth":1,
            "lineColor":"black"
         }
      }
   ]
}

hg.streamlit_highcharts(plot_2, 640)

         
