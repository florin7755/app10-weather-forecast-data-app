import pytest
import streamlit as st
from streamlit.web import cli as stcli
from streamlit import runtime
import sys
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Select the number of forecast days")
option = st.selectbox("select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t , labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)

if __name__ == '__main__':
    if runtime.exists():
       name = tuple
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

