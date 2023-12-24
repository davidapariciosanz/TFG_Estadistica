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
