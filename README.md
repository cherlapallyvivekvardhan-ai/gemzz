# 🧭 SalaryScope India: AI-Powered Tech Salary Market Intelligence & Career Upskilling Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B.svg)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F51B5.svg)](https://plotly.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, data-driven salary benchmarking and career acceleration platform designed for the Indian technology ecosystem.

Calibrated to **2025–2026 tech compensation benchmarks across 55+ top employers, 8 major tech corridors, and 40+ high-demand tech skills**.

---

## 🎯 Key Capabilities & What It Solves

### 1. 🧭 Personalized Salary Predictor & Take-Home Estimator
* **Input Parameters:** Years of Experience (0–20+ yrs), Domain Role, Education Pedigree, Active Tech Skills Stack, and Location.
* **Instant Compensation Benchmarks:**
  * **Median Market CTC** (INR Lakhs)
  * **25th–75th Percentile** Offer Range
  * **Top 10% Outlier CTC** (Tier 1 Big Tech / Quant benchmarks)
* **Granular Breakdown:** Base Salary (Fixed) vs. Annual Performance Bonus vs. Stocks / RSUs.
* **Monthly In-Hand Take-Home:** Accurate tax deductions under the **New Tax Regime (Section 115BAC, FY 2025-26)** with standard deductions and Section 87A rebate calculations.
* **Long-Term Trajectory Curve:** Dynamic 0–15 year progression curve for your specific domain and skill stack.

### 2. 🗺️ Regional Salary Intelligence (North vs. South vs. West vs. East)
* **Direct Regional Comparison:**
  * **South Hubs:** Bengaluru (Karnataka), Hyderabad (Telangana), Chennai (Tamil Nadu)
  * **North Hubs:** Delhi-NCR Gurgaon (Haryana), Delhi-NCR Noida (UP), Chandigarh/Mohali
  * **West Hubs:** Mumbai / Navi Mumbai, Pune, Ahmedabad (GIFT City)
  * **East & Remote:** Kolkata, Fully Remote / Distributed
* **Identifies Highest-Paying Hubs:** Pinpoints where your exact skill set commands the highest gross CTC (e.g., South Region led by Bengaluru and Hyderabad).
* **Cost of Living & Real Purchasing Power Index:** Real-world comparison showing whether a higher nominal CTC in Mumbai/Bengaluru actually yields higher savings than Hyderabad, Pune, or Remote setups after adjusting for tech corridor rents and living expenses.

### 3. 🏢 Company Pay Intelligence & Wished Company Evaluation
* **🎯 Target / Wished Company Deep-Dive:**
  * Select or search any company (e.g., *Google, Microsoft, Amazon, Meta, Uber, Flipkart, Swiggy, Zomato, Razorpay, CRED, PhonePe, Goldman Sachs, Morgan Stanley, Atlassian, Adobe, Postman, BrowserStack, Zerodha, TCS, Infosys, Accenture*).
  * Evaluates your custom compensation package, base salary, bonus, and RSU equity policy.
  * **Skill Fit Gap Analysis:** Identifies matched skills and highlights exact missing skills required to crack that employer.
  * Interview difficulty bar (1–5 scale) and hiring bar insights.
* **🏆 Skill-Matched Company Leaderboard:**
  * Dynamic ranking of companies that pay the highest for your exact skill combination.
  * Filterable by category: *Tier 1 Big Tech (FAANG+), Indian Tech Unicorns, FinTech & Elite GCCs, Scaled Product, or Global IT Services*.

### 4. 🚀 Upskilling ROI & Salary Growth Booster
* **Automated High-ROI Skill Recommendations:**
  * Scans missing skills from your domain and identifies the top 5 highest-yielding skills to learn next.
  * Quantified Salary Hike: e.g., **+₹4.5 L / yr (+28%)** if you master *System Design*, or **+₹6.0 L / yr (+35%)** for *Generative AI & LLMs*.
  * Highlights which dream companies unlock higher salary bands and which geographic areas have peak demand.
* **🔮 Interactive "What-If" Upskill Simulator:**
  * Add 1 to 3 prospective skills and observe real-time projected salary leaps, before/after component charts, and monthly in-hand jumps.

### 5. 🌐 Macroeconomic Market & Public Pay Parity
* Retains macroeconomic structure: 2.15M+ active MCA enterprises, five-sector economic stratification, and 7th CPC Central Pay Commission matrix for public-private pay comparisons.

### 6. 📄 Career Strategy Dossier & CSV Export
* Summary career scorecard and tactical negotiation playbook (leveraging equity, competing offers, and remote allowances).
* One-click download of regional salary benchmarks as CSV.

---

## 🏗️ Project Architecture

```
salary_intelligence_app/
├── app.py                      # Primary Streamlit application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Production container configuration
├── run.bat                     # Windows one-click batch launcher
├── run.ps1                     # PowerShell one-click launch script
│
├── .streamlit/
│   └── config.toml             # Theme & server configuration
│
├── data/
│   ├── salary_data.py          # Regional benchmarks, 55+ companies, role curves
│   └── skills_data.py          # 40+ skills taxonomy, demand scores, multipliers
│
├── engine/
│   └── salary_calculator.py    # Core math: Tax, CTC, Regional & Upskilling engines
│
├── views/
│   ├── calculator_view.py      # Profile input & compensation estimator
│   ├── regional_view.py        # North vs South vs West regional analysis
│   ├── company_view.py         # Wished company & skill-matched leaderboards
│   ├── upskill_view.py         # High-ROI skills & What-If simulator
│   ├── macro_view.py           # Corporate registry & 7th CPC pay matrix
│   └── report_view.py          # Career dossier & report export
│
├── labour_to_owner/            # Legacy compatibility wrapper
│   ├── app.py                  # Forwards to main app
│   └── requirements.txt
│
└── tests/
    └── test_engine.py          # Automated test suite (100% pass)
```

---

## ⚡ Quickstart & Local Execution

### Option A: Direct Command Line (Recommended)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch application
streamlit run app.py
```

### Option B: Windows One-Click
* Simply double-click **`run.bat`** or run **`.\run.ps1`** in PowerShell.

### Option C: Run Test Suite
```bash
python -m unittest discover -s tests
```

---

## ☁️ Deployment Guide

### 1. Deploy on Streamlit Community Cloud (Free & 1-Click)
1. Push this repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Select your repository, branch (`main`), and set **Main file path** to `app.py`.
4. Click **Deploy**! The app will be live with full interactivity.

### 2. Deploy with Docker
```bash
# Build Docker image
docker build -t salaryscope-india .

# Run container
docker run -p 8501:8501 salaryscope-india
```
Access at `http://localhost:8501`.

### 3. Deploy on Render, Railway, or Hugging Face Spaces
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `streamlit run app.py --server.port=8501 --server.address=0.0.0.0`

---

## 📊 Data Sources & Methodology
* **Compensation Bands:** Aggregated and calibrated to verified 2025–2026 tech offer levels across Tier 1 Product, Unicorns, GCCs, and IT Services.
* **Taxation Engine:** Modeled on the Indian Union Budget New Tax Regime (Section 115BAC) with standard deduction of ₹75,000, updated income tax slabs, and Section 87A rebate.
* **Cost of Living Indices:** Calibrated using real estate rental averages in tech corridors (Whitefield/ORR in Bengaluru, Hitec City in Hyderabad, Cyber City in Gurgaon, BKC/Powai in Mumbai, OMR in Chennai, Kharadi/Hinjewadi in Pune).
