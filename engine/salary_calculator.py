"""
Salary Computation, Regional Analysis, Company Benchmarking, and Upskilling ROI Engine.
"""

import math
import numpy as np
import pandas as pd
from data.skills_data import SKILLS_DATA
from data.salary_data import REGIONS_DATA, COMPANIES_DATA, ROLE_EXPERIENCE_CURVES, EDUCATION_TIERS


# ==============================================================================
# TAX & IN-HAND CALCULATOR (NEW TAX REGIME 115BAC FY 2025-26)
# ==============================================================================
def calculate_inhand_monthly(gross_annual_ctc_inr):
    """
    Computes estimated monthly in-hand take-home salary after standard deductions,
    EPF, and Income Tax under New Tax Regime (Section 115BAC).
    """
    # Exclude non-cash components (assume 15% average is stocks/retention/PF employer)
    cash_gross = gross_annual_ctc_inr * 0.88
    
    # Standard deduction of ₹75,000 for salaried employees
    taxable_income = max(0.0, cash_gross - 75000)
    
    # New Tax Regime Slabs
    # Upto ₹4,00,000: Nil
    # ₹4,00,001 - ₹8,00,000: 5%
    # ₹8,00,001 - ₹12,00,000: 10%
    # ₹12,00,001 - ₹16,00,000: 15%
    # ₹16,00,001 - ₹20,00,000: 20%
    # ₹20,00,001 - ₹24,00,000: 25%
    # Above ₹24,00,000: 30%
    slabs = [
        (400000, 0.0),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float('inf'), 0.30)
    ]
    
    tax = 0.0
    prev_limit = 0.0
    for limit, rate in slabs:
        if taxable_income > prev_limit:
            taxable_in_slab = min(taxable_income, limit) - prev_limit
            tax += taxable_in_slab * rate
            prev_limit = limit
        else:
            break
            
    # Section 87A rebate for taxable income up to 12 Lakhs (Zero tax)
    if taxable_income <= 1200000:
        tax = 0.0
    else:
        # Marginal relief buffer
        tax = min(tax, taxable_income - 1200000)
        
    # Health and Education Cess (4%)
    total_tax = tax * 1.04
    
    # Annual take-home after tax
    annual_inhand = max(0.0, cash_gross - total_tax)
    monthly_inhand = annual_inhand / 12.0
    
    return {
        "monthly_inhand_inr": monthly_inhand,
        "annual_inhand_inr": annual_inhand,
        "annual_tax_inr": total_tax,
        "effective_tax_rate_pct": (total_tax / cash_gross * 100) if cash_gross > 0 else 0.0
    }


