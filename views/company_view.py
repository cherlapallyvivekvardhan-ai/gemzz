"""
Company View: Wished Company Compensation Evaluation & Skill-Matched Company Leaderboard.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from engine.salary_calculator import evaluate_company_for_candidate, rank_companies_by_skill_match
from data.salary_data import get_company_names, get_company_tiers, COMPANIES_DATA


def render_company_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255,179,0,0.15), rgba(41,121,255,0.10)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">🏢 Company Salary Intelligence & Skill-Matching</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            Enter your wished company to inspect their expected compensation package and skill fit, or explore top-paying companies actively hiring for your tech stack.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Retrieve user profile from session state
    yoe = float(st.session_state.get("yoe", 3.5))
    role = st.session_state.get("role", "Software Engineer (Backend / Full Stack)")
    skills = st.session_state.get("skills", ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"])
    edu = st.session_state.get("edu", "Tier 1 (IIT / BITS / NIT / Top IIIT)")
    city = st.session_state.get("city", "Bengaluru")
    
    # User Profile Context Bar
    st.markdown(f"""
    <div style="background: rgba(22, 27, 34, 0.8); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 10px 16px; margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 18px; font-size: 0.9rem;">
        <div>👤 <b>Role:</b> {role}</div>
        <div>⏳ <b>Experience:</b> {yoe} Yrs</div>
        <div>📍 <b>Location:</b> {city}</div>
        <div>🛠️ <b>Current Skills:</b> {', '.join(skills[:5])}{' +more' if len(skills)>5 else ''}</div>
    </div>
    """, unsafe_allow_html=True)
    
    tab_wished, tab_matched = st.tabs([
        "🎯 Evaluate Your Wished Company",
        "🏆 Top-Paying Companies Matching Your Skills"
    ])
    
    # -------------------------------------------------------------------------
    # TAB 1: WISHED COMPANY EVALUATION
    # -------------------------------------------------------------------------
    with tab_wished:
        st.markdown("### 🔍 Select Your Target / Wished Company")
        
        all_companies = get_company_names()
        default_comp = st.session_state.get("wished_company", "Google")
        comp_index = all_companies.index(default_comp) if default_comp in all_companies else 0
        
        col_select, col_tier = st.columns([2, 1])
        with col_select:
            selected_comp = st.selectbox(
                "Choose or Search Wished Company",
                all_companies,
                index=comp_index
            )
            st.session_state["wished_company"] = selected_comp
            
        with col_tier:
            comp_tier_info = COMPANIES_DATA[selected_comp]["tier"]
            st.markdown(f"""
            <div style="background: rgba(22, 27, 34, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 14px; margin-top: 25px;">
                <div style="font-size: 0.75rem; color: #8B949E; text-transform: uppercase;">Employer Category</div>
                <div style="font-size: 0.95rem; font-weight: 600; color: #FFB300;">{comp_tier_info}</div>
            </div>
            """, unsafe_allow_html=True)
            
        # Run company evaluation
        comp_eval = evaluate_company_for_candidate(
            company_name=selected_comp,
            years_of_experience=yoe,
            role=role,
            selected_skills=skills,
            education_tier=edu,
            target_city=city
        )
        
        if comp_eval:
            st.write("")
            # Top metrics cards
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric("Total Expected CTC", f"₹{comp_eval['median_ctc_lakhs']:.1f} L", "Median Package")
            with c2:
                st.metric("Base Fixed Salary", f"₹{comp_eval['base_salary_lakhs']:.1f} L", "Cash Component")
            with c3:
                st.metric("Annual Stocks / RSUs", f"₹{comp_eval['stock_lakhs']:.1f} L", "Equity Vesting")
            with c4:
                st.metric("Skill Fit Match", f"{comp_eval['fit_score_pct']}%", f"{len(comp_eval['matched_skills'])} of {len(comp_eval['primary_stack'])} skills")
                
            col_chart, col_details = st.columns([1.2, 1], gap="medium")
            
            with col_chart:
                st.markdown("#### 📦 Compensation Package Breakdown")
                pkg_data = {
                    "Component": ["Base Salary", "Target Bonus", "RSUs / Stocks"],
                    "Amount (₹ L)": [comp_eval['base_salary_lakhs'], comp_eval['bonus_lakhs'], comp_eval['stock_lakhs']]
                }
                fig_pkg = px.bar(
                    pkg_data,
                    x="Component",
                    y="Amount (₹ L)",
                    color="Component",
                    color_discrete_sequence=["#2979FF", "#FFB300", "#00E676"],
                    text="Amount (₹ L)"
                )
                fig_pkg.update_traces(texttemplate='₹%{text:.1f} L', textposition='outside')
                fig_pkg.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    height=280,
                    margin=dict(l=10, r=10, t=20, b=10),
                    showlegend=False
                )
                st.plotly_chart(fig_pkg, use_container_width=True)
                
                st.markdown(f"""
                <div style="background: rgba(0, 230, 118, 0.08); border: 1px solid rgba(0, 230, 118, 0.25); border-radius: 10px; padding: 12px 16px;">
                    <div style="font-size: 0.85rem; color: #8B949E;">Estimated Monthly In-Hand (Take-Home) at {selected_comp}</div>
                    <div style="font-size: 1.5rem; font-weight: 700; color: #00E676;">
                        ₹{comp_eval['monthly_inhand_inr']:,.0f} <span style="font-size: 0.9rem; color: #F0F6FC; font-weight: 400;">/ month</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with col_details:
                st.markdown("#### 🎯 Skill Fit & Interview Bar")
                st.markdown(f"**Interview Bar:** `{comp_eval['hiring_bar']}`")
                st.markdown(f"**Difficulty Rating:** {'⭐' * int(round(comp_eval['interview_difficulty']))} ({comp_eval['interview_difficulty']}/5.0)")
                st.markdown(f"**India Office Hubs:** {', '.join(comp_eval['locations'])}")
                
                # Matched Skills
                st.markdown("**✅ Matched Tech Stack:**")
                if comp_eval["matched_skills"]:
                    st.markdown(" ".join([f"`{s}`" for s in comp_eval["matched_skills"]]))
                else:
                    st.caption("None of their core stack matched yet.")
                    
                # Missing Skills
                st.markdown("**⚠️ Missing Skills for this Company:**")
                if comp_eval["missing_skills"]:
                    st.markdown(" ".join([f"`{s}`" for s in comp_eval["missing_skills"]]))
                    st.caption("💡 Developing these missing skills significantly boosts your interview shortlisting probability.")
                else:
                    st.success("🎉 Outstanding! You have 100% of this company's core stack!")
                    
                st.info(f"**Ecosystem Summary:** {comp_eval['summary']}")
                
    # -------------------------------------------------------------------------
    # TAB 2: SKILL-MATCHED COMPANY LEADERBOARD
    # -------------------------------------------------------------------------
    with tab_matched:
        st.markdown("### 🏆 Top Paying Employers for Your Tech Stack")
        
        tier_filter_options = ["All Tiers"] + get_company_tiers()
        chosen_tier = st.selectbox("Filter by Employer Category", tier_filter_options)
        
        ranked_df = rank_companies_by_skill_match(
            years_of_experience=yoe,
            role=role,
            selected_skills=skills,
            education_tier=edu,
            target_city=city,
            filter_tier=chosen_tier
        )
        
        if not ranked_df.empty:
            # Top 15 visual bar chart
            top_display_df = ranked_df.head(12).sort_values(by="Expected CTC (₹ L)", ascending=True)
            
            fig_top = px.bar(
                top_display_df,
                x="Expected CTC (₹ L)",
                y="Company",
                orientation="h",
                color="Tier",
                color_discrete_sequence=["#2979FF", "#00E676", "#FFB300", "#B388FF", "#18FFFF"],
                text="Expected CTC (₹ L)",
                title="Top Employers by Projected Compensation (INR Lakhs)"
            )
            fig_top.update_traces(texttemplate='₹%{text:.1f} L', textposition='outside')
            fig_top.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=480,
                margin=dict(l=10, r=10, t=40, b=10),
                xaxis_title="Expected Total CTC (₹ Lakhs)",
                yaxis_title="",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_top, use_container_width=True)
            
            st.markdown("#### 📋 Full Company Matching Matrix")
            st.dataframe(
                ranked_df,
                hide_index=True,
                use_container_width=True
            )
        else:
            st.warning("No companies found for this filter criteria.")
