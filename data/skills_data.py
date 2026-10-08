"""
Skills Database and Taxonomy for Tech Salary Intelligence.
Includes demand scores, salary multipliers, top hiring companies, and regional hotspots.
"""

SKILLS_DATA = {
    # System Architecture & Core Engineering
    "System Design": {
        "category": "Architecture & Systems",
        "demand_score": 9.8,
        "salary_boost_pct": 0.22,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)"],
        "target_companies": ["Google", "Amazon", "Uber", "Flipkart", "Razorpay", "Swiggy"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 10,
        "synergies": ["Distributed Systems", "Microservices", "Apache Kafka"],
        "description": "High-level architecture, scalability, CAP theorem, caching, load balancing, sharding."
    },
    "Distributed Systems": {
        "category": "Architecture & Systems",
        "demand_score": 9.6,
        "salary_boost_pct": 0.20,
        "primary_regions": ["South (Bengaluru)", "West (Mumbai)", "South (Hyderabad)"],
        "target_companies": ["Google", "Uber", "Microsoft", "PhonePe", "Morgan Stanley"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 12,
        "synergies": ["System Design", "Go (Golang)", "Apache Kafka"],
        "description": "Consensus algorithms (Raft/Paxos), fault tolerance, distributed transactions."
    },
    "Microservices": {
        "category": "Architecture & Systems",
        "demand_score": 9.2,
        "salary_boost_pct": 0.14,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Pune)"],
        "target_companies": ["Amazon", "Swiggy", "Zomato", "JP Morgan", "Paytm"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Docker", "Kubernetes", "Spring Boot", "Go (Golang)"],
        "description": "Decomposed domain-driven services, API gateway, service mesh, event choreography."
    },

    # AI, ML & GenAI
    "Generative AI & LLMs": {
        "category": "AI & Machine Learning",
        "demand_score": 9.9,
        "salary_boost_pct": 0.28,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)"],
        "target_companies": ["Google", "Microsoft", "Meta", "Adobe", "Flipkart", "Postman"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 8,
        "synergies": ["PyTorch", "Python", "Vector Databases", "LangChain"],
        "description": "RAG pipelines, Fine-tuning, LangChain, LlamaIndex, embeddings, agentic workflows."
    },
    "PyTorch": {
        "category": "AI & Machine Learning",
        "demand_score": 9.3,
        "salary_boost_pct": 0.18,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)"],
        "target_companies": ["Google", "Meta", "NVIDIA", "Amazon", "Microsoft"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 10,
        "synergies": ["Python", "Generative AI & LLMs", "TensorFlow"],
        "description": "Deep learning model training, neural architectures, GPU optimization."
    },
    "TensorFlow": {
        "category": "AI & Machine Learning",
        "demand_score": 8.7,
        "salary_boost_pct": 0.13,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)"],
        "target_companies": ["Google", "Uber", "Samsung R&D", "TCS", "Accenture"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 8,
        "synergies": ["Python", "PyTorch"],
        "description": "Production ML models, TF Serving, edge ML deployment."
    },
    "Machine Learning & Data Science": {
        "category": "AI & Machine Learning",
        "demand_score": 9.0,
        "salary_boost_pct": 0.16,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Mumbai)"],
        "target_companies": ["Flipkart", "Zomato", "Goldman Sachs", "Swiggy", "InMobi"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 8,
        "synergies": ["Python", "SQL", "PyTorch"],
        "description": "Predictive modeling, regression, classification, clustering, feature engineering."
    },

    # Core Programming Languages
    "Go (Golang)": {
        "category": "Programming Languages",
        "demand_score": 9.5,
        "salary_boost_pct": 0.18,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Mumbai)"],
        "target_companies": ["Uber", "Razorpay", "Swiggy", "Zerodha", "CRED", "Google"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Kubernetes", "Docker", "Microservices", "Distributed Systems"],
        "description": "High-concurrency microservices, goroutines, low-latency networked backends."
    },
    "Rust": {
        "category": "Programming Languages",
        "demand_score": 9.4,
        "salary_boost_pct": 0.22,
        "primary_regions": ["South (Bengaluru)", "West (Mumbai)"],
        "target_companies": ["Microsoft", "AWS", "Coinbase", "HFT Firms", "BrowserStack"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 12,
        "synergies": ["System Design", "Distributed Systems"],
        "description": "Memory-safe systems programming, ultra-high performance, WebAssembly."
    },
    "Python": {
        "category": "Programming Languages",
        "demand_score": 9.6,
        "salary_boost_pct": 0.12,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)", "West (Pune)"],
        "target_companies": ["Google", "Meta", "Amazon", "Goldman Sachs", "Zomato"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["FastAPI", "Generative AI & LLMs", "PyTorch", "SQL"],
        "description": "Versatile backend, data science, automation, AI pipelines."
    },
    "Java": {
        "category": "Programming Languages",
        "demand_score": 9.3,
        "salary_boost_pct": 0.12,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)", "South (Chennai)"],
        "target_companies": ["Amazon", "Flipkart", "Goldman Sachs", "Morgan Stanley", "PhonePe", "TCS"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Spring Boot", "Microservices", "Apache Kafka", "SQL"],
        "description": "Enterprise grade backend, JVM performance, high-throughput systems."
    },
    "C++": {
        "category": "Programming Languages",
        "demand_score": 9.1,
        "salary_boost_pct": 0.17,
        "primary_regions": ["West (Mumbai)", "South (Bengaluru)", "South (Hyderabad)"],
        "target_companies": ["Tower Research", "Graviton", "Adobe", "Google", "Samsung R&D"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 10,
        "synergies": ["Distributed Systems", "Rust"],
        "description": "Low-latency systems, quant finance, game engines, embedded/systems software."
    },
    "JavaScript / TypeScript": {
        "category": "Programming Languages",
        "demand_score": 9.2,
        "salary_boost_pct": 0.10,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Pune)"],
        "target_companies": ["Postman", "Razorpay", "CRED", "Swiggy", "Microsoft"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["React.js", "Node.js", "Next.js"],
        "description": "Modern full-stack web development, typed enterprise codebases."
    },

    # Cloud & DevOps Infrastructure
    "Kubernetes": {
        "category": "Cloud & DevOps",
        "demand_score": 9.6,
        "salary_boost_pct": 0.19,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)"],
        "target_companies": ["Google", "AWS", "Atlassian", "BrowserStack", "Razorpay"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 7,
        "synergies": ["Docker", "AWS", "Terraform", "Go (Golang)"],
        "description": "Container orchestration, ingress controllers, helm charts, service mesh."
    },
    "AWS (Amazon Web Services)": {
        "category": "Cloud & DevOps",
        "demand_score": 9.4,
        "salary_boost_pct": 0.14,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)", "West (Mumbai)"],
        "target_companies": ["Amazon", "Razorpay", "Swiggy", "Postman", "Freshworks"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Terraform", "Docker", "Kubernetes"],
        "description": "Cloud native architecture, ECS/EKS, Lambda, S3, RDS, CloudFront."
    },
    "Azure": {
        "category": "Cloud & DevOps",
        "demand_score": 9.0,
        "salary_boost_pct": 0.12,
        "primary_regions": ["South (Hyderabad)", "South (Bengaluru)", "West (Pune)", "South (Chennai)"],
        "target_companies": ["Microsoft", "Accenture", "TCS", "Infosys", "EY"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Docker", "Kubernetes", "C# / .NET"],
        "description": "Enterprise cloud migrations, AKS, Azure DevOps, cloud governance."
    },
    "GCP (Google Cloud)": {
        "category": "Cloud & DevOps",
        "demand_score": 8.8,
        "salary_boost_pct": 0.13,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "North (Delhi-NCR)"],
        "target_companies": ["Google", "Flipkart", "ShareChat", "Zomato"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["BigQuery", "Kubernetes", "Python"],
        "description": "BigQuery, GKE, Vertex AI, global infrastructure."
    },
    "Terraform & IaC": {
        "category": "Cloud & DevOps",
        "demand_score": 9.1,
        "salary_boost_pct": 0.14,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)"],
        "target_companies": ["Atlassian", "BrowserStack", "Uber", "Razorpay"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 5,
        "synergies": ["AWS", "Azure", "Kubernetes"],
        "description": "Infrastructure as Code, multi-cloud provisioning, state management."
    },
    "Docker": {
        "category": "Cloud & DevOps",
        "demand_score": 8.9,
        "salary_boost_pct": 0.08,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "South (Hyderabad)"],
        "target_companies": ["All Modern Tech Companies"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 3,
        "synergies": ["Kubernetes", "CI/CD", "AWS"],
        "description": "Containerization, image optimization, multi-stage builds."
    },
    "CI/CD Pipelines": {
        "category": "Cloud & DevOps",
        "demand_score": 8.7,
        "salary_boost_pct": 0.09,
        "primary_regions": ["South (Bengaluru)", "West (Pune)", "South (Chennai)"],
        "target_companies": ["Atlassian", "Accenture", "Infosys", "Freshworks"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["Docker", "AWS", "Git"],
        "description": "GitHub Actions, GitLab CI, automated test gates, zero-downtime deployment."
    },

    # Data Engineering & Messaging
    "Apache Kafka": {
        "category": "Data & Messaging",
        "demand_score": 9.5,
        "salary_boost_pct": 0.18,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Mumbai)"],
        "target_companies": ["Uber", "Flipkart", "Swiggy", "PhonePe", "Goldman Sachs"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["System Design", "Distributed Systems", "Java", "Go (Golang)"],
        "description": "Event streaming, high throughput pub/sub, stream processing, Kafka Connect."
    },
    "Apache Spark": {
        "category": "Data & Messaging",
        "demand_score": 9.2,
        "salary_boost_pct": 0.16,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)"],
        "target_companies": ["Walmart Global Tech", "Flipkart", "InMobi", "JPMorgan Chase"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 7,
        "synergies": ["Python", "SQL", "Data Engineering"],
        "description": "Large-scale distributed batch and stream computation, PySpark, Databricks."
    },
    "Redis & Caching": {
        "category": "Data & Messaging",
        "demand_score": 9.0,
        "salary_boost_pct": 0.11,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)"],
        "target_companies": ["Swiggy", "Zomato", "CRED", "Razorpay"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 3,
        "synergies": ["System Design", "Node.js", "Python", "Go (Golang)"],
        "description": "In-memory data structures, caching strategies, rate limiting, pub/sub."
    },
    "SQL & Relational Databases": {
        "category": "Data & Messaging",
        "demand_score": 9.3,
        "salary_boost_pct": 0.08,
        "primary_regions": ["All Regions"],
        "target_companies": ["All Tech Companies"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["PostgreSQL", "Python", "Data Engineering"],
        "description": "PostgreSQL/MySQL schema design, indexing, query optimization, EXPLAIN analysis."
    },
    "NoSQL & MongoDB": {
        "category": "Data & Messaging",
        "demand_score": 8.6,
        "salary_boost_pct": 0.08,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "South (Chennai)"],
        "target_companies": ["Freshworks", "Paytm", "Swiggy", "TCS"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 3,
        "synergies": ["Node.js", "System Design"],
        "description": "Document storage, horizontal scaling, sharding, replication."
    },

    # Backend Frameworks
    "Spring Boot": {
        "category": "Backend Frameworks",
        "demand_score": 9.2,
        "salary_boost_pct": 0.11,
        "primary_regions": ["South (Bengaluru)", "South (Hyderabad)", "West (Pune)", "South (Chennai)"],
        "target_companies": ["Amazon", "Goldman Sachs", "Flipkart", "Morgan Stanley", "TCS"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 5,
        "synergies": ["Java", "Microservices", "Apache Kafka"],
        "description": "Enterprise Java framework, Spring Security, Spring Cloud, Hibernate/JPA."
    },
    "Node.js & Express": {
        "category": "Backend Frameworks",
        "demand_score": 9.0,
        "salary_boost_pct": 0.09,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Pune)"],
        "target_companies": ["Postman", "CRED", "Razorpay", "Swiggy"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["JavaScript / TypeScript", "React.js", "Redis & Caching"],
        "description": "Asynchronous event-driven I/O, REST APIs, GraphQL, microservices."
    },
    "FastAPI": {
        "category": "Backend Frameworks",
        "demand_score": 8.9,
        "salary_boost_pct": 0.11,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)"],
        "target_companies": ["Microsoft", "Zomato", "Swiggy", "AI Startups"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 3,
        "synergies": ["Python", "Generative AI & LLMs", "Docker"],
        "description": "High-performance async Python APIs, Pydantic validation, AI model serving."
    },
    "Django": {
        "category": "Backend Frameworks",
        "demand_score": 8.4,
        "salary_boost_pct": 0.07,
        "primary_regions": ["North (Delhi-NCR)", "South (Bengaluru)"],
        "target_companies": ["Zomato", "PolicyBazaar", "Instagram/Meta"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["Python", "SQL & Relational Databases"],
        "description": "Batteries-included web framework, ORM, authentication, Django REST framework."
    },

    # Frontend & Mobile
    "React.js": {
        "category": "Frontend & Mobile",
        "demand_score": 9.3,
        "salary_boost_pct": 0.10,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Pune)", "South (Hyderabad)"],
        "target_companies": ["Meta", "CRED", "Flipkart", "Atlassian", "Swiggy"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 5,
        "synergies": ["JavaScript / TypeScript", "Next.js", "Node.js & Express"],
        "description": "Component architecture, hooks, state management (Zustand/Redux), SSR."
    },
    "Next.js": {
        "category": "Frontend & Mobile",
        "demand_score": 9.1,
        "salary_boost_pct": 0.12,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)"],
        "target_companies": ["Vercel partners", "CRED", "Zepto", "Groww"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 4,
        "synergies": ["React.js", "JavaScript / TypeScript"],
        "description": "App Router, Server Components, SEO optimization, full-stack Next apps."
    },
    "React Native": {
        "category": "Frontend & Mobile",
        "demand_score": 8.8,
        "salary_boost_pct": 0.12,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)"],
        "target_companies": ["CRED", "CoinDCX", "Flipkart", "Zomato"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["React.js", "JavaScript / TypeScript"],
        "description": "Cross-platform mobile apps for iOS and Android, native bridges."
    },
    "Flutter": {
        "category": "Frontend & Mobile",
        "demand_score": 8.5,
        "salary_boost_pct": 0.11,
        "primary_regions": ["South (Bengaluru)", "North (Delhi-NCR)", "West (Pune)"],
        "target_companies": ["Zerodha", "Google", "Alibaba", "Tencent"],
        "learning_difficulty": "Intermediate",
        "weeks_to_learn": 6,
        "synergies": ["Dart", "Mobile Architecture"],
        "description": "Cross-platform mobile & desktop, Dart runtime, custom rendering engine."
    },

    # Security & Quality
    "Cybersecurity & AppSec": {
        "category": "Security & Quality",
        "demand_score": 9.2,
        "salary_boost_pct": 0.18,
        "primary_regions": ["West (Mumbai)", "South (Bengaluru)", "South (Hyderabad)"],
        "target_companies": ["Goldman Sachs", "JP Morgan", "Cisco", "Paytm", "Palo Alto Networks"],
        "learning_difficulty": "Advanced",
        "weeks_to_learn": 10,
        "synergies": ["Linux", "Cloud & DevOps", "Python"],
        "description": "Threat modeling, OWASP, penetration testing, IAM, zero-trust architecture."
    },
    "Automation Testing (Selenium/Playwright)": {
        "category": "Security & Quality",
        "demand_score": 8.1,
        "salary_boost_pct": 0.06,
        "primary_regions": ["South (Chennai)", "West (Pune)", "South (Hyderabad)", "North (Noida)"],
        "target_companies": ["BrowserStack", "TCS", "Cognizant", "Infosys", "Accenture"],
        "learning_difficulty": "Beginner",
        "weeks_to_learn": 4,
        "synergies": ["Python", "Java", "CI/CD Pipelines"],
        "description": "End-to-end test automation, API testing, performance load testing."
    }
}

# Skill categories helper
CATEGORIES = sorted(list(set(s["category"] for s in SKILLS_DATA.values())))

def get_skills_by_category():
    grouped = {}
    for skill, info in SKILLS_DATA.items():
        cat = info["category"]
        grouped.setdefault(cat, []).append(skill)
    return grouped