# ==============================================================================
# CORE SALARY PREDICTION ENGINE
# ==============================================================================
def calculate_candidate_salary(
    years_of_experience: float,
    role: str,
    selected_skills: list,
    education_tier: str = "Tier 1 (IIT / BITS / NIT / Top IIIT)",
    target_city: str = "Bengaluru",
    target_company: str = None
):
    """
    Computes market salary estimate (in INR Lakhs) for given candidate profile.
    Returns median, 25th percentile, 75th percentile, 90th percentile, and breakdown.
    """
    # 1. Base Role & Experience Curve
    role_info = ROLE_EXPERIENCE_CURVES.get(
        role,
        ROLE_EXPERIENCE_CURVES["Software Engineer (Backend / Full Stack)"]
    )
    base_0 = role_info["base_at_0"]
    growth = role_info["growth_factor"]
    
    # Smooth logarithmic & power progression
    yoe = max(0.0, float(years_of_experience))
    exp_multiplier = 1.0 + (growth - 1.0) * (math.pow(yoe, 0.88) * 1.25)
    baseline_ctc = base_0 * exp_multiplier
    
    # 2. Education Tier Factor (decreases weight as experience grows)
    edu_raw_factor = EDUCATION_TIERS.get(education_tier, 1.0)
    edu_weight = max(0.08, 1.0 - (yoe * 0.09))
    edu_effective_multiplier = 1.0 + (edu_raw_factor - 1.0) * edu_weight
    
    # 3. Skills Stack Multiplier
    skill_boost_sum = 0.0
    for sk in selected_skills:
        if sk in SKILLS_DATA:
            skill_boost_sum += SKILLS_DATA[sk]["salary_boost_pct"]
            
    # Synergy bonuses
    synergy_bonus = 0.0
    skills_set = set(selected_skills)
    
    # Known high-value synergies
    if "System Design" in skills_set and "Distributed Systems" in skills_set:
        synergy_bonus += 0.06
    if "Go (Golang)" in skills_set and "Kubernetes" in skills_set:
        synergy_bonus += 0.05
    if "PyTorch" in skills_set and "Generative AI & LLMs" in skills_set:
        synergy_bonus += 0.07
    if "Java" in skills_set and "Spring Boot" in skills_set and "Apache Kafka" in skills_set:
        synergy_bonus += 0.05
    if "React.js" in skills_set and "Next.js" in skills_set and "Node.js & Express" in skills_set:
        synergy_bonus += 0.04
    if "AWS (Amazon Web Services)" in skills_set and "Docker" in skills_set and "Kubernetes" in skills_set:
        synergy_bonus += 0.05
        
    total_skill_boost = min(0.75, skill_boost_sum * 0.72 + synergy_bonus)
    skill_multiplier = 1.0 + total_skill_boost
    
    # 4. Regional City Multiplier
    city_mult = 1.0
    region_found = "South"
    for reg_name, reg_val in REGIONS_DATA.items():
        if target_city in reg_val["cities"]:
            city_mult = reg_val["cities"][target_city]["multiplier"]
            region_found = reg_name
            break
            
    # 5. Company Multiplier (if specific company provided)
    comp_mult = 1.0
    bonus_pct = 0.12
    stock_pct = 0.15
    if target_company and target_company in COMPANIES_DATA:
        c_info = COMPANIES_DATA[target_company]
        comp_mult = c_info["multiplier"]
        bonus_pct = c_info["bonus_pct"]
        stock_pct = c_info["stock_equity_pct"]
        
    # Total Median CTC calculation (in INR Lakhs)
    median_ctc = baseline_ctc * edu_effective_multiplier * skill_multiplier * city_mult * comp_mult
    
    # Percentiles
    p25_ctc = median_ctc * 0.82
    p75_ctc = median_ctc * 1.25
    p90_ctc = median_ctc * 1.58
    
    # Salary Component Breakdown
    stock_component = median_ctc * stock_pct
    bonus_component = median_ctc * bonus_pct
    base_salary_component = max(0.0, median_ctc - stock_component - bonus_component)
    
    # In-Hand Monthly Take Home
    inhand_data = calculate_inhand_monthly(median_ctc * 100000)
    
    return {
        "median_lakhs": round(median_ctc, 2),
        "p25_lakhs": round(p25_ctc, 2),
        "p75_lakhs": round(p75_ctc, 2),
        "p90_lakhs": round(p90_ctc, 2),
        "base_salary_lakhs": round(base_salary_component, 2),
        "bonus_lakhs": round(bonus_component, 2),
        "stock_lakhs": round(stock_component, 2),
        "monthly_inhand_inr": round(inhand_data["monthly_inhand_inr"], 0),
        "annual_inhand_lakhs": round(inhand_data["annual_inhand_inr"] / 100000, 2),
        "effective_tax_pct": round(inhand_data["effective_tax_rate_pct"], 1),
        "skill_boost_applied_pct": round(total_skill_boost * 100, 1),
        "city_multiplier": city_mult,
        "region": region_found,
        "company_multiplier": comp_mult
    }


