"""
SalaryScope India: AI-Powered Tech Salary Market Intelligence & Career Upskilling Engine.
"""

import sys
import os
import streamlit as st

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from views.calculator_view import render_calculator_view
from views.regional_view import render_regional_view
from views.company_view import render_company_view
from views.upskill_view import render_upskill_view
from views.macro_view import render_macro_view
from views.report_view import render_report_view

# Page Configuration
st.set_page_config(
    page_title="SalaryScope India | Tech Market Intelligence",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Dark UI CSS Styling
CSS = """
<style>
/* Global dark styling with modern gradients */
.stApp {
    background: radial-gradient(1200px 600px at 10% -10%, #16264a44, transparent),
                radial-gradient(900px 500px at 100% 0, #00e67614, transparent),
                #0B0E14;
    color: #F0F6FC;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: #0D1117;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

/* Header customization */
header[data-testid="stHeader"] {
    background: rgba(11, 14, 20, 0.8);
    backdrop-filter: blur(10px);
}

/* Metric card containers */
[data-testid="stMetric"] {
    background: rgba(22, 27, 34, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

/* Metric values */
[data-testid="stMetricValue"] {
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    color: #F0F6FC !important;
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    font-size: 0.8rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    color: #8B949E !important;
}

/* Buttons */
.stButton>button {
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease-in-out;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(41, 121, 255, 0.3);
}

/* Dataframe container */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    overflow: hidden;
}

/* Tabs styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0;
    padding: 10px 18px;
    background: rgba(22, 27, 34, 0.5);
    color: #8B949E;
}
.stTabs [aria-selected="true"] {
    background: rgba(41, 121, 255, 0.15) !important;
    color: #2979FF !important;
    border-bottom: 2px solid #2979FF !important;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def init_session_state():
    """Initializes default candidate profile parameters in session state."""
    if "yoe" not in st.session_state:
        st.session_state["yoe"] = 3.5
    if "role" not in st.session_state:
        st.session_state["role"] = "Software Engineer (Backend / Full Stack)"
    if "skills" not in st.session_state:
        st.session_state["skills"] = ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"]
    if "edu" not in st.session_state:
        st.session_state["edu"] = "Tier 1 (IIT / BITS / NIT / Top IIIT)"
    if "city" not in st.session_state:
        st.session_state["city"] = "Bengaluru"
    if "wished_company" not in st.session_state:
        st.session_state["wished_company"] = "Google"


def main():
    init_session_state()
    
    # Sidebar Branding
    st.sidebar.markdown("""
    <div style="padding: 10px 0 20px 0; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 15px;">
        <h2 style="margin: 0; font-size: 1.45rem; color: #2979FF; display: flex; align-items: center; gap: 8px;">
            🧭 SalaryScope
        </h2>
        <div style="font-size: 0.78rem; color: #00E676; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 600; margin-top: 4px;">
            India Tech Market Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    menu_options = [
        "🧭 1. Salary Predictor & Profile",
        "🗺️ 2. Regional Analysis (North vs South)",
        "🏢 3. Company & Wished Company Pay",
        "🚀 4. Upskill ROI & Salary Booster",
        "🌐 5. Macro Economy & Registry",
        "📄 6. Career Strategy & Export"
    ]
    
    selected_page = st.sidebar.radio(
        "Navigation",
        menu_options,
        index=0,
        label_visibility="collapsed"
    )
    
    # Sidebar quick profile view
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### ⚡ Active Profile Snapshot")
    st.sidebar.markdown(f"""
    <div style="background: rgba(22, 27, 34, 0.7); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 12px; font-size: 0.85rem;">
        <div>⏳ <b>Experience:</b> {st.session_state['yoe']} Yrs</div>
        <div style="margin-top: 4px;">👤 <b>Role:</b> {st.session_state['role'][:22]}...</div>
        <div style="margin-top: 4px;">📍 <b>Hub:</b> {st.session_state['city']}</div>
        <div style="margin-top: 4px;">🛠️ <b>Skills:</b> {len(st.session_state['skills'])} active</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.caption("Data calibrated to 2025–2026 Indian Tech Compensation Benchmarks · 55+ Employers · 8 Tech Hubs")
    
    # Page Router
    if selected_page == "🧭 1. Salary Predictor & Profile":
        render_calculator_view()
    elif selected_page == "🗺️ 2. Regional Analysis (North vs South)":
        render_regional_view()
    elif selected_page == "🏢 3. Company & Wished Company Pay":
        render_company_view()
    elif selected_page == "🚀 4. Upskill ROI & Salary Booster":
        render_upskill_view()
    elif selected_page == "🌐 5. Macro Economy & Registry":
        render_macro_view()
    elif selected_page == "📄 6. Career Strategy & Export":
        render_report_view()


if __name__ == "__main__":
    main()
