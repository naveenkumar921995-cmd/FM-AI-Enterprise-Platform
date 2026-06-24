import streamlit as st
import pandas as pd
import os
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# -----------------------------------
# IMPORT AGENTS
# -----------------------------------

from agents.supervisor_agent import supervisor_agent
from agents.hvac_agent import hvac_agent
from agents.electrical_agent import electrical_agent
from agents.fire_agent import fire_agent

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="FM AI Enterprise",
    layout="wide"
)

# -----------------------------------
# SESSION
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🏢 FM AI Enterprise")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Assistant",
        "Assets",
        "Work Orders",
        "Incidents",
        "Vendors",
        "Analytics"
    ]
)

# -----------------------------------
# DASHBOARD
# -----------------------------------

if page == "Dashboard":

    st.title("🏢 Executive Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Assets",
            "500"
        )

    with col2:
        st.metric(
            "Open Work Orders",
            "128"
        )

    with col3:
        st.metric(
            "Critical Incidents",
            "12"
        )

    with col4:
        st.metric(
            "SLA Compliance",
            "96%"
        )

    st.divider()

    chart_data = pd.DataFrame(
        {
            "Month": [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May"
            ],
            "Incidents": [
                22,
                18,
                15,
                12,
                10
            ]
        }
    )

    st.line_chart(
        chart_data.set_index("Month")
    )

# -----------------------------------
# AI ASSISTANT
# -----------------------------------
elif page == "AI Assistant":

    st.title("🤖 FM AI Enterprise Assistant")

    query = st.chat_input(
        "Ask HVAC, Electrical, Fire related question..."
    )

    if query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        try:

            result = supervisor_agent(query)

        except Exception as e:

            result = {
                "agent": "System",
                "answer": str(e)
            }

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result
            }
        )

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            if msg["role"] == "user":

                st.write(
                    msg["content"]
                )

            else:

                result = msg["content"]

                if isinstance(result, dict):

                    st.subheader(
                        result.get(
                            "agent",
                            "AI Assistant"
                        )
                    )

                    st.write(
                        result.get(
                            "answer",
                            "No response available."
                        )
                    )

                    if result.get("recommendation"):

                        st.info(
                            result["recommendation"]
                        )

                    if result.get("citations"):

                        st.subheader(
                            "📚 References"
                        )

                        for item in result["citations"]:

                            st.write(
                                f"📄 {item.get('file','Unknown')} | "
                                f"Page {item.get('page','N/A')}"
                            )

                else:

                    st.write(
                        str(result)
                    )
# -----------------------------------
# ASSETS
# -----------------------------------
elif page == "Assets":

    st.title("🏭 Asset Management")

    assets = pd.read_csv("data/assets.csv")

    st.metric(
        "Total Assets",
        len(assets)
    )

    st.dataframe(
        assets,
        use_container_width=True
    )
# -----------------------------------
# WORK ORDERS
# -----------------------------------

elif page == "Work Orders":

    st.title("📋 Work Order Dashboard")

    wo = pd.read_csv(
        "data/work_orders.csv"
    )

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "Total WO",
            len(wo)
        )

    with c2:
        st.metric(
            "Open WO",
            len(
                wo[
                    wo["status"]=="Open"
                ]
            )
        )

    with c3:
        st.metric(
            "Closed WO",
            len(
                wo[
                    wo["status"]=="Closed"
                ]
            )
        )

    st.dataframe(
        wo,
        use_container_width=True
    )
# -----------------------------------
# INCIDENTS
# -----------------------------------

elif page == "Incidents":

    st.title("🚨 Incident Dashboard")

    incidents = pd.read_csv(
        "data/incidents.csv"
    )

    st.metric(
        "Total Incidents",
        len(incidents)
    )

    st.dataframe(
        incidents,
        use_container_width=True
    )
# -----------------------------------
# VENDORS
# -----------------------------------

elif page == "Vendors":

    st.title("🏢 Vendor Management")

    vendors = pd.read_csv(
        "data/vendors.csv"
    )

    st.metric(
        "Total Vendors",
        len(vendors)
    )

    st.dataframe(
        vendors,
        use_container_width=True
    )
# -----------------------------------
# ANALYTICS
# -----------------------------------
elif page == "Vendors":

    st.title("🏢 Vendor Management")

    vendors = pd.read_csv(
        "data/vendors.csv"
    )

    st.dataframe(
        vendors,
        use_container_width=True
    )
elif page == "Analytics":

    st.title("📊 Analytics")

    df = pd.DataFrame({

        "Severity": [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],

        "Count": [
            10,
            15,
            8,
            3
        ]
    })

    st.bar_chart(
        df.set_index("Severity")
    )