# ==============================================================================
# REGIONAL COMPARISON ENGINE (NORTH VS SOUTH VS WEST VS EAST)
# ==============================================================================
def get_regional_salary_comparison(
    years_of_experience: float,
    role: str,
    selected_skills: list,
    education_tier: str = "Tier 1 (IIT / BITS / NIT / Top IIIT)",
    target_company: str = None
):
    """
    Evaluates candidate's salary across all Indian tech regions and cities,
    including nominal CTC, cost-of-living adjusted real savings, and ranking.
    """
    rows = []
    
    for region_name, reg_info in REGIONS_DATA.items():
        for city_name, city_info in reg_info["cities"].items():
            res = calculate_candidate_salary(
                years_of_experience=years_of_experience,
                role=role,
                selected_skills=selected_skills,
                education_tier=education_tier,
                target_city=city_name,
                target_company=target_company
            )
            
            median_ctc = res["median_lakhs"]
            monthly_inhand = res["monthly_inhand_inr"]
            rent_inr = city_info["avg_rent_monthly_inr"]
            
            # Other basic living expenses (groceries, utilities, commute)
            other_living_inr = 16000 * city_info["living_cost_factor"]
            total_monthly_expenses = rent_inr + other_living_inr
            monthly_net_savings = max(0.0, monthly_inhand - total_monthly_expenses)
            annual_net_savings_lakhs = (monthly_net_savings * 12) / 100000
            
            rows.append({
                "Region": region_name,
                "City": city_name,
                "Display Name": city_info["display_name"],
                "Median CTC (₹ L)": median_ctc,
                "25th-75th Band (₹ L)": f"₹{res['p25_lakhs']} - ₹{res['p75_lakhs']} L",
                "Monthly In-Hand (₹)": monthly_inhand,
                "Cost of Living Index": city_info["cost_of_living_index"],
                "Monthly Rent Est. (₹)": rent_inr,
                "Est. Annual Real Savings (₹ L)": round(annual_net_savings_lakhs, 2),
                "Demand Heat": city_info["demand_heat"],
                "Top Specialty": city_info["specialty"],
                "Multiplier": city_info["multiplier"]
            })
            
    df = pd.DataFrame(rows)
    df = df.sort_values(by="Median CTC (₹ L)", ascending=False).reset_index(drop=True)
    
    # Regional summaries
    region_summary = df.groupby("Region").agg(
        Avg_CTC_Lakhs=("Median CTC (₹ L)", "mean"),
        Max_CTC_Lakhs=("Median CTC (₹ L)", "max"),
        Avg_Savings_Lakhs=("Est. Annual Real Savings (₹ L)", "mean"),
        Avg_COLI=("Cost of Living Index", "mean")
    ).round(2).reset_index().sort_values(by="Avg_CTC_Lakhs", ascending=False)
    
    top_city = df.iloc[0]["City"]
    top_region = df.iloc[0]["Region"]
    highest_ctc = df.iloc[0]["Median CTC (₹ L)"]
    
    # Best savings city
    best_savings_row = df.sort_values(by="Est. Annual Real Savings (₹ L)", ascending=False).iloc[0]
    
    return {
        "cities_df": df,
        "region_summary_df": region_summary,
        "highest_paying_city": top_city,
        "highest_paying_region": top_region,
        "highest_ctc_lakhs": highest_ctc,
        "best_savings_city": best_savings_row["City"],
        "best_savings_lakhs": best_savings_row["Est. Annual Real Savings (₹ L)"]
    }


# ==============================================================================
# COMPANY SALARY BENCHMARK & SKILL MATCH ENGINE
# ==============================================================================
def evaluate_company_for_candidate(
    company_name: str,
    years_of_experience: float,
    role: str,
    selected_skills: list,
    education_tier: str = "Tier 1 (IIT / BITS / NIT / Top IIIT)",
    target_city: str = "Bengaluru"
):
    """
    Detailed compensation & skill fit analysis for a specific chosen company.
    """
    if company_name not in COMPANIES_DATA:
        return None
        
    c_info = COMPANIES_DATA[company_name]
    
    # Calculate salary tailored to this company
    salary_res = calculate_candidate_salary(
        years_of_experience=years_of_experience,
        role=role,
        selected_skills=selected_skills,
        education_tier=education_tier,
        target_city=target_city,
        target_company=company_name
    )
    
    # Skill overlap calculation
    comp_skills = c_info["primary_stack"]
    candidate_skills_set = set(selected_skills)
    
    matched = [s for s in comp_skills if s in candidate_skills_set]
    missing = [s for s in comp_skills if s not in candidate_skills_set]
    fit_score = (len(matched) / len(comp_skills)) * 100 if comp_skills else 100.0
    
    return {
        "company_name": company_name,
        "tier": c_info["tier"],
        "median_ctc_lakhs": salary_res["median_lakhs"],
        "p25_ctc_lakhs": salary_res["p25_lakhs"],
        "p75_ctc_lakhs": salary_res["p75_lakhs"],
        "p90_ctc_lakhs": salary_res["p90_lakhs"],
        "base_salary_lakhs": salary_res["base_salary_lakhs"],
        "bonus_lakhs": salary_res["bonus_lakhs"],
        "stock_lakhs": salary_res["stock_lakhs"],
        "monthly_inhand_inr": salary_res["monthly_inhand_inr"],
        "interview_difficulty": c_info["interview_difficulty"],
        "hiring_bar": c_info["hiring_bar"],
        "locations": c_info["locations"],
        "primary_stack": comp_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "fit_score_pct": round(fit_score, 1),
        "summary": c_info["summary"]
    }


