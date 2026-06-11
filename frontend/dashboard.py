import streamlit as st
import pandas as pd

from database.dashboard_service import (
    get_dashboard_metrics
)

st.title("🏢 FM AI Enterprise Dashboard")

metrics = get_dashboard_metrics()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "SLA",
        f"{metrics['sla']}%"
    )

with col2:
    st.metric(
        "MTTR",
        f"{metrics['mttr']} Hrs"
    )

with col3:
    st.metric(
        "MTBF",
        f"{metrics['mtbf']} Days"
    )

with col4:
    st.metric(
        "Asset Availability",
        f"{metrics['asset_availability']}%"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Incident Summary")

    incident_df = pd.DataFrame({

        "Status": [
            "Open",
            "Closed"
        ],

        "Count": [
            metrics["open_incidents"],
            metrics["closed_incidents"]
        ]
    })

    st.bar_chart(
        incident_df.set_index("Status")
    )

with col2:

    st.subheader("Work Orders")

    wo_df = pd.DataFrame({

        "Type": [
            "Open",
            "Critical"
        ],

        "Count": [
            metrics["open_workorders"],
            metrics["critical_workorders"]
        ]
    })

    st.bar_chart(
        wo_df.set_index("Type")
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Energy KPI")

    st.metric(
        "Energy Reduction",
        f"{metrics['energy_reduction']}%"
    )

with col2:

    st.subheader("Customer Experience")

    st.metric(
        "Occupant Satisfaction",
        f"{metrics['occupant_satisfaction']}%"
    )

st.divider()

st.subheader("AI Recommendations")

st.success(
    "AHU-03 showing recurring filter blockage. PM recommended."
)

st.warning(
    "UPS-02 battery health below threshold."
)

st.info(
    "Fire Alarm Loop-2 communication loss detected last week."
)
