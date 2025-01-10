import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"

def analytics_by_month_tab():
    st.title("Expense Breakdown By Month")

    response = requests.post(f"{API_URL}/analytics_month/")
    response = response.json()
    #st.write(response)

    data = {
        "Month": [month['Month'] for month in response],
        "Total": [month['total'] for month in response]
    }

    df = pd.DataFrame(data)

    st.bar_chart(data=df.set_index("Month")['Total'], width=0, height=0, use_container_width=True)
    df["Total"] = df["Total"].map("{:.2f}".format)

    st.table(df)