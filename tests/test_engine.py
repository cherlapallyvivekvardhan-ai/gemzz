"""
Unit and integration tests for SalaryScope calculation engine.
"""

import unittest
import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.salary_calculator import (
    calculate_candidate_salary,
    get_regional_salary_comparison,
    evaluate_company_for_candidate,
    rank_companies_by_skill_match,
    recommend_upskilling_path,
    calculate_inhand_monthly
)


class TestSalaryScopeEngine(unittest.TestCase):
    
    def test_calculate_inhand_monthly(self):
        # Gross ₹12 Lakhs should have 0 tax under Section 87A rebate
        res_12l = calculate_inhand_monthly(1200000)
        self.assertEqual(res_12l["annual_tax_inr"], 0.0)
        self.assertGreater(res_12l["monthly_inhand_inr"], 0)
        
        # High gross ₹30 Lakhs
        res_30l = calculate_inhand_monthly(3000000)
        self.assertGreater(res_30l["annual_tax_inr"], 0.0)
        self.assertGreater(res_30l["monthly_inhand_inr"], 100000)
        
    def test_candidate_salary_calculation(self):
        res = calculate_candidate_salary(
            years_of_experience=4.0,
            role="Software Engineer (Backend / Full Stack)",
            selected_skills=["Python", "SQL & Relational Databases", "AWS (Amazon Web Services)"],
            education_tier="Tier 1 (IIT / BITS / NIT / Top IIIT)",
            target_city="Bengaluru"
        )
        self.assertIn("median_lakhs", res)
        self.assertGreater(res["median_lakhs"], 10.0)
        self.assertLess(res["p25_lakhs"], res["median_lakhs"])
        self.assertGreater(res["p75_lakhs"], res["median_lakhs"])
        self.assertGreater(res["p90_lakhs"], res["p75_lakhs"])
        self.assertGreater(res["monthly_inhand_inr"], 50000)
        
    def test_regional_salary_comparison(self):
        res = get_regional_salary_comparison(
            years_of_experience=3.0,
            role="Software Engineer (Backend / Full Stack)",
            selected_skills=["Java", "Spring Boot"]
        )
        self.assertIn("cities_df", res)
        self.assertFalse(res["cities_df"].empty)
        # Should identify top paying city (e.g. Bengaluru)
        self.assertTrue(len(res["highest_paying_city"]) > 0)
        self.assertIn(res["highest_paying_region"], ["South", "West", "North"])
        # Should identify best savings city
        self.assertTrue(len(res["best_savings_city"]) > 0)
        
    def test_wished_company_evaluation(self):
        eval_google = evaluate_company_for_candidate(
            company_name="Google",
            years_of_experience=5.0,
            role="Software Engineer (Backend / Full Stack)",
            selected_skills=["Python", "System Design", "Go (Golang)"],
            target_city="Bengaluru"
        )
        self.assertIsNotNone(eval_google)
        self.assertGreater(eval_google["median_ctc_lakhs"], 30.0)
        self.assertIn("Python", eval_google["matched_skills"])
        self.assertGreater(eval_google["fit_score_pct"], 0.0)
        
    def test_skill_matched_company_ranking(self):
        ranked = rank_companies_by_skill_match(
            years_of_experience=2.0,
            role="AI / Machine Learning Engineer",
            selected_skills=["Python", "PyTorch", "Generative AI & LLMs"]
        )
        self.assertFalse(ranked.empty)
        self.assertIn("Company", ranked.columns)
        self.assertIn("Expected CTC (₹ L)", ranked.columns)
        
    def test_upskilling_recommendations(self):
        recs, current_ctc = recommend_upskilling_path(
            years_of_experience=3.0,
            role="Software Engineer (Backend / Full Stack)",
            current_skills=["Python", "SQL & Relational Databases"]
        )
        self.assertFalse(recs.empty)
        # Recommended skills should not include current skills
        rec_skill_names = recs["Skill"].tolist()
        self.assertNotIn("Python", rec_skill_names)
        # First recommended skill should yield positive hike
        top_rec = recs.iloc[0]
        self.assertGreater(top_rec["Salary Boost (₹ L)"], 0.0)
        self.assertGreater(top_rec["Hike (%)"], 0.0)


if __name__ == "__main__":
    unittest.main()