def rank_companies_by_skill_match(
    years_of_experience: float,
    role: str,
    selected_skills: list,
    education_tier: str = "Tier 1 (IIT / BITS / NIT / Top IIIT)",
    target_city: str = "Bengaluru",
    filter_tier: str = "All Tiers"
):
    """
    Ranks all companies in the ecosystem based on:
    1. Expected CTC for the candidate
    2. Candidate's skill fit match percentage
    """
    candidate_skills_set = set(selected_skills)
    results = []
    
    for comp_name, comp_info in COMPANIES_DATA.items():
        if filter_tier != "All Tiers" and comp_info["tier"] != filter_tier:
            continue
            
        sal = calculate_candidate_salary(
            years_of_experience=years_of_experience,
            role=role,
            selected_skills=selected_skills,
            education_tier=education_tier,
            target_city=target_city,
            target_company=comp_name
        )
        
        comp_stack = comp_info["primary_stack"]
        matched = [s for s in comp_stack if s in candidate_skills_set]
        fit_pct = (len(matched) / len(comp_stack) * 100) if comp_stack else 0.0
        
        results.append({
            "Company": comp_name,
            "Tier": comp_info["tier"],
            "Expected CTC (₹ L)": sal["median_lakhs"],
            "Base Salary (₹ L)": sal["base_salary_lakhs"],
            "Annual Stocks (₹ L)": sal["stock_lakhs"],
            "Skill Fit Match (%)": round(fit_pct, 1),
            "Matched Skills": ", ".join(matched) if matched else "None",
            "Interview Bar": comp_info["hiring_bar"],
            "Locations": ", ".join(comp_info["locations"][:2])
        })
        
    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values(by="Expected CTC (₹ L)", ascending=False).reset_index(drop=True)
    return df


# ==============================================================================
# UPSKILLING ROI & SALARY BOOSTER ENGINE
# ==============================================================================
def recommend_upskilling_path(
    years_of_experience: float,
    role: str,
    current_skills: list,
    education_tier: str = "Tier 1 (IIT / BITS / NIT / Top IIIT)",
    target_city: str = "Bengaluru",
    target_company: str = None
):
    """
    Identifies high-impact skills NOT currently in the candidate's profile.
    Calculates exact incremental CTC gain (+₹ Lakhs, +% hike),
    the unlocked companies, and the best regions for each skill.
    """
    current_skills_set = set(current_skills)
    current_calc = calculate_candidate_salary(
        years_of_experience=years_of_experience,
        role=role,
        selected_skills=current_skills,
        education_tier=education_tier,
        target_city=target_city,
        target_company=target_company
    )
    current_ctc = current_calc["median_lakhs"]
    
    recommendations = []
    
    for skill_name, skill_info in SKILLS_DATA.items():
        if skill_name in current_skills_set:
            continue
            
        # Simulate adding this single skill
        simulated_skills = current_skills + [skill_name]
        sim_calc = calculate_candidate_salary(
            years_of_experience=years_of_experience,
            role=role,
            selected_skills=simulated_skills,
            education_tier=education_tier,
            target_city=target_city,
            target_company=target_company
        )
        
        sim_ctc = sim_calc["median_lakhs"]
        ctc_gain = round(sim_ctc - current_ctc, 2)
        pct_gain = round((ctc_gain / current_ctc * 100), 1) if current_ctc > 0 else 0.0
        
        recommendations.append({
            "Skill": skill_name,
            "Category": skill_info["category"],
            "Salary Boost (₹ L)": ctc_gain,
            "Hike (%)": pct_gain,
            "New Projected CTC (₹ L)": sim_ctc,
            "Demand Score": skill_info["demand_score"],
            "Difficulty": skill_info["learning_difficulty"],
            "Est. Weeks": skill_info["weeks_to_learn"],
            "Best Regions": ", ".join(skill_info["primary_regions"][:2]),
            "Target Companies": ", ".join(skill_info["target_companies"][:3]),
            "Description": skill_info["description"]
        })
        
    df = pd.DataFrame(recommendations)
    if not df.empty:
        df = df.sort_values(by=["Salary Boost (₹ L)", "Demand Score"], ascending=[False, False]).reset_index(drop=True)
    return df, current_ctc
