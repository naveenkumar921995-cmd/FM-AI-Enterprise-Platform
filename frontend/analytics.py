import streamlit as st
import pandas as pd

st.title("Facility Analytics")

df = pd.DataFrame({
    "Severity": [
        "Low",
        "Medium",
        "High",
        "Critical"
    ],
    "Count": [
        15,
        8,
        4,
        2
    ]
})

st.bar_chart(
    df.set_index("Severity")
)

st.metric(
    "MTTR",
    "3.5 Hours"
)

st.metric(
    "SLA Compliance",
    "96%"
)
