"""
Macro View: Preserving Corporate Registry Analytics and Public Sector / 7th CPC Pay Parity.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

SECTORS = {
    "Business Services": 533996, "Community, Personal & Social Services": 329483,
    "Trading (Wholesale & Retail)": 299016, "Construction & Civil Infrastructure": 160996,
    "Manufacturing (Metals & Chemicals)": 136025, "Real Estate & Commercial Renting": 106221,
    "Manufacturing (Machinery & Equipments)": 97003, "Agriculture & Allied Activities": 93335,
    "Transport, Storage & Communications": 89152, "Financial Intermediation & Banking": 81680,
    "Manufacturing (Food & Beverages)": 66642, "Manufacturing (Textiles & Apparel)": 45761,
    "Electricity, Gas & Water Utilities": 36653, "Manufacturing (Miscellaneous)": 28406,
    "Paper, Publishing & Media": 20872, "Mining & Mineral Quarrying": 16147,
    "Manufacturing (Leather)": 4579, "Manufacturing (Wood & Furniture)": 4396,
    "Insurance & Pension Funding": 1396, "Unclassified Corporate Operations": 3051
}

FIVE = {
    "Primary (extraction)": "Agriculture & Allied Activities|Mining & Mineral Quarrying",
    "Secondary (industry)": "Construction & Civil Infrastructure|Manufacturing (Metals & Chemicals)|Manufacturing (Machinery & Equipments)|Manufacturing (Food & Beverages)|Manufacturing (Textiles & Apparel)|Manufacturing (Miscellaneous)|Manufacturing (Leather)|Manufacturing (Wood & Furniture)|Electricity, Gas & Water Utilities|Paper, Publishing & Media",
    "Tertiary (services)": "Trading (Wholesale & Retail)|Transport, Storage & Communications|Financial Intermediation & Banking|Insurance & Pension Funding|Real Estate & Commercial Renting|Community, Personal & Social Services",
    "Quaternary (knowledge)": "Business Services",
    "Quinary (sovereign)": "Unclassified Corporate Operations"
}

STATES = {
    "Maharashtra": 401886, "Delhi": 274958, "Uttar Pradesh": 190342, "West Bengal": 158010,
    "Karnataka": 150806, "Tamil Nadu": 143958, "Telangana": 132010, "Gujarat": 121419
}

CPC = [
    (1,18000,56900,"Peon / MTS / Safaiwala"), (2,19900,63200,"LDC / DEO-A"),
    (3,21700,69100,"Postal Asst / CAPF Constable"), (4,25500,81100,"UDC / Head Constable"),
    (5,29200,92300,"Jr Accountant / Steno-I"), (6,35400,112400,"Sub-Inspector / PRT"),
    (7,44900,142400,"ASO / TGT"), (8,47600,151100,"AAO / PGT"),
    (9,53100,167800,"Under Secretary"), (10,56100,177500,"IAS / IPS entry"),
    (11,67700,208700,"Deputy Secretary / Exec Engineer"), (12,78800,209200,"Director (field)"),
    (13,123100,215900,"Director (Centre) / DIG"), (14,144200,218200,"Joint Secretary / IG Police"),
    (15,182200,224100,"Addl Secretary"), (16,205400,224400,"Special Secretary / DG"),
    (17,225000,225000,"Secretary to GoI"), (18,250000,250000,"Cabinet Secretary")
]


def render_macro_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(22,38,74,0.4), rgba(41,121,255,0.15)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">🌐 Macroeconomic Market & Public Pay Parity</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            National occupational registry distribution across 2.15M+ active MCA enterprises, economic sectors, and 7th CPC government pay parity.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["🏛️ Corporate Registry Structure", "⚖️ 7th CPC Public Sector Pay Matrix"])
    
    with t1:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Registered Companies", "31,92,605", "All-time")
        c2.metric("Active Companies", "21,54,810", "Operational")
        c3.metric("Struck-Off / Closed", "10,37,795", "MCA Registry")
        c4.metric("Top-8 States Share", "≈ 75%", "Geographic Concentration")
        
        st.write("")
        rows = [(s, k, v) for s, v in SECTORS.items() for k, names in FIVE.items() if s in names.split("|")]
        df = pd.DataFrame(rows, columns=["Activity", "Sector", "Active"])
        
        col_tree, col_pie = st.columns([1.2, 1])
        with col_tree:
            fig_tree = px.treemap(
                df, path=["Sector", "Activity"], values="Active",
                color="Active", color_continuous_scale=["#0D2A66", "#2979FF", "#00E676"],
                title="Active Enterprises by Sector Tier"
            )
            fig_tree.update_layout(template="plotly_dark", height=420, margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(fig_tree, use_container_width=True)
            
        with col_pie:
            g = df.groupby("Sector", as_index=False).Active.sum()
            fig_pie = px.pie(g, names="Sector", values="Active", hole=0.6, title="Share of National Registry",
                             color_discrete_sequence=["#2979FF", "#00E676", "#FFB300", "#B388FF", "#FF5252"])
            fig_pie.update_layout(template="plotly_dark", height=420, margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(fig_pie, use_container_width=True)
            
    with t2:
        st.markdown("### 🏛️ 7th Central Pay Commission Pay Matrix")
        cpc_df = pd.DataFrame(CPC, columns=["Pay Level", "Minimum Basic (₹)", "Maximum Basic (₹)", "Benchmark Post"])
        st.dataframe(cpc_df, hide_index=True, use_container_width=True)
