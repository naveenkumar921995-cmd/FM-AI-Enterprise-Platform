import streamlit as st
import pandas as pd

try:
    assets = pd.read_csv("data/assets.csv")
    work_orders = pd.read_csv("data/work_orders.csv")
    incidents = pd.read_csv("data/incidents.csv")
    vendors = pd.read_csv("data/vendors.csv")

    st.title("🏢 Executive Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Assets",
            len(assets)
        )

    with col2:
        st.metric(
            "Work Orders",
            len(work_orders)
        )

    with col3:
        st.metric(
            "Incidents",
            len(incidents)
        )

    with col4:
        st.metric(
            "Vendors",
            len(vendors)
        )

    st.divider()

    st.subheader("Assets by System")

    st.bar_chart(
        assets["system"].value_counts()
    )

    st.subheader("Work Orders Status")

    st.bar_chart(
        work_orders["status"].value_counts()
    )

except Exception as e:

    st.error(
        f"Dashboard Error: {str(e)}"
    )
