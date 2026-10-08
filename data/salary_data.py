"""
Comprehensive Salary Data, Regional Metrics, and Company Profiles for India Tech Ecosystem.
Calibrated to 2025-2026 tech compensation benchmarks across South, North, West, East, and Remote.
"""

# ==============================================================================
# 1. REGIONAL AND CITY BENCHMARKS
# ==============================================================================
REGIONS_DATA = {
    "South": {
        "description": "India's Deep-Tech, Cloud, SaaS & GCC Innovation Capital",
        "avg_regional_multiplier": 1.12,
        "key_hubs": ["Bengaluru", "Hyderabad", "Chennai"],
        "dominant_sectors": ["AI/ML Labs", "Cloud Infrastructure", "Enterprise SaaS", "Global Capability Centers (GCCs)"],
        "cities": {
            "Bengaluru": {
                "display_name": "Bengaluru (Karnataka)",
                "multiplier": 1.18,
                "cost_of_living_index": 110,
                "avg_rent_monthly_inr": 28000,
                "demand_heat": "Ultra High 🔥",
                "specialty": "Unicorn Startups, FAANG+ R&D, AI Research, Venture Capital Hub",
                "top_employers": ["Google", "Amazon", "Flipkart", "Swiggy", "Razorpay", "CRED", "Microsoft", "Uber"],
                "living_cost_factor": 1.15
            },
            "Hyderabad": {
                "display_name": "Hyderabad (Telangana)",
                "multiplier": 1.10,
                "cost_of_living_index": 88,
                "avg_rent_monthly_inr": 20000,
                "demand_heat": "Very High ⚡",
                "specialty": "Mega GCC Campuses, Cloud Platforms, Enterprise Systems, Life Sciences Tech",
                "top_employers": ["Microsoft", "Google", "Amazon", "Salesforce", "Goldman Sachs", "ServiceNow"],
                "living_cost_factor": 0.90
            },
            "Chennai": {
                "display_name": "Chennai (Tamil Nadu)",
                "multiplier": 0.98,
                "cost_of_living_index": 82,
                "avg_rent_monthly_inr": 18000,
                "demand_heat": "High 📈",
                "specialty": "Global SaaS Capital (Zoho, Freshworks), Automotive Tech, Large-Scale Banking Tech",
                "top_employers": ["Freshworks", "Zoho", "Amazon", "PayPal", "Cognizant", "Standard Chartered"],
                "living_cost_factor": 0.85
            }
        }
    },
    "North": {
        "description": "High-Velocity Consumer Tech, FinTech, E-Commerce & Enterprise Corridor",
        "avg_regional_multiplier": 1.05,
        "key_hubs": ["Delhi-NCR (Gurgaon)", "Delhi-NCR (Noida)", "Chandigarh / Mohali"],
        "dominant_sectors": ["FinTech & Payments", "B2C E-Commerce & Quick Commerce", "Product Consulting", "Enterprise Software"],
        "cities": {
            "Delhi-NCR (Gurgaon)": {
                "display_name": "Gurgaon / Gurugram (Haryana)",
                "multiplier": 1.14,
                "cost_of_living_index": 106,
                "avg_rent_monthly_inr": 27000,
                "demand_heat": "Very High 🔥",
                "specialty": "Consumer Tech, FinTech Powerhouses, High-Scale Quick Commerce, Big 4 Consulting",
                "top_employers": ["Zomato", "Blinkit", "MakeMyTrip", "PolicyBazaar", "Delhivery", "Google", "American Express"],
                "living_cost_factor": 1.10
            },
            "Delhi-NCR (Noida)": {
                "display_name": "Noida / Greater Noida (UP)",
                "multiplier": 0.97,
                "cost_of_living_index": 85,
                "avg_rent_monthly_inr": 19000,
                "demand_heat": "High 📈",
                "specialty": "Software R&D Centers, Mobile OS, Digital Payments, Tech Infrastructure",
                "top_employers": ["Adobe", "Samsung R&D", "Microsoft", "Paytm", "HCLTech", "Oracle"],
                "living_cost_factor": 0.88
            },
            "Chandigarh": {
                "display_name": "Chandigarh / Mohali (Punjab/Haryana)",
                "multiplier": 0.84,
                "cost_of_living_index": 72,
                "avg_rent_monthly_inr": 14000,
                "demand_heat": "Moderate 🚀",
                "specialty": "Emerging Tech Corridors, Outsourced Engineering, Cloud Migrations",
                "top_employers": ["Infosys", "Tech Mahindra", "Quark", "Promoted Startups"],
                "living_cost_factor": 0.74
            }
        }
    },
    "West": {
        "description": "Financial Capital, Low-Latency FinTech, Quant Trading & R&D Hub",
        "avg_regional_multiplier": 1.08,
        "key_hubs": ["Mumbai", "Pune", "Ahmedabad (GIFT City)"],
        "dominant_sectors": ["Banking & Investment Tech (BFSI)", "Algorithmic & Quant Trading", "Automotive Embedded Tech", "Enterprise Engineering"],
        "cities": {
            "Mumbai": {
                "display_name": "Mumbai / Navi Mumbai (Maharashtra)",
                "multiplier": 1.16,
                "cost_of_living_index": 126,
                "avg_rent_monthly_inr": 36000,
                "demand_heat": "Very High 🔥",
                "specialty": "Highest Quant & HFT Comp, BFSI Tech Centers, Media/AdTech, Major Conglomerate Tech",
                "top_employers": ["Morgan Stanley", "JP Morgan", "Nomura", "BrowserStack", "Zepto", "Jio Platforms", "Tata Digital"],
                "living_cost_factor": 1.30
            },
            "Pune": {
                "display_name": "Pune (Maharashtra)",
                "multiplier": 1.01,
                "cost_of_living_index": 86,
                "avg_rent_monthly_inr": 19000,
                "demand_heat": "High 📈",
                "specialty": "Systems Software, Deep R&D, Automotive IoT, FinTech Engineering Hub",
                "top_employers": ["NVIDIA", "Veritas", "Barclays", "Mastercard", "Siemens", "PhonePe"],
                "living_cost_factor": 0.88
            },
            "Ahmedabad": {
                "display_name": "Ahmedabad / Gandhinagar - GIFT City (Gujarat)",
                "multiplier": 0.86,
                "cost_of_living_index": 73,
                "avg_rent_monthly_inr": 14500,
                "demand_heat": "Emerging Fast ⚡",
                "specialty": "GIFT SEZ FinTech & Banking Offshore Centers, Cloud Security",
                "top_employers": ["NSE IFSC Tech", "Oracle", "TCS", "Adani Tech", "FinTech Startups"],
                "living_cost_factor": 0.75
            }
        }
    },
    "East": {
        "description": "Rapidly Growing Tech Corridor with High Savings Ratio",
        "avg_regional_multiplier": 0.85,
        "key_hubs": ["Kolkata", "Bhubaneswar"],
        "dominant_sectors": ["Data Analytics", "Enterprise IT Consulting", "Cloud Operations"],
        "cities": {
            "Kolkata": {
                "display_name": "Kolkata (West Bengal - Sector V / New Town)",
                "multiplier": 0.85,
                "cost_of_living_index": 68,
                "avg_rent_monthly_inr": 13500,
                "demand_heat": "Moderate 🚀",
                "specialty": "Enterprise Systems, Financial Analytics, Cost-Effective Engineering Operations",
                "top_employers": ["TCS", "Cognizant", "PwC AC", "Wipro", "IBM", "Capgemini"],
                "living_cost_factor": 0.70
            },
            "Bhubaneswar": {
                "display_name": "Bhubaneswar (Odisha)",
                "multiplier": 0.80,
                "cost_of_living_index": 65,
                "avg_rent_monthly_inr": 12000,
                "demand_heat": "Developing 🌿",
                "specialty": "State Tech Parks, Tier-2 Delivery Centers",
                "top_employers": ["Infosys", "TCS", "Wipro", "Mindtree", "Tech Mahindra"],
                "living_cost_factor": 0.67
            }
        }
    },
    "Remote": {
        "description": "Location-Agnostic Distributed Engineering Roles",
        "avg_regional_multiplier": 1.06,
        "key_hubs": ["All-India Distributed / Work from Anywhere"],
        "dominant_sectors": ["Global Remote SaaS", "Developer Tooling", "Web3 / Decentralized", "US/EU Remote Contractors"],
        "cities": {
            "Remote / Pan-India": {
                "display_name": "Fully Remote / Distributed (Pan-India)",
                "multiplier": 1.06,
                "cost_of_living_index": 75,
                "avg_rent_monthly_inr": 15000,
                "demand_heat": "High 🌍",
                "specialty": "Distributed Global Teams, Async Work, Maximum Real Savings Retention",
                "top_employers": ["GitLab", "Automattic", "Postman", "Atlassian", "BrowserStack", "Zerodha"],
                "living_cost_factor": 0.75
            }
        }
    }
}


