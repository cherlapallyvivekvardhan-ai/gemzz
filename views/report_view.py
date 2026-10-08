"""
Report View: Career Dossier, Negotiation Playbook, and Exportable Salary Report.
"""

import streamlit as st
import pandas as pd
from engine.salary_calculator import calculate_candidate_salary, get_regional_salary_comparison, rank_companies_by_skill_match, recommend_upskilling_path


def render_report_view():
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(41,121,255,0.15), rgba(179,136,255,0.12)); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.12); margin-bottom: 24px;">
        <h2 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #F0F6FC;">📄 Career Strategy Dossier & Report Export</h2>
        <p style="margin: 0; color: #8B949E; font-size: 0.95rem;">
            Consolidated intelligence summary of your market value, regional standing, company targets, and negotiation strategy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Retrieve user profile from session state
    yoe = float(st.session_state.get("yoe", 3.5))
    role = st.session_state.get("role", "Software Engineer (Backend / Full Stack)")
    skills = st.session_state.get("skills", ["Python", "SQL & Relational Databases", "Docker", "AWS (Amazon Web Services)"])
    edu = st.session_state.get("edu", "Tier 1 (IIT / BITS / NIT / Top IIIT)")
    city = st.session_state.get("city", "Bengaluru")
    wished_comp = st.session_state.get("wished_company", "Google")
    
    # Run full analyses
    cand_sal = calculate_candidate_salary(yoe, role, skills, edu, city, wished_comp)
    reg_sal = get_regional_salary_comparison(yoe, role, skills, edu, wished_comp)
    comp_rank = rank_companies_by_skill_match(yoe, role, skills, edu, city)
    upskill_df, _ = recommend_upskilling_path(yoe, role, skills, edu, city)
    
    st.markdown("### 📋 Executive Career Profile Summary")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Expected CTC", f"₹{cand_sal['median_lakhs']:.1f} L", f"{city}")
    with c2:
        st.metric("Highest Paying Hub", f"{reg_sal['highest_paying_city']}", f"₹{reg_sal['highest_ctc_lakhs']:.1f} L")
    with c3:
        st.metric("Best Savings Hub", f"{reg_sal['best_savings_city']}", f"₹{reg_sal['best_savings_lakhs']:.1f} L / yr")
    with c4:
        top_skill_rec = upskill_df.iloc[0]["Skill"] if not upskill_df.empty else "N/A"
        st.metric("Top Recommended Skill", f"{top_skill_rec}", f"+₹{upskill_df.iloc[0]['Salary Boost (₹ L)']:.1f} L" if not upskill_df.empty else "")
        
    st.markdown("---")
    
    st.markdown("### 🎯 Strategic Career Recommendations")
    
    r1, r2 = st.columns(2)
    with r1:
        st.markdown(f"""
        <div style="background: rgba(22, 27, 34, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 18px;">
            <h4 style="margin: 0 0 10px 0; color: #2979FF;">📍 Geographic Mobility Strategy</h4>
            <ul style="color: #F0F6FC; font-size: 0.9rem; line-height: 1.6; margin: 0; padding-left: 20px;">
                <li><b>South Region (Bengaluru & Hyderabad):</b> Commands the highest nominal CTC for {role}. Relocating here offers max networking and Tier 1 product exits.</li>
                <li><b>Real Wealth Maximizer:</b> If your focus is max bank balance accumulation, <b>{reg_sal['best_savings_city']}</b> offers the highest disposable savings ratio after rent and expenses.</li>
                <li><b>North Region (Gurgaon):</b> Top choice for consumer high-scale startups (Zomato, Blinkit, MakeMyTrip).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown(f"""
        <div style="background: rgba(22, 27, 34, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 18px;">
            <h4 style="margin: 0 0 10px 0; color: #00E676;">💼 Negotiation & Offer Optimization</h4>
            <ul style="color: #F0F6FC; font-size: 0.9rem; line-height: 1.6; margin: 0; padding-left: 20px;">
                <li><b>Equity Component:</b> At senior levels (5+ Yrs), request RSUs over fixed cash. Big Tech & Unicorn RSUs provide substantial appreciation upside.</li>
                <li><b>Competing Leverage:</b> Always hold simultaneous offers from at least 1 GCC and 1 Product Unicorn to trigger counter-bid escalations.</li>
                <li><b>Tax Efficiency:</b> Utilize Section 115BAC (New Tax Regime) with zero tax up to ₹12.75L salaried income for smart tax savings.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    
    # Downloadable CSV Data
    st.markdown("### 📥 Export Your Career Data & Analysis")
    
    # Create consolidated summary dataframe
    export_cities = reg_sal["cities_df"][["Region", "City", "Median CTC (₹ L)", "Monthly In-Hand (₹)", "Est. Annual Real Savings (₹ L)", "Demand Heat"]]
    csv_bytes = export_cities.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Regional Salary Report (CSV)",
        data=csv_bytes,
        file_name=f"salary_intelligence_regional_report_{int(yoe)}yoe.csv",
        mime="text/csv",
        help="Download city-by-city salary and purchasing power benchmarks as CSV."
    )
