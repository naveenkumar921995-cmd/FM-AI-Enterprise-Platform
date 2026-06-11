import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")

# -----------------------------
# DARK THEME
# -----------------------------

st.markdown("""
<style>

.stApp{
background-color:#061426;
color:white;
}

.metric-card{
background:#0d2138;
padding:15px;
border-radius:12px;
border:1px solid #00d4ff;
text-align:center;
}

h1,h2,h3{
color:#00d4ff;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.title("🏢 FM AI ENTERPRISE COMMAND CENTER")

# -----------------------------
# KPI ROW
# -----------------------------

c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("SLA","97.2%","+2%")
c2.metric("MTTR","1.9 Hrs","-0.4")
c3.metric("MTBF","245 Days","+15")
c4.metric("Assets","99.1%","+1.2%")
c5.metric("Energy","-18%","+4%")
c6.metric("CSAT","94%","+3%")

# -----------------------------
# GAUGES
# -----------------------------

st.subheader("Executive KPI")

g1,g2,g3,g4 = st.columns(4)

def gauge(value,title):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text":title},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"cyan"}
        }
    ))

    fig.update_layout(
        height=250,
        paper_bgcolor="#061426",
        font_color="white"
    )

    return fig

with g1:
    st.plotly_chart(
        gauge(97,"SLA"),
        use_container_width=True
    )

with g2:
    st.plotly_chart(
        gauge(99,"Asset Availability"),
        use_container_width=True
    )

with g3:
    st.plotly_chart(
        gauge(94,"Occupant Satisfaction"),
        use_container_width=True
    )

with g4:
    st.plotly_chart(
        gauge(98,"Service Availability"),
        use_container_width=True
    )

# -----------------------------
# CENTER BUILDING PLACEHOLDER
# -----------------------------

st.subheader("Digital Twin Building")

st.image(
    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
    use_container_width=True
)

# -----------------------------
# INCIDENTS + WORK ORDERS
# -----------------------------

left,right = st.columns(2)

with left:

    st.subheader("Incident Summary")

    fig = go.Figure(
        data=[
            go.Pie(
                labels=[
                    "Critical",
                    "Major",
                    "Minor",
                    "Low"
                ],
                values=[
                    2,
                    5,
                    10,
                    7
                ],
                hole=.6
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="#061426",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("Work Orders")

    wo = pd.DataFrame({
        "Status":[
            "Open",
            "Closed",
            "Overdue",
            "Critical"
        ],
        "Count":[
            210,
            4850,
            18,
            12
        ]
    })

    st.bar_chart(
        wo.set_index("Status")
    )

# -----------------------------
# ENERGY
# -----------------------------

st.subheader("Energy Dashboard")

energy = pd.DataFrame({

    "Hour":[1,2,3,4,5,6,7,8,9,10],

    "HVAC":[10,15,12,18,16,20,18,17,21,19],

    "Lighting":[6,8,9,8,10,11,9,10,12,11],

    "Others":[5,7,6,8,7,9,8,9,10,8]
})

st.line_chart(
    energy.set_index("Hour")
)

# -----------------------------
# AI RECOMMENDATIONS
# -----------------------------

st.subheader("AI Insights")

st.warning(
    "⚠ Chiller-02 efficiency dropped by 8%"
)

st.warning(
    "⚠ AHU-15 filter replacement due"
)

st.warning(
    "⚠ UPS Battery health below threshold"
)

st.warning(
    "⚠ Fire Alarm Loop-3 communication issue"
)