# ==============================================================================
# 2. COMPANY PROFILES DATABASE (55+ TOP EMPLOYERS IN INDIA)
# ==============================================================================
COMPANIES_DATA = {
    # Tier 1 - Big Tech / Global FAANG+
    "Google": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 2.25,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.35,
        "interview_difficulty": 4.9,
        "hiring_bar": "Elite (Data Structures, System Design, Googleyness)",
        "locations": ["Bengaluru", "Hyderabad", "Delhi-NCR (Gurgaon)"],
        "primary_stack": ["Python", "Go (Golang)", "C++", "System Design", "Generative AI & LLMs", "Distributed Systems", "Kubernetes"],
        "summary": "Gold standard in engineering culture, global scale infrastructure, top-tier compensation and equity grants."
    },
    "Microsoft": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 2.05,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.30,
        "interview_difficulty": 4.7,
        "hiring_bar": "Very High (System Architecture, DSA, Cloud Scale)",
        "locations": ["Hyderabad", "Bengaluru", "Delhi-NCR (Noida)"],
        "primary_stack": ["C# / .NET", "Java", "Azure", "Distributed Systems", "Generative AI & LLMs", "Python"],
        "summary": "Deep focus on Cloud (Azure), AI copilot platforms, massive India R&D campus in Hyderabad and Bengaluru."
    },
    "Amazon": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 1.95,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.32,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (14 Leadership Principles, Low-Level & High-Level Design)",
        "locations": ["Bengaluru", "Hyderabad", "Chennai", "Delhi-NCR (Gurgaon)"],
        "primary_stack": ["Java", "AWS (Amazon Web Services)", "Distributed Systems", "System Design", "Microservices", "SQL & Relational Databases"],
        "summary": "High ownership, fast-paced environment, massive AWS platform and international retail engineering teams."
    },
    "Meta (Facebook)": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 2.30,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.38,
        "interview_difficulty": 4.9,
        "hiring_bar": "Elite (Speed Coding, Massive Scale Distributed Architecture)",
        "locations": ["Bengaluru", "Delhi-NCR (Gurgaon)"],
        "primary_stack": ["Python", "React.js", "Distributed Systems", "PyTorch", "Generative AI & LLMs", "C++"],
        "summary": "Top compensator in tech; engineering teams focus on PyTorch, AI infrastructure, and WhatsApp business scale."
    },
    "Uber": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 2.15,
        "bonus_pct": 0.14,
        "stock_equity_pct": 0.30,
        "interview_difficulty": 4.8,
        "hiring_bar": "Elite (Complex Concurrency, Distributed Systems, High Throughput)",
        "locations": ["Bengaluru", "Hyderabad"],
        "primary_stack": ["Go (Golang)", "Java", "Apache Kafka", "Microservices", "System Design", "Docker"],
        "summary": "World-class engineering teams working on high-throughput ride-hailing and fintech payment engines."
    },
    "Apple": {
        "tier": "Tier 1 - Big Tech (FAANG+)",
        "multiplier": 2.10,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.32,
        "interview_difficulty": 4.7,
        "hiring_bar": "Very High (Deep Systems, Hardware-Software Co-Design, iOS Core)",
        "locations": ["Hyderabad", "Bengaluru"],
        "primary_stack": ["C++", "Python", "System Design", "Machine Learning & Data Science"],
        "summary": "High secrecy, elite engineering standards, expanding Hyderabad maps & services engineering hub."
    },

    # Tier 1 - Indian Tech Unicorns & High-Growth Product
    "Flipkart": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.85,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.22,
        "interview_difficulty": 4.5,
        "hiring_bar": "Very High (Machine Coding, System Architecture, Low Level Design)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Java", "Spring Boot", "Apache Kafka", "System Design", "Microservices", "Data Engineering"],
        "summary": "Pioneer of Indian tech engineering culture; huge throughput during Big Billion Days scale."
    },
    "Swiggy": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.80,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.20,
        "interview_difficulty": 4.4,
        "hiring_bar": "High (Machine Coding, Event-Driven Architecture, High Concurrency)",
        "locations": ["Bengaluru", "Remote / Pan-India"],
        "primary_stack": ["Go (Golang)", "Python", "Microservices", "Redis & Caching", "AWS (Amazon Web Services)", "System Design"],
        "summary": "Fast-moving logistics and food delivery platform with a progressive permanent remote-first policy for tech."
    },
    "Zomato": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.78,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.20,
        "interview_difficulty": 4.4,
        "hiring_bar": "High (Fast execution, Full Stack & Backend Scalability)",
        "locations": ["Delhi-NCR (Gurgaon)"],
        "primary_stack": ["Python", "Go (Golang)", "React.js", "Distributed Systems", "FastAPI", "Redis & Caching"],
        "summary": "Flagship tech employer in Gurgaon (North); rapid product iterations across Zomato and Blinkit quick-commerce."
    },
    "Razorpay": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.88,
        "bonus_pct": 0.14,
        "stock_equity_pct": 0.22,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (Fintech Reliability, 99.999% SLA Systems, High-Level Design)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Go (Golang)", "AWS (Amazon Web Services)", "Kubernetes", "System Design", "Microservices", "SQL & Relational Databases"],
        "summary": "India's payment gateway powerhouse; benchmark compensation, engineering excellence in financial infrastructure."
    },
    "CRED": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.90,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.25,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (Design Craft, Reactive Systems, High Concurrency)",
        "locations": ["Bengaluru"],
        "primary_stack": ["React.js", "React Native", "Go (Golang)", "AWS (Amazon Web Services)", "Redis & Caching", "System Design"],
        "summary": "Renowned for top 95th-percentile compensation packages, sleek UI/UX, and high talent density."
    },
    "PhonePe": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.85,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.22,
        "interview_difficulty": 4.5,
        "hiring_bar": "Very High (UPI Scale, Low Latency, Cassandra/Kafka Mastery)",
        "locations": ["Bengaluru", "Pune"],
        "primary_stack": ["Java", "Apache Kafka", "Distributed Systems", "System Design", "Microservices", "Spring Boot"],
        "summary": "Processes billions of UPI transactions monthly; exceptionally robust distributed systems engineering."
    },
    "Zepto": {
        "tier": "Tier 1 - Indian Tech Unicorns",
        "multiplier": 1.76,
        "bonus_pct": 0.10,
        "stock_equity_pct": 0.24,
        "interview_difficulty": 4.3,
        "hiring_bar": "High (Hyper-growth, Real-time Supply Chain Optimization)",
        "locations": ["Bengaluru", "Mumbai"],
        "primary_stack": ["Go (Golang)", "React.js", "Next.js", "Redis & Caching", "AWS (Amazon Web Services)", "Microservices"],
        "summary": "Hyper-growth quick commerce company; high-pace environment with attractive equity components."
    },

    # Tier 1 - FinTech & Global Capability Centers (GCCs)
    "Goldman Sachs": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.95,
        "bonus_pct": 0.25,
        "stock_equity_pct": 0.15,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (DSA, Math/Quant logic, Low Latency, Systems)",
        "locations": ["Bengaluru", "Hyderabad"],
        "primary_stack": ["Java", "Python", "C++", "Spring Boot", "Cybersecurity & AppSec", "SQL & Relational Databases"],
        "summary": "Industry-leading cash bonuses, prestigious Wall Street financial technology center in Bengaluru."
    },
    "Morgan Stanley": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.90,
        "bonus_pct": 0.24,
        "stock_equity_pct": 0.15,
        "interview_difficulty": 4.5,
        "hiring_bar": "Very High (Low-latency Linux, C++/Java, Algorithmic Trading Systems)",
        "locations": ["Mumbai", "Bengaluru"],
        "primary_stack": ["Java", "C++", "Distributed Systems", "Python", "Linux", "SQL & Relational Databases"],
        "summary": "Premier investment bank with major technology hubs in Mumbai and Bengaluru, heavy quant/trading focus."
    },
    "JP Morgan Chase": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.82,
        "bonus_pct": 0.20,
        "stock_equity_pct": 0.12,
        "interview_difficulty": 4.4,
        "hiring_bar": "High (Object-Oriented Design, Security, Cloud Native Migration)",
        "locations": ["Bengaluru", "Mumbai", "Hyderabad"],
        "primary_stack": ["Java", "Python", "React.js", "AWS (Amazon Web Services)", "Microservices", "Cybersecurity & AppSec"],
        "summary": "Global banking behemoth with tens of thousands of technologists in India; very stable and competitive comp."
    },
    "Atlassian": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 2.10,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.28,
        "interview_difficulty": 4.7,
        "hiring_bar": "Very High (Values & Craft, High-Level System Architecture, Distributed Cloud)",
        "locations": ["Bengaluru", "Remote / Pan-India"],
        "primary_stack": ["Java", "React.js", "AWS (Amazon Web Services)", "Docker", "Kubernetes", "System Design"],
        "summary": "Exceptional work-life balance, top-tier compensation, 'Team Anywhere' flexible remote policy."
    },
    "Adobe": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.95,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.25,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (Computer Vision, Complex Algorithms, C++/Cloud)",
        "locations": ["Delhi-NCR (Noida)", "Bengaluru"],
        "primary_stack": ["C++", "Java", "Python", "Machine Learning & Data Science", "Generative AI & LLMs", "AWS (Amazon Web Services)"],
        "summary": "Flagship engineering presence in Noida; creative cloud, document cloud, generative AI (Firefly) research."
    },
    "Salesforce": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.90,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.24,
        "interview_difficulty": 4.5,
        "hiring_bar": "High (Multi-tenant Cloud Architecture, Big Data, API Scale)",
        "locations": ["Hyderabad", "Bengaluru"],
        "primary_stack": ["Java", "React.js", "AWS (Amazon Web Services)", "Distributed Systems", "Kubernetes"],
        "summary": "Huge state-of-the-art campus in Hyderabad; renowned for employee benefits and enterprise cloud scale."
    },
    "Intuit": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.92,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.25,
        "interview_difficulty": 4.6,
        "hiring_bar": "Very High (Design for Delight, Clean Code, Scalable Fintech Platforms)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Java", "React.js", "AWS (Amazon Web Services)", "Kubernetes", "Generative AI & LLMs", "Microservices"],
        "summary": "Consistently rated among the best tech employers in India; builders of TurboTax, QuickBooks, and Credit Karma."
    },
    "Cisco": {
        "tier": "Tier 1 - FinTech & Elite GCCs",
        "multiplier": 1.65,
        "bonus_pct": 0.15,
        "stock_equity_pct": 0.18,
        "interview_difficulty": 4.2,
        "hiring_bar": "High (Networking, Systems, Cloud Security, Linux Kernels)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Python", "C++", "Linux", "Cybersecurity & AppSec", "Docker", "Kubernetes"],
        "summary": "Massive R&D campus in Bengaluru; leader in networking hardware, telecommunications, and cybersecurity."
    },

    # Tier 2 - Scaled Product Companies & Unicorn Challengers
    "Postman": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.75,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.20,
        "interview_difficulty": 4.4,
        "hiring_bar": "High (API Design, JavaScript/TypeScript mastery, Developer Empathy)",
        "locations": ["Bengaluru", "Remote / Pan-India"],
        "primary_stack": ["JavaScript / TypeScript", "Node.js & Express", "React.js", "Docker", "AWS (Amazon Web Services)", "Next.js"],
        "summary": "Global leader in API development platforms, founded in India with international dev-tool adoption."
    },
    "BrowserStack": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.72,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.20,
        "interview_difficulty": 4.4,
        "hiring_bar": "High (Operating Systems, Cloud Virtualization, Distributed Test Runners)",
        "locations": ["Mumbai", "Remote / Pan-India"],
        "primary_stack": ["Python", "Docker", "Kubernetes", "AWS (Amazon Web Services)", "Go (Golang)", "Rust"],
        "summary": "Profitable global SaaS powerhouse originating from Mumbai; builds real-device cloud test infrastructure."
    },
    "Groww": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.70,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.18,
        "interview_difficulty": 4.3,
        "hiring_bar": "High (High Concurrency, Fintech Brokerage Scale, Reactive UI)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Go (Golang)", "React.js", "Microservices", "Apache Kafka", "Redis & Caching", "Docker"],
        "summary": "India's largest stockbroker by active clients; high-pace fintech environment and modern Go/React stack."
    },
    "Zerodha": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.75,
        "bonus_pct": 0.25,
        "stock_equity_pct": 0.10,
        "interview_difficulty": 4.5,
        "hiring_bar": "Very High (Frugal Engineering, Open Source, Extreme Performance)",
        "locations": ["Bengaluru", "Remote / Pan-India"],
        "primary_stack": ["Go (Golang)", "Python", "SQL & Relational Databases", "Flutter", "Linux", "System Design"],
        "summary": "Legendary lean engineering team (only ~35 engineers handling 15% of Indian retail trading volume); ultra-high cash bonuses."
    },
    "Meesho": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.68,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.18,
        "interview_difficulty": 4.3,
        "hiring_bar": "High (Big Data Spark, Cost-optimized Cloud Scale, E-commerce)",
        "locations": ["Bengaluru"],
        "primary_stack": ["Java", "Python", "Apache Spark", "Apache Kafka", "Kubernetes", "AWS (Amazon Web Services)"],
        "summary": "Pioneered mass-market zero-commission e-commerce; big data and recommendation systems heavy."
    },
    "Freshworks": {
        "tier": "Tier 2 - Scaled Product & Growth",
        "multiplier": 1.62,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.18,
        "interview_difficulty": 4.2,
        "hiring_bar": "High (Multi-tenant SaaS Architecture, Clean Code, Product Sense)",
        "locations": ["Chennai", "Bengaluru"],
        "primary_stack": ["React.js", "AWS (Amazon Web Services)", "Java", "Python", "SQL & Relational Databases"],
        "summary": "Nasdaq-listed global SaaS player anchored in Chennai; enterprise customer experience products."
    },

    # Tier 3 - Global IT Services & Consulting (Mass Recruiters & Delivery Leaders)
    "TCS (Tata Consultancy Services)": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.88,
        "bonus_pct": 0.10,
        "stock_equity_pct": 0.02,
        "interview_difficulty": 3.2,
        "hiring_bar": "Moderate (Aptitude, Core Java/Python, RDBMS, Domain)",
        "locations": ["Pan-India (Mumbai, Bengaluru, Chennai, Hyderabad, Delhi-NCR, Kolkata, Pune)"],
        "primary_stack": ["Java", "Spring Boot", "SQL & Relational Databases", "Python", "AWS (Amazon Web Services)", "Azure"],
        "summary": "India's largest IT employer; stable careers, vast enterprise clients, digital wings (TCS Digital/Innovator) pay higher."
    },
    "Infosys": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.88,
        "bonus_pct": 0.10,
        "stock_equity_pct": 0.02,
        "interview_difficulty": 3.2,
        "hiring_bar": "Moderate (Programming Logic, OOPs, Web Basics)",
        "locations": ["Pan-India (Bengaluru, Pune, Hyderabad, Chennai, Chandigarh, Mysore)"],
        "primary_stack": ["Java", "Spring Boot", "React.js", "Python", "Azure", "Cloud & DevOps"],
        "summary": "Global digital services giant; specialist tracks (Power Programmer / DSE) offer 2x-3x entry packages."
    },
    "Wipro": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.86,
        "bonus_pct": 0.08,
        "stock_equity_pct": 0.02,
        "interview_difficulty": 3.1,
        "hiring_bar": "Moderate (Core Concepts, Engineering Basics, Project Experience)",
        "locations": ["Pan-India (Bengaluru, Chennai, Hyderabad, Pune, Delhi-NCR)"],
        "primary_stack": ["Java", "SQL & Relational Databases", "Cloud & DevOps", "Automation Testing (Selenium/Playwright)"],
        "summary": "Massive enterprise footprint in infrastructure management, business cloud migration, and QA engineering."
    },
    "Accenture": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.98,
        "bonus_pct": 0.12,
        "stock_equity_pct": 0.04,
        "interview_difficulty": 3.5,
        "hiring_bar": "Moderate-High (Problem Solving, Cloud Certifications, Consulting Skills)",
        "locations": ["Pan-India (Bengaluru, Mumbai, Delhi-NCR, Hyderabad, Pune, Chennai)"],
        "primary_stack": ["AWS (Amazon Web Services)", "Azure", "Java", "Python", "Data Engineering", "Microservices"],
        "summary": "Top-tier consulting and strategy operations with massive engineering transformation centers across metros."
    },
    "Cognizant": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.88,
        "bonus_pct": 0.10,
        "stock_equity_pct": 0.02,
        "interview_difficulty": 3.2,
        "hiring_bar": "Moderate (Data structures, SQL, Frameworks)",
        "locations": ["Pan-India (Chennai, Kolkata, Bengaluru, Hyderabad, Pune)"],
        "primary_stack": ["Java", "React.js", "SQL & Relational Databases", "Azure", "Automation Testing (Selenium/Playwright)"],
        "summary": "Heavy presence in Chennai and Kolkata; major healthcare and life sciences client base."
    },
    "LTIMindtree": {
        "tier": "Tier 3 - Global IT Services & Consulting",
        "multiplier": 0.92,
        "bonus_pct": 0.10,
        "stock_equity_pct": 0.02,
        "interview_difficulty": 3.4,
        "hiring_bar": "Moderate (Full Stack, Microservices, Cloud)",
        "locations": ["Pan-India (Mumbai, Bengaluru, Pune, Chennai, Hyderabad)"],
        "primary_stack": ["Java", "Microservices", "Spring Boot", "React.js", "AWS (Amazon Web Services)"],
        "summary": "Mid-tier IT champion merged under L&T group, known for competitive engineering project delivery."
    }
}


