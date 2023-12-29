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

hg.streamlit_highcharts(chart_def, 640)

aux = st.selectbox('Select an option:', [0, 1])

if aux == 0:
    series_dict = [
        {"type": "spline",
         "name": 'Grado en Administración y Dirección de Empresas',
         "data": [65., 322., 330., 332., 360., 346.]},

        {"type": "spline",
         "name": 'Grado en Pruebaa',
         "data": [15., 32., 370., 32., 30., 46.]}
    ]

else:
    series_dict = [
        {"type": "spline",
         "name": 'Grado en Administración y Dirección de Empresas',
         "data": [65., 322., 330., 332., 360., 346.]}
    ]

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
