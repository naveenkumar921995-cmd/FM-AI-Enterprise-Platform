import streamlit as st
import pandas as pd

st.title("Incident Analytics")

data = pd.DataFrame({
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
    data.set_index("Severity")
)