# ==============================================================================
# 3. BASE NATIONAL SALARY SCALE BY ROLE AND YEARS OF EXPERIENCE
# ==============================================================================
# Baseline national CTC in INR Lakhs (for standard tier-2 tech product company)
ROLE_EXPERIENCE_CURVES = {
    "Software Engineer (Backend / Full Stack)": {
        "base_at_0": 6.5,
        "growth_factor": 1.28,
        "description": "API design, business logic, system scalability, database tuning."
    },
    "AI / Machine Learning Engineer": {
        "base_at_0": 8.5,
        "growth_factor": 1.34,
        "description": "Model training, LLM fine-tuning, RAG pipelines, production ML serving."
    },
    "Cloud & DevOps / Platform Engineer": {
        "base_at_0": 7.0,
        "growth_factor": 1.30,
        "description": "Kubernetes orchestration, CI/CD, cloud infra automation, reliability engineering."
    },
    "Data Engineer & Big Data Architect": {
        "base_at_0": 7.2,
        "growth_factor": 1.29,
        "description": "Distributed data pipelines, Spark, Kafka, lakehouse architecture."
    },
    "Frontend & Web Engineer": {
        "base_at_0": 6.0,
        "growth_factor": 1.25,
        "description": "Responsive UI, client-side state, modern React/Next.js frameworks."
    },
    "Mobile App Engineer (iOS / Android)": {
        "base_at_0": 6.2,
        "growth_factor": 1.26,
        "description": "Cross-platform Flutter/React Native or native Swift/Kotlin architectures."
    },
    "Technical Product Manager (TPM)": {
        "base_at_0": 10.0,
        "growth_factor": 1.32,
        "description": "Product strategy, roadmap delivery, tech-business alignment, metrics."
    },
    "Cybersecurity & AppSec Engineer": {
        "base_at_0": 7.5,
        "growth_factor": 1.31,
        "description": "Zero trust, vulnerability testing, SOC operations, cloud governance."
    },
    "QA / Test Automation Engineer": {
        "base_at_0": 4.8,
        "growth_factor": 1.20,
        "description": "Automated regression testing, Playwright, Selenium, performance load tests."
    }
}

# Education pedigree adjustments
EDUCATION_TIERS = {
    "Tier 1 (IIT / BITS / NIT / Top IIIT)": 1.35,
    "Tier 2 (Good State Govt / Top Private Universities)": 1.10,
    "Tier 3 (Standard Engineering Colleges)": 0.95,
    "Non-CS / Self-Taught / Bootcamp with Strong Portfolio": 1.05
}

def get_company_names():
    return sorted(list(COMPANIES_DATA.keys()))

def get_company_tiers():
    return sorted(list(set(c["tier"] for c in COMPANIES_DATA.values())))

def get_role_names():
    return sorted(list(ROLE_EXPERIENCE_CURVES.keys()))
