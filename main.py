import streamlit as st
import streamlit_highcharts as hg
import pprint


st.write("## Example")
selSample=st.selectbox("Choose a sample",[hg.SAMPLE11,hg.SAMPLE,hg.SAMPLE2,hg.SAMPLE3,hg.SAMPLE4,hg.SAMPLE5,hg.SAMPLE6,hg.SAMPLE7,hg.SAMPLE8,hg.SAMPLE9,hg.SAMPLE10],format_func=lambda x: str(x["title"]["text"])
)
value = hg.streamlit_highcharts(selSample,640)
with st.expander("Show code...",expanded=False):
    
    var=pprint.pformat(selSample,width=40,indent=2)
    st.code("import streamlit as st \
             \r\nimport streamlit_highcharts as hg \
             \r\n\r\nchartDef="+
            var + "\r\n\r\n\r\n" +
            "hg.streamlit_highcharts(chartDef,640)"
            ,language="python")


# Set the title of the app
st.title("My Streamlit App")

chart_def = {
    "title": {
        "text": "Sales of petroleum products March, Norway",
        "align": "left"
    },
    "xAxis": {
        "categories": ["Jet fuel", "Duty-free diesel"]
    },
    "yAxis": {
        "title": {"text": "Million liter"}
    },
    "series": [
        {"type": "column",
         "name": "2020",
         "data": [59, 83]},
        {"type": "column",
         "name": "2021",
         "data": [24, 79]
         },
        {"type": "column",
         "name": "2022",
         "data": [58, 88]
         },
        {"type": "spline",
         "name": "Average",
         "data": [47, 83.33],
         "marker": {
             "lineWidth": 2,
             "fillColor": "black",
         }
         }
    ]
}

hg.streamlit_highcharts(chart_def, 640)



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
    "series": [
        {"type":"spline",
         "name": 'Grado en Administración y Dirección de Empresas',
         "data": [65., 322., 330., 332., 360., 346.]},
        {"type":"spline",
         "name": 'Grado en Pruebaa',
         "data": [15., 32., 370., 32., 30., 46.]}
    ]
}


hg.streamlit_highcharts(as_str, 640)


as_str = {
   "chart":{
      "type":"line"
   },
   "title":{
      "text":"Monthly Average Temperature"
   },
   "subtitle":{
      "text":"Source: ""+""<a href=\"https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature\" ""+""target=\"_blank\">Wikipedia.com</a>"
   },
   "xAxis":{
      "categories":[
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
      ]
   },
   "yAxis":{
      "title":{
         "text":"Temperature (°C)"
      }
   },
   "plotOptions":{
      "line":{
         "dataLabels":{
            "enabled": True
         },
         "enableMouseTracking": False
      }
   },
   "series":[
      {
         "name":"Reggane",
         "data":[
            16.0,
            18.2,
            23.1,
            27.9,
            32.2,
            36.4,
            39.8,
            38.4,
            35.5,
            29.2,
            22.0,
            17.8
         ]
      },
      {
         "name":"Tallinn",
         "data":[
            -2.9,
            -3.6,
            -0.6,
            4.8,
            10.2,
            14.5,
            17.6,
            16.5,
            12.0,
            6.5,
            2.0,
            -0.9
         ]
      }
   ]
}


hg.streamlit_highcharts(as_str, 640)
