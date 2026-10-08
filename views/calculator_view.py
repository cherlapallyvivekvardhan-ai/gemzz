"""
Calculator View: Interactive Profile Input, Dynamic CTC Estimator, and Salary Progression.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from engine.salary_calculator import calculate_candidate_salary
from data.salary_data import ROLE_EXPERIENCE_CURVES, EDUCATION_TIERS, COMPANIES_DATA
from data.skills_data import SKILLS_DATA, get_skills_by_category


def render_calculator_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(41,121,255,0.15), rgba(0,230,118,0.10)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">🧭 Tech Salary Predictor & Profile Benchmark</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            Enter your experience, core tech skills, and target parameters to generate real-time compensation benchmarks calibrated to the 2025-2026 Indian tech market.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_input, col_output = st.columns([1.1, 1.4], gap="large")
    
    with col_input:
        st.markdown("### 📋 Candidate Profile")
        
        # 1. Experience
        yoe = st.slider(
            "Years of Professional Experience",
            min_value=0.0,
            max_value=20.0,
            value=float(st.session_state.get("yoe", 3.5)),
            step=0.5,
            help="Total relevant years of full-time technical experience."
        )
        st.session_state["yoe"] = yoe
        
        # Experience level badge
        if yoe < 2:
            level_label = "🌱 SDE 1 / Junior (Entry Level)"
        elif yoe < 5:
            level_label = "⚡ SDE 2 / Mid-Level Specialist"
        elif yoe < 8:
            level_label = "🔥 SDE 3 / Senior Engineer"
        elif yoe < 12:
            level_label = "🏆 Staff / Lead Engineer"
        else:
            level_label = "👑 Principal / Engineering Leader"
        st.caption(f"**Level Stratum:** {level_label}")
        
        # 2. Primary Domain Role
        role_options = list(ROLE_EXPERIENCE_CURVES.keys())
        default_role_idx = role_options.index(st.session_state.get("role", "Software Engineer (Backend / Full Stack)")) if st.session_state.get("role") in role_options else 0
        role = st.selectbox(
            "Primary Domain / Target Role",
            role_options,
            index=default_role_idx
        )
        st.session_state["role"] = role
        
        # 3. Education Pedigree
        edu_options = list(EDUCATION_TIERS.keys())
        edu = st.selectbox(
            "Education Pedigree",
            edu_options,
            index=edu_options.index(st.session_state.get("edu", edu_options[0])) if st.session_state.get("edu") in edu_options else 0
        )
        st.session_state["edu"] = edu
        
        # 4. Preferred City / Tech Hub
        city_options = ["Bengaluru", "Hyderabad", "Delhi-NCR (Gurgaon)", "Delhi-NCR (Noida)", "Mumbai", "Pune", "Chennai", "Kolkata", "Remote / Pan-India"]
        city = st.selectbox(
            "Primary Location / Tech Hub",
            city_options,
            index=city_options.index(st.session_state.get("city", "Bengaluru")) if st.session_state.get("city") in city_options else 0
        )
        st.session_state["city"] = city
        
        # 5. Skills Selection
        st.markdown("#### 🛠️ Tech Skills Stack")
        skills_by_cat = get_skills_by_category()
        
        # Predefined default skills if not in session state
        default_skills = st.session_state.get("skills", ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"])
        
        all_skills_flat = sorted(list(SKILLS_DATA.keys()))
        selected_skills = st.multiselect(
            "Select Your Active Skills (or search skills)",
            all_skills_flat,
            default=default_skills,
            help="Select the skills you actively use or can clear technical interviews in."
        )
        st.session_state["skills"] = selected_skills
        
        st.info(f"✨ **{len(selected_skills)} skills selected**. High-impact skills unlock premium tiers!")
        
    with col_output:
        st.markdown("### 💰 Compensation Benchmark")
        
        # Compute salary
        res = calculate_candidate_salary(
            years_of_experience=yoe,
            role=role,
            selected_skills=selected_skills,
            education_tier=edu,
            target_city=city
        )
        
        # Metric Cards Row
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(
                label="Median CTC",
                value=f"₹{res['median_lakhs']:.1f} L",
                delta=f"+{res['skill_boost_applied_pct']}% skill boost"
            )
        with m2:
            st.metric(
                label="Market Band (25th-75th)",
                value=f"₹{res['p25_lakhs']:.1f} - {res['p75_lakhs']:.1f} L",
                help="Typical offer band depending on negotiation and company tier."
            )
        with m3:
            st.metric(
                label="Top 10% Outlier CTC",
                value=f"₹{res['p90_lakhs']:.1f} L",
                delta="Tier 1 Product / Quant",
                delta_color="normal"
            )
            
        st.markdown(f"""
        <div style="background: rgba(22, 27, 34, 0.7); border: 1px solid rgba(0, 230, 118, 0.3); border-radius: 12px; padding: 14px 18px; margin: 12px 0;">
            <div style="font-size: 0.85rem; color: #8B949E; text-transform: uppercase; letter-spacing: 0.05em;">Estimated Monthly Take-Home (In-Hand Post-Tax)</div>
            <div style="font-size: 1.8rem; font-weight: 700; color: #00E676; margin-top: 2px;">
                ₹{res['monthly_inhand_inr']:,.0f} <span style="font-size: 1rem; color: #F0F6FC; font-weight: 400;">/ month</span>
            </div>
            <div style="font-size: 0.8rem; color: #8B949E; margin-top: 4px;">
                Calculated under New Tax Regime FY26 (Section 115BAC) · Annual In-Hand: ₹{res['annual_inhand_lakhs']:.2f} L · Effective Tax: {res['effective_tax_pct']}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # CTC Component Breakdown (Donut Chart)
        st.markdown("#### 🧩 CTC Package Breakdown")
        breakdown_df = {
            "Component": ["Base Salary (Fixed)", "Performance Bonus", "Stocks / RSUs (Annualized)"],
            "Amount (₹ L)": [res["base_salary_lakhs"], res["bonus_lakhs"], res["stock_lakhs"]]
        }
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=breakdown_df["Component"],
            values=breakdown_df["Amount (₹ L)"],
            hole=0.55,
            marker=dict(colors=["#2979FF", "#FFB300", "#00E676"]),
            textinfo="label+percent",
            hoverinfo="label+value"
        )])
        fig_donut.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=260,
            margin=dict(l=10, r=10, t=20, b=10),
            showlegend=False
        )
        st.plotly_chart(fig_donut, use_container_width=True)
        
    st.markdown("---")
    
    # Career Progression Trajectory (0 to 15 years curve)
    st.markdown("### 📈 Long-Term Career Compensation Trajectory (0 - 15 Years)")
    years_range = [0, 1, 2, 3, 5, 7, 10, 12, 15]
    trajectory_data = []
    for yr in years_range:
        sim = calculate_candidate_salary(
            years_of_experience=yr,
            role=role,
            selected_skills=selected_skills,
            education_tier=edu,
            target_city=city
        )
        trajectory_data.append({
            "Experience (Years)": yr,
            "Median CTC (₹ L)": sim["median_lakhs"],
            "25th Percentile": sim["p25_lakhs"],
            "75th Percentile": sim["p75_lakhs"],
            "Top 10% Outlier": sim["p90_lakhs"]
        })
        
    import pandas as pd
    traj_df = pd.DataFrame(trajectory_data)
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=traj_df["Experience (Years)"],
        y=traj_df["Top 10% Outlier"],
        name="Top 10% Outlier (Tier 1 Product)",
        line=dict(color="#00E676", width=2, dash="dash")
    ))
    fig_line.add_trace(go.Scatter(
        x=traj_df["Experience (Years)"],
        y=traj_df["75th Percentile"],
        name="75th Percentile (Upper Market)",
        line=dict(color="#2979FF", width=2)
    ))
    fig_line.add_trace(go.Scatter(
        x=traj_df["Experience (Years)"],
        y=traj_df["Median CTC (₹ L)"],
        name="Median Expected CTC",
        line=dict(color="#FFB300", width=3),
        fill='tonexty',
        fillcolor='rgba(41, 121, 255, 0.1)'
    ))
    fig_line.add_trace(go.Scatter(
        x=traj_df["Experience (Years)"],
        y=traj_df["25th Percentile"],
        name="25th Percentile (Floor)",
        line=dict(color="#8B949E", width=1.5)
    ))
    
    fig_line.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="Years of Experience",
        yaxis_title="Annual CTC (₹ Lakhs)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_line, use_container_width=True)
