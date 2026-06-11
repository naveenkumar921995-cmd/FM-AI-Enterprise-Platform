import os
import streamlit as st
import requests
import pandas as pd
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
from rag.uploader import process_pdf

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="FM AI Enterprise",
    layout="wide"
)

# --------------------------------------------------
# SESSION
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🏢 FM AI Enterprise")

st.sidebar.subheader(
    "Knowledge Base Upload"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    filepath = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(filepath, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    chunks = process_pdf(filepath)

    st.sidebar.success(
        f"✅ PDF Indexed ({chunks} chunks)"
    )

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

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

if page == "Executive Dashboard":

    import frontend.executive_dashboard
# --------------------------------------------------
# AI ASSISTANT
# --------------------------------------------------

if page == "AI Assistant":

    st.title("🤖 FM AI Enterprise Assistant")

    query = st.chat_input(
        "Ask about HVAC, Electrical, Fire, Vendor, Incident..."
    )

    if query:

        response = requests.post(
            API_URL,
            json={
                "query": query
            }
        )

        result = response.json()

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result
            }
        )

    for msg in st.session_state.messages:

        with st.chat_message(
            msg["role"]
        ):

            if msg["role"] == "user":

                st.write(
                    msg["content"]
                )

            else:

                result = msg["content"]

                st.subheader(
                    result.get(
                        "agent",
                        "AI Assistant"
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
                        "📚 Sources"
                    )

                    for source in result["citations"]:

                        st.write(
                            f"📄 {source['file']} | Page {source['page']}"
                        )

# --------------------------------------------------
# ASSETS
# --------------------------------------------------

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

# --------------------------------------------------
# WORK ORDERS
# --------------------------------------------------

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

# --------------------------------------------------
# INCIDENTS
# --------------------------------------------------

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

# --------------------------------------------------
# ANALYTICS
# --------------------------------------------------

elif page == "Analytics":

    st.title("📊 Facility Analytics")

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
        df.set_index(
            "Severity"
        )
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "MTTR",
            "3.5 Hours"
        )

    with col2:

        st.metric(
            "SLA Compliance",
            "96%"
        )
