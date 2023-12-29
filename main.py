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
import ast
import os
import pandas as pd
import pickle
import numpy as np

UNIVERSITY = "uva"
PATH_CDATA = './cdata/' + UNIVERSITY

with open(os.path.join(PATH_CDATA, 'all_degrees.pkl'), 'rb') as file:
    all_degrees = pickle.load(file)

df_degrees_counts = pd.read_csv(os.path.join(PATH_CDATA, 'df_degrees_counts.csv'), encoding='latin1')
df_degrees_list = pd.read_csv(os.path.join(PATH_CDATA, 'df_degrees_list.csv'), encoding='latin1')


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

    "exporting": {
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

defecto = "Grado en Estadística"
filtered_rows = df_degrees_list.loc[df_degrees_list["Titulacion"] == defecto].drop(columns=["Titulacion"]).values

lista_1 = ast.literal_eval(filtered_rows[0].tolist()[0]),
lista_2 = ast.literal_eval(filtered_rows[0].tolist()[1])
lista_3 = ast.literal_eval(filtered_rows[0].tolist()[2])
lista_4 = ast.literal_eval(filtered_rows[0].tolist()[3])
lista_5 = ast.literal_eval(filtered_rows[0].tolist()[4])

plot_2 = {
    
   "chart":{
      "type": "boxplot"
   },
    
   "title":{
      "text": "Distribución de las notas de admisión: " + defecto
   },
    
   "legend":{
      "enabled": False
   },

    "credits": {
        "enabled": False
    },
    
    "exporting": {
        "enabled": False
    },
    
   "xAxis":{
      "categories":[
         "2017-18",
         "2018-19"
      ],
      "title":{
         "text":"Curso académico"
      }
   },
    
   "yAxis":{
      "title":{
         "text":"Nota de admisión"
      },
      "plotLines":[
         {
            "value":4,
            "color":"red",
            "width":1,
            "label":{
               "text":"Media teórica",
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
         "name":"Estadísticos",
         "data":[
             [
                 np.min(lista_1),
                 np.percentile(lista_1, 25),
                 np.median(lista_1),
                 np.percentile(lista_1, 75),
                 np.max(lista_1)
             ],
             [
                 np.min(lista_2),
                 np.percentile(lista_2, 25),
                 np.median(lista_2),
                 np.percentile(lista_2, 75),
                 np.max(lista_2)
             ],
             [
                 np.min(lista_3),
                 np.percentile(lista_3, 25),
                 np.median(lista_3),
                 np.percentile(lista_3, 75),
                 np.max(lista_3)
             ],
             [
                 np.min(lista_4),
                 np.percentile(lista_4, 25),
                 np.median(lista_4),
                 np.percentile(lista_4, 75),
                 np.max(lista_4)
             ],
             [
                 np.min(lista_5),
                 np.percentile(lista_5, 25),
                 np.median(lista_5),
                 np.percentile(lista_5, 75),
                 np.max(lista_5)
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
               2
            ],
            [
               1,
               3
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

         
plot_3 = {
   "chart":{
      "type":"packedbubble",
      "height":"100%"
   },
   "title":{
      "text":"Análisis clúster de titulaciones",
      "align":"left"
   },
   "tooltip":{
      "useHTML": True,
      "pointFormat":"<b>{point.name}:</b> {point.value} estudiantes"
   },
   "plotOptions":{
      "packedbubble":{
         "minSize":"20%",
         "maxSize":"100%",
         "zMin":0,
         "zMax":1000,
         "layoutAlgorithm":{
            "gravitationalConstant":0.05,
            "splitSeries":True,
            "seriesInteraction":False,
            "dragBetweenSeries":True,
            "parentNodeLimit":True
         },
         "dataLabels":{
            "enabled":True,
            "format":"{point.name}",
            "filter":{
               "property":"y",
               "operator":">",
               "value":250
            },
            "style":{
               "color":"black",
               "textOutline":"none",
               "fontWeight":"normal"
            }
         }
      }
   },
   "series":[
      {
         "name":"Clúster 1",
         "data":[
            {
               "name":'Grado en Matemáticas',
               "value":767.1
            },
            {
               "name":'Grado en Medicina',
               "value":20.7
            },
            {
               "name":'Grado en Nutrición Humana y Dietética',
               "value":97.2
            }
         ]
      },
       
      {
         "name":"Clúster 2",
         "data":[
            {
               "name":'Grado en Turismo',
               "value":8.2
            },
            {
               "name":'Grado en Traducción e Interpretación',
               "value":9.2
            }
         ]
      },
       
      {
         "name":"Clúster 3",
         "data":[
            {
               "name":'Grado en Fundamentos de la Arquitectura',
               "value":409.4
            },
            {
               "name":'Grado en Física',
               "value":34.1
            },
            {
               "name":'Grado en Geografía y Planificación Territorial',
               "value":7.1
            }
         ]
      }
   ]
}

hg.streamlit_highcharts(plot_3, 640)
