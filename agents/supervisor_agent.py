import os
import sys
import streamlit as st
import pandas as pd

# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# --------------------------------------------------
# IMPORTS
# --------------------------------------------------

from rag.uploader import process_pdf
from agents.supervisor_agent import supervisor_agent

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="FM AI Enterprise",
    page_icon="🏢",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
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

    try:

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

    except Exception as e:

        st.sidebar.error(
            f"Upload Error: {str(e)}"
        )

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Dashboard",
        "AI Assistant",
        "Assets",
        "Work Orders",
        "Incidents",
        "Analytics"
    ]
)

# --------------------------------------------------
# EXECUTIVE DASHBOARD
# --------------------------------------------------

if page == "Executive Dashboard":

    st.title(
        "🏢 Executive Dashboard"
    )

    try:
        import frontend.executive_dashboard
    except:
        st.warning(
            "Executive dashboard module not found."
        )

# --------------------------------------------------
# AI ASSISTANT
# --------------------------------------------------

elif page == "AI Assistant":

    st.title(
        "🤖 FM AI Enterprise Assistant"
    )

    query = st.chat_input(
        "Ask about HVAC, Electrical, Fire, Vendor, Incident..."
    )

    if query:

        try:

            result = supervisor_agent(
                query
            )

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

        except Exception as e:

            st.error(
                f"Agent Error: {str(e)}"
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

                if isinstance(
                    result,
                    dict
                ):

                    st.subheader(
                        result.get(
                            "agent",
                            "AI Assistant"
                        )
                    )

                    st.write(
                        result.get(
                            "answer",
                            "No answer available."
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
                                f"📄 {source.get('file','Unknown')} | "
                                f"Page {source.get('page','N/A')}"
                            )

                else:

                    st.write(
                        str(result)
                    )

# --------------------------------------------------
# ASSETS
# --------------------------------------------------

elif page == "Assets":

    st.title(
        "🏭 Asset Management"
    )

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

    st.title(
        "📋 Work Order Dashboard"
    )

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

    st.title(
        "🚨 Incident Dashboard"
    )

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

    st.title(
        "📊 Facility Analytics"
    )

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
