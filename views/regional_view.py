"""
Regional View: Deep-Dive Geographic Salary Intelligence (North vs. South vs. West vs. East).
Suggests regions where compensation is highest and analyzes real purchasing power.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from engine.salary_calculator import get_regional_salary_comparison
from data.salary_data import REGIONS_DATA


def render_regional_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(41,121,255,0.10)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">🗺️ Regional Salary Intelligence: North vs. South vs. West vs. East</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            Comparative analysis showing where salaries are highest across Indian tech hubs for your specific experience and skill stack, with Cost of Living and Real Savings adjustments.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Retrieve user profile from session state
    yoe = float(st.session_state.get("yoe", 3.5))
    role = st.session_state.get("role", "Software Engineer (Backend / Full Stack)")
    skills = st.session_state.get("skills", ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"])
    edu = st.session_state.get("edu", "Tier 1 (IIT / BITS / NIT / Top IIIT)")
    
    # User Profile Context Bar
    st.markdown(f"""
    <div style="background: rgba(22, 27, 34, 0.8); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 16px; margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 18px; font-size: 0.9rem;">
        <div>👤 <b>Role:</b> {role}</div>
        <div>⏳ <b>Experience:</b> {yoe} Yrs</div>
        <div>🛠️ <b>Skills Analyzed:</b> {', '.join(skills[:5])}{' +more' if len(skills)>5 else ''}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Run regional analysis
    data = get_regional_salary_comparison(
        years_of_experience=yoe,
        role=role,
        selected_skills=skills,
        education_tier=edu
    )
    
    cities_df = data["cities_df"]
    summary_df = data["region_summary_df"]
    
    # Top Highlight Banners
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background: rgba(41, 121, 255, 0.12); border-left: 4px solid #2979FF; border-radius: 10px; padding: 16px; height: 100%;">
            <div style="font-size: 0.8rem; color: #8B949E; text-transform: uppercase; font-weight: 600;">🏆 Highest Gross Paying Tech Hub</div>
            <div style="font-size: 1.6rem; font-weight: 700; color: #2979FF; margin: 4px 0;">{data['highest_paying_city']} ({data['highest_paying_region']} Region)</div>
            <div style="font-size: 0.95rem; color: #F0F6FC;">
                Median Offer CTC: <b>₹{data['highest_ctc_lakhs']:.2f} Lakhs</b> · Prime center for VC-funded startups & FAANG+ labs.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div style="background: rgba(0, 230, 118, 0.12); border-left: 4px solid #00E676; border-radius: 10px; padding: 16px; height: 100%;">
            <div style="font-size: 0.8rem; color: #8B949E; text-transform: uppercase; font-weight: 600;">💰 Highest Real Wealth Accumulator</div>
            <div style="font-size: 1.6rem; font-weight: 700; color: #00E676; margin: 4px 0;">{data['best_savings_city']}</div>
            <div style="font-size: 0.95rem; color: #F0F6FC;">
                Est. Annual Real Savings: <b>₹{data['best_savings_lakhs']:.2f} Lakhs</b> · Optimal blend of strong compensation and moderate rent.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    
    # Regional Comparison Tabs
    tab_overview, tab_purchasing, tab_hubs = st.tabs([
        "📊 Nominal CTC by City & Zone",
        "💵 Cost of Living & Real Savings",
        "🏙️ Regional Tech Ecosystem Specializations"
    ])
    
    with tab_overview:
        st.markdown("### 🌆 Tech Hub CTC Comparison (North vs. South vs. West vs. East)")
        
        # Color mapping by region
        color_map = {
            "South": "#2979FF",
            "North": "#00E676",
            "West": "#FFB300",
            "East": "#B388FF",
            "Remote": "#18FFFF"
        }
        
        fig_bar = px.bar(
            cities_df,
            x="City",
            y="Median CTC (₹ L)",
            color="Region",
            color_discrete_map=color_map,
            text="Median CTC (₹ L)",
            title=f"Expected Annual CTC by City for {yoe} Yrs Experience",
            hover_data=["Display Name", "25th-75th Band (₹ L)", "Demand Heat", "Top Specialty"]
        )
        fig_bar.update_traces(texttemplate='₹%{text:.1f}L', textposition='outside')
        fig_bar.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=420,
            margin=dict(l=10, r=10, t=50, b=10),
            yaxis_title="Median CTC (₹ Lakhs)",
            xaxis_title="",
            legend_title="Geographic Zone"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Regional macro summary table
        st.markdown("#### 🧭 Macro Regional Aggregates")
        st.dataframe(
            summary_df.rename(columns={
                "Region": "Geographic Region",
                "Avg_CTC_Lakhs": "Average Median CTC (₹ L)",
                "Max_CTC_Lakhs": "Top Hub CTC (₹ L)",
                "Avg_Savings_Lakhs": "Avg Real Annual Savings (₹ L)",
                "Avg_COLI": "Avg Cost of Living Index"
            }),
            hide_index=True,
            use_container_width=True
        )
        
    with tab_purchasing:
        st.markdown("### ⚖️ The Real Wealth Reality: CTC vs. Living Costs & Savings")
        st.info("💡 **Key Market Insight**: High nominal CTC does not automatically translate to highest wealth. High rents in Mumbai, Bengaluru, and Gurgaon can significantly diminish disposable savings compared to Hyderabad, Pune, or Remote setups.")
        
        # Grouped Bar: CTC vs Annual Savings
        savings_chart_df = cities_df.sort_values(by="Est. Annual Real Savings (₹ L)", ascending=False)
        
        fig_compare = go.Figure()
        fig_compare.add_trace(go.Bar(
            x=savings_chart_df["City"],
            y=savings_chart_df["Median CTC (₹ L)"],
            name="Nominal Gross CTC (₹ L)",
            marker_color="#2979FF"
        ))
        fig_compare.add_trace(go.Bar(
            x=savings_chart_df["City"],
            y=savings_chart_df["Est. Annual Real Savings (₹ L)"],
            name="Real Net Annual Savings (₹ L)",
            marker_color="#00E676"
        ))
        fig_compare.update_layout(
            barmode="group",
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            yaxis_title="Amount in ₹ Lakhs",
            xaxis_title="",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_compare, use_container_width=True)
        
        st.markdown("#### 📋 Detailed Regional Living & Salary Index")
        st.dataframe(
            cities_df[[
                "Region", "City", "Median CTC (₹ L)", "Monthly In-Hand (₹)",
                "Cost of Living Index", "Monthly Rent Est. (₹)", "Est. Annual Real Savings (₹ L)", "Demand Heat"
            ]],
            hide_index=True,
            use_container_width=True
        )
        
    with tab_hubs:
        st.markdown("### 🗺️ Ecosystem Hotspots & Industry Dominance")
        
        for reg_name, reg_info in REGIONS_DATA.items():
            with st.expander(f"📍 {reg_name} Region — {reg_info['description']}", expanded=(reg_name in ["South", "North"])):
                st.markdown(f"**Dominant Tech Sectors:** {', '.join(reg_info['dominant_sectors'])}")
                st.markdown(f"**Key Cities:** {', '.join(reg_info['key_hubs'])}")
                
                cols = st.columns(len(reg_info["cities"]))
                for col, (c_name, c_data) in zip(cols, reg_info["cities"].items()):
                    with col:
                        st.markdown(f"""
                        <div style="background: rgba(22, 27, 34, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 14px;">
                            <div style="font-weight: 700; color: #F0F6FC; font-size: 1.05rem;">{c_name}</div>
                            <div style="font-size: 0.8rem; color: #FFB300; margin: 4px 0;">{c_data['demand_heat']}</div>
                            <p style="font-size: 0.85rem; color: #8B949E; margin-bottom: 6px;"><b>Specialty:</b> {c_data['specialty']}</p>
                            <div style="font-size: 0.8rem; color: #2979FF;"><b>Top Employers:</b><br>{', '.join(c_data['top_employers'][:4])}</div>
                        </div>
                        """, unsafe_allow_html=True)
