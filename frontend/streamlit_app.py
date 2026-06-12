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

    st.title("🤖 FM AI Assistant")

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

            category = route_query(query)

            if "hvac" in category:
                result = hvac_agent(query)

            elif "electrical" in category:
                result = electrical_agent(query)

            elif "fire" in category:
                result = fire_agent(query)

            else:
                result = {
                    "agent": "Supervisor Agent",
                    "answer": "Unable to determine correct department."
                }

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

                st.subheader(
                    result.get(
                        "agent",
                        "Assistant"
                    )
                )

                st.write(
                    result.get(
                        "answer",
                        ""
                    )
                )

                if "recommendation" in result:

                    st.info(
                        result["recommendation"]
                    )

                if "citations" in result:

                    st.subheader(
                        "📚 References"
                    )

                    for item in result["citations"]:

                        st.write(
                            f"📄 {item.get('file')} | Page {item.get('page')}"
                        )

# -----------------------------------
# ASSETS
# -----------------------------------

elif page == "Assets":

    st.title("🏭 Asset Management")

    assets = pd.DataFrame({

        "Asset ID": [
            "AHU-01",
            "CH-01",
            "DG-01"
        ],

        "System": [
            "HVAC",
            "HVAC",
            "Electrical"
        ],

        "Health Score": [
            95,
            88,
            92
        ]
    })

    st.dataframe(
        assets,
        use_container_width=True
    )

# -----------------------------------
# WORK ORDERS
# -----------------------------------

elif page == "Work Orders":

    st.title("📋 Work Orders")

    wo = pd.DataFrame({

        "WO ID": [
            "WO1001",
            "WO1002",
            "WO1003"
        ],

        "Priority": [
            "High",
            "Medium",
            "Low"
        ],

        "Status": [
            "Open",
            "Open",
            "Closed"
        ]
    })

    st.dataframe(
        wo,
        use_container_width=True
    )

# -----------------------------------
# INCIDENTS
# -----------------------------------

elif page == "Incidents":

    st.title("🚨 Incidents")

    incidents = pd.DataFrame({

        "Incident ID": [
            "INC001",
            "INC002"
        ],

        "Severity": [
            "High",
            "Medium"
        ],

        "Status": [
            "Open",
            "Closed"
        ]
    })

    st.dataframe(
        incidents,
        use_container_width=True
    )

# -----------------------------------
# ANALYTICS
# -----------------------------------

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
