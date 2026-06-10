import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="FM AI Enterprise",
    layout="wide"
)

# ---------------------------------------------------
# SESSION
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🏢 FM AI Enterprise")
st.sidebar.subheader(
    "Knowledge Base Upload"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)
page = st.sidebar.radio(
    "Navigation",
    [
        "AI Assistant",
        "Assets",
        "Work Orders",
        "Incidents",
        "Analytics"
    ]
)

# ---------------------------------------------------
# AI ASSISTANT
# ---------------------------------------------------

if page == "AI Assistant":

    st.title("🤖 FM AI Enterprise Assistant")

    query = st.chat_input(
        "Ask anything about HVAC, Electrical, Fire, Vendor..."
    )

    if query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        response = requests.post(
            API_URL,
            json={"query": query}
        )

        result = response.json()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": str(result)
            }
        )

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ---------------------------------------------------
# ASSETS
# ---------------------------------------------------

from database.assets_service import get_assets

assets = get_assets()

st.dataframe(
    assets,
    use_container_width=True
)

# ---------------------------------------------------
# WORK ORDERS
# ---------------------------------------------------

elif page == "Work Orders":

    st.title("📋 Work Order Dashboard")

    wo_data = pd.DataFrame({

        "WO ID": [
            "WO-1001",
            "WO-1002",
            "WO-1003"
        ],

        "System": [
            "HVAC",
            "Fire",
            "Electrical"
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
        wo_data,
        use_container_width=True
    )

# ---------------------------------------------------
# INCIDENTS
# ---------------------------------------------------

elif page == "Incidents":

    st.title("🚨 Incident Dashboard")

    incident_data = pd.DataFrame({

        "Incident ID": [
            "INC-1001",
            "INC-1002"
        ],

        "Description": [
            "Water leakage basement",
            "Fire detector fault"
        ],

        "Severity": [
            "Medium",
            "High"
        ],

        "Status": [
            "Open",
            "Closed"
        ]
    })

    st.dataframe(
        incident_data,
        use_container_width=True
    )
#Analytics Section
elif page == "Analytics":

    st.title("Facility Analytics")

    df = pd.DataFrame({

        "Severity": [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],

        "Count": [
            12,
            9,
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
