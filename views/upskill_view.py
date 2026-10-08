"""
Upskill View: High-ROI Skill Recommendations, Salary Multipliers, and What-If Simulator.
Suggests skills to develop to increase salary across target companies and regions.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from engine.salary_calculator import recommend_upskilling_path, calculate_candidate_salary
from data.skills_data import SKILLS_DATA


def render_upskill_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(179,136,255,0.15), rgba(0,230,118,0.10)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">🚀 Upskilling ROI & Salary Growth Booster</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            Discover which skills offer the highest monetary return on your learning investment, which top companies will pay for them, and which geographic areas have peak demand.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Retrieve user profile from session state
    yoe = float(st.session_state.get("yoe", 3.5))
    role = st.session_state.get("role", "Software Engineer (Backend / Full Stack)")
    skills = st.session_state.get("skills", ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"])
    edu = st.session_state.get("edu", "Tier 1 (IIT / BITS / NIT / Top IIIT)")
    city = st.session_state.get("city", "Bengaluru")
    wished_comp = st.session_state.get("wished_company", None)
    
    # User Profile Context Bar
    st.markdown(f"""
    <div style="background: rgba(22, 27, 34, 0.8); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 16px; margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 18px; font-size: 0.9rem;">
        <div>👤 <b>Role:</b> {role}</div>
        <div>⏳ <b>Experience:</b> {yoe} Yrs</div>
        <div>📍 <b>Location:</b> {city}</div>
        <div>🛠️ <b>Current Stack ({len(skills)}):</b> {', '.join(skills[:5])}{' +more' if len(skills)>5 else ''}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Run recommendation algorithm
    recs_df, current_ctc = recommend_upskilling_path(
        years_of_experience=yoe,
        role=role,
        current_skills=skills,
        education_tier=edu,
        target_city=city,
        target_company=wished_comp
    )
    
    tab_rec, tab_sim = st.tabs([
        "💡 Top High-ROI Skills to Learn Next",
        "🔮 Interactive 'What-If' Upskill Simulator"
    ])
    
    # -------------------------------------------------------------------------
    # TAB 1: HIGH-ROI SKILL RECOMMENDATIONS
    # -------------------------------------------------------------------------
    with tab_rec:
        st.markdown(f"### 📈 Projected Salary Gains from High-Impact Skills (Current Baseline: ₹{current_ctc:.1f} L)")
        
        if not recs_df.empty:
            # Pareto Bar Chart of Top Skills
            top_skills_chart = recs_df.head(10).sort_values(by="Salary Boost (₹ L)", ascending=True)
            
            fig_boost = px.bar(
                top_skills_chart,
                x="Salary Boost (₹ L)",
                y="Skill",
                orientation="h",
                color="Salary Boost (₹ L)",
                color_continuous_scale=["#2979FF", "#00E676"],
                text="Salary Boost (₹ L)",
                hover_data=["Hike (%)", "Target Companies", "Best Regions", "Est. Weeks"],
                title="Incremental Annual Salary Hike by Skill (₹ Lakhs)"
            )
            fig_boost.update_traces(texttemplate='+₹%{text:.1f} L', textposition='outside')
            fig_boost.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=380,
                margin=dict(l=10, r=10, t=40, b=10),
                xaxis_title="Additional CTC Gain (₹ Lakhs / Year)",
                yaxis_title=""
            )
            st.plotly_chart(fig_boost, use_container_width=True)
            
            # Detailed Recommendation Cards for Top 4 Skills
            st.markdown("#### 🎯 Priority Upskilling Action Roadmap")
            
            top_4 = recs_df.head(4).to_dict("records")
            card_cols = st.columns(2)
            
            for idx, item in enumerate(top_4):
                col = card_cols[idx % 2]
                with col:
                    st.markdown(f"""
                    <div style="background: rgba(22, 27, 34, 0.9); border: 1px solid rgba(0,230,118,0.25); border-radius: 14px; padding: 18px; margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">{item['Skill']}</span>
                            <span style="background: rgba(0,230,118,0.18); color: #00E676; padding: 4px 10px; border-radius: 8px; font-weight: 700; font-size: 0.95rem;">
                                +₹{item['Salary Boost (₹ L)']:.1f} L (+{item['Hike (%)']}%)
                            </span>
                        </div>
                        <p style="font-size: 0.85rem; color: #8B949E; margin: 4px 0 10px 0;">{item['Description']}</p>
                        <div style="font-size: 0.85rem; margin-bottom: 6px;">
                            <span style="color: #FFB300;">🏢 Target Companies:</span> <b>{item['Target Companies']}</b>
                        </div>
                        <div style="font-size: 0.85rem; margin-bottom: 6px;">
                            <span style="color: #2979FF;">📍 Peak Demand Regions:</span> <b>{item['Best Regions']}</b>
                        </div>
                        <div style="font-size: 0.82rem; color: #8B949E; display: flex; gap: 14px; margin-top: 8px;">
                            <span>⏱️ <b>Time to Learn:</b> ~{item['Est. Weeks']} Weeks</span>
                            <span>⚡ <b>Difficulty:</b> {item['Difficulty']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            st.markdown("#### 📋 Full Skills Market Opportunity Catalog")
            st.dataframe(
                recs_df[[
                    "Skill", "Category", "Salary Boost (₹ L)", "Hike (%)",
                    "New Projected CTC (₹ L)", "Target Companies", "Best Regions", "Est. Weeks", "Difficulty"
                ]],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.success("🎉 You have mastered all major skills in our database! You are at maximum market leverage.")
            
    # -------------------------------------------------------------------------
    # TAB 2: INTERACTIVE "WHAT-IF" SIMULATOR
    # -------------------------------------------------------------------------
    with tab_sim:
        st.markdown("### 🔮 Simulate Future Salary by Adding Skills")
        st.markdown("Select 1 to 3 new skills you plan to learn and observe the immediate projected hike in your market compensation.")
        
        missing_skills_pool = [s for s in SKILLS_DATA.keys() if s not in skills]
        
        sim_selected = st.multiselect(
            "Choose Skills to Add to Your Repertoire",
            missing_skills_pool,
            default=[missing_skills_pool[0], missing_skills_pool[1]] if len(missing_skills_pool) >= 2 else missing_skills_pool[:1],
            max_selections=4
        )
        
        if sim_selected:
            simulated_full_skills = skills + sim_selected
            
            # Recalculate salary with simulated skills
            current_eval = calculate_candidate_salary(
                years_of_experience=yoe,
                role=role,
                selected_skills=skills,
                education_tier=edu,
                target_city=city,
                target_company=wished_comp
            )
            
            sim_eval = calculate_candidate_salary(
                years_of_experience=yoe,
                role=role,
                selected_skills=simulated_full_skills,
                education_tier=edu,
                target_city=city,
                target_company=wished_comp
            )
            
            delta_ctc = sim_eval["median_lakhs"] - current_eval["median_lakhs"]
            delta_pct = (delta_ctc / current_eval["median_lakhs"] * 100) if current_eval["median_lakhs"] > 0 else 0.0
            delta_inhand = sim_eval["monthly_inhand_inr"] - current_eval["monthly_inhand_inr"]
            
            st.write("")
            s1, s2, s3, s4 = st.columns(4)
            with s1:
                st.metric("Current Baseline CTC", f"₹{current_eval['median_lakhs']:.1f} L")
            with s2:
                st.metric("Projected New CTC", f"₹{sim_eval['median_lakhs']:.1f} L", f"+₹{delta_ctc:.1f} L (+{delta_pct:.1f}%)")
            with s3:
                st.metric("Top 10% Outlier Ceiling", f"₹{sim_eval['p90_lakhs']:.1f} L", "Tier 1 Product")
            with s4:
                st.metric("Extra In-Hand / Month", f"+₹{delta_inhand:,.0f}", "Monthly Take-Home Jump")
                
            # Comparison Bar Chart
            comp_fig_df = {
                "Profile Stage": ["Current Stack", f"With +{', '.join(sim_selected[:2])}"],
                "Median CTC (₹ L)": [current_eval["median_lakhs"], sim_eval["median_lakhs"]],
                "Fixed Base (₹ L)": [current_eval["base_salary_lakhs"], sim_eval["base_salary_lakhs"]],
                "Stocks / Equity (₹ L)": [current_eval["stock_lakhs"], sim_eval["stock_lakhs"]]
            }
            
            fig_delta = go.Figure()
            fig_delta.add_trace(go.Bar(
                x=comp_fig_df["Profile Stage"],
                y=comp_fig_df["Fixed Base (₹ L)"],
                name="Base Salary",
                marker_color="#2979FF"
            ))
            fig_delta.add_trace(go.Bar(
                x=comp_fig_df["Profile Stage"],
                y=comp_fig_df["Stocks / Equity (₹ L)"],
                name="Stocks / RSUs",
                marker_color="#00E676"
            ))
            fig_delta.update_layout(
                barmode="stack",
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=320,
                margin=dict(l=10, r=10, t=30, b=10),
                yaxis_title="Annual Compensation (₹ Lakhs)",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_delta, use_container_width=True)
            
            st.success(f"🚀 **Upskilling Outcome**: Adding **{', '.join(sim_selected)}** increases your estimated annual CTC by **₹{delta_ctc:.1f} Lakhs**, yielding an extra **₹{delta_inhand:,.0f} every single month** into your bank account!")
        else:
            st.info("Pick at least one skill from the dropdown above to simulate.")
