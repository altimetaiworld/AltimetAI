# app/services.py

class ContentService:
    """Mock database and service layer for website copy and content structures."""
    
    @staticmethod
    def get_services():
        return [
            {
                "id": "ai-data-copilot",
                "slug": "ai-data-copilot",
                "name": "AI Data Copilot",
                "tagline": "Conversational Business Intelligence & SQL Generation",
                "icon": "database",
                "short_description": "Bridge the gap between raw data and business users. Query complex warehouses in natural language with production-grade SQL generation.",
                "overview": (
                    "Altimet AI Data Copilot transforms how enterprise teams interact with their structured data. "
                    "By leveraging advanced language models fine-tuned on custom schemas, it allows business analysts, "
                    "executives, and operations teams to ask complex analytics questions in plain language and receive "
                    "accurate SQL, verified tables, and beautiful visualization recommendations in milliseconds."
                ),
                "business_problems": [
                    "Data analysts spending 60%+ of their time writing repetitive SQL queries for business teams.",
                    "Siloed analytical tools resulting in delayed decision-making and dated dashboard exports.",
                    "Executive teams unable to get ad-hoc visual insights without relying on BI tickets."
                ],
                "solution": (
                    "We build custom AI schema mappers and semantic translators that securely connect to your "
                    "Snowflake, BigQuery, or Postgres warehouse. The system translates questions to SQL, runs them within "
                    "a secure sandbox, verifies the results through an automated validation layer, and outputs clean data formats."
                ),
                "benefits": [
                    {"label": "Reporting Time Reduction", "value": "80%"},
                    {"label": "Query Accuracy Rate", "value": "99.4%"},
                    {"label": "Self-Service Adoption", "value": "4.2x"}
                ],
                "architecture_steps": [
                    {"title": "Schema Parsing", "desc": "Extracts database schema, foreign keys, and descriptions into a metadata graph."},
                    {"title": "Semantic Translator", "desc": "Maps business terminology to physical schema column and table identifiers."},
                    {"title": "Validation Sandbox", "desc": "Executes query safely, verifies SQL syntax and bounds check before delivery."},
                    {"title": "Visualizer Engine", "desc": "Suggests optimal chart representation (bar, line, scatter) for output datasets."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Discovery", "duration": "Weeks 1-2", "details": "Database schema audit, permissioning setups, and defining core business glossary."},
                    {"phase": "Phase 2: Semantic Tuning", "desc": "Building custom metadata graphs and optimizing SQL generation weights on golden datasets.", "duration": "Weeks 3-5"},
                    {"phase": "Phase 3: Integration", "desc": "Connecting with corporate Slack, MS Teams, or embedding within existing BI dashboards.", "duration": "Weeks 6-8"},
                    {"phase": "Phase 4: Deployment & QA", "desc": "Shadow running alongside analysts, user acceptance testing, and final security hardening.", "duration": "Weeks 9-10"}
                ],
                "faq": [
                    {
                        "q": "Does Altimet AI copy or store our source database records?",
                        "a": "No. The AI Data Copilot only reads schema definitions and metadata graphs. When queries are run, database access is performed via secure credentials with read-only access directly inside your VPC. No database rows ever leave your environment."
                    },
                    {
                        "q": "How does the copilot handle database schema changes?",
                        "a": "Our system includes an automated schema synchronization engine that listens to database DDL changes. Schema shifts trigger an automated test suite that validates the AI's understanding of the new columns."
                    }
                ]
            },
            {
                "id": "knowledge-copilot",
                "slug": "knowledge-copilot",
                "name": "Enterprise Knowledge Copilot",
                "tagline": "Semantic Search & Synthesis Across Dispersed Systems",
                "icon": "book-open",
                "short_description": "Consolidate and query internal wikis, PDFs, contracts, and codebases. Get accurate answers with complete source citations.",
                "overview": (
                    "Enterprise information is usually scattered across Slack, Notion, Google Drive, and PDFs. "
                    "The Knowledge Copilot connects these disjointed documentation repositories, building an "
                    "enterprise-wide semantic knowledge graph that allows users to perform deep semantic searches, "
                    "generate synthesis summaries, and extract structured facts with references back to source materials."
                ),
                "business_problems": [
                    "Employees losing hours daily searching for internal policy documents, product specs, and guides.",
                    "Onboarding bottlenecks where new hires must ask colleagues questions covered in static wikis.",
                    "Risk of relying on outdated SOPs, resulting in operational errors and compliance exposure."
                ],
                "solution": (
                    "We design a state-of-the-art Retrieval-Augmented Generation (RAG) platform. By implementing "
                    "hierarchical document chunking, multi-stage reranking, and semantic vector indexing, we achieve "
                    "unmatched citation accuracy and eliminate hallucinations, providing reliable, secure access to enterprise IP."
                ),
                "benefits": [
                    {"label": "Time Spent Searching", "value": "-65%"},
                    {"label": "Answer Accuracy", "value": "98.8%"},
                    {"label": "New Hire Ramp Time", "value": "-30%"}
                ],
                "architecture_steps": [
                    {"title": "Document Connectors", "desc": "Ingests docs from Notion, Drive, Confluence, and internal servers in real time."},
                    {"title": "Hierarchical Chunking", "desc": "Splits documents logically to retain contextual links between parents and children."},
                    {"title": "Vector Embedding", "desc": "Converts text blocks into high-dimensional vectors for semantic indexing."},
                    {"title": "Reranking Layer", "desc": "Sorts retrieved chunks based on domain-specific keyword relevance and user context."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Connection", "duration": "Weeks 1-2", "details": "Configure API read permissions for Notion, Jira, Drive, and PDF servers."},
                    {"phase": "Phase 2: Embedding & Indexing", "desc": "Creating vector databases using Qdrant or Pinecone with semantic indexing.", "duration": "Weeks 3-4"},
                    {"phase": "Phase 3: LLM Optimization", "desc": "Prompt tuning and system instruction alignment with company safety guardrails.", "duration": "Weeks 5-6"},
                    {"phase": "Phase 4: User Rollout", "desc": "Deploying internal web app and Slack bot; training team on prompting.", "duration": "Weeks 7-8"}
                ],
                "faq": [
                    {
                        "q": "How does the system respect file permissions?",
                        "a": "Our platform mirrors ACL (Access Control Lists) dynamically. If a user does not have permission to view a contract in Google Drive, the Knowledge Copilot automatically excludes that source document from their search results."
                    },
                    {
                        "q": "Can it search scanned PDF files or tables?",
                        "a": "Yes. We implement an advanced OCR (Optical Character Recognition) pipeline combined with layout parsing models to accurately extract data from scanned documents, diagrams, and financial tables."
                    }
                ]
            },
            {
                "id": "ai-agents",
                "slug": "ai-agents",
                "name": "AI Agent Systems",
                "tagline": "Autonomous Workflows & Multi-Agent Coordination",
                "icon": "cpu",
                "short_description": "Deploy self-correcting agents built on LangGraph to automate complex operations, customer support, and research tasks.",
                "overview": (
                    "Unlike simple conversational bots, AI Agent Systems are autonomous code executions that run "
                    "goal-directed workflows. We design multi-agent systems using framework standards like LangGraph. "
                    "These agents collaborate, call API tools, verify their own work, and escalate to human operators "
                    "only when encountering exceptional cases."
                ),
                "business_problems": [
                    "Manual operational workflows involving copying and pasting data across software portals.",
                    "Repetitive, high-volume customer service requests draining support staff resources.",
                    "Delayed response times on booking, lead qualification, and document compliance checks."
                ],
                "solution": (
                    "We develop stateful, resilient multi-agent graphs. One agent specializes in document parsing, "
                    "another in database lookups, and a supervisor agent orchestrates tasks, reviews outputs, and "
                    "coordinates external API integrations with complete auditability."
                ),
                "benefits": [
                    {"label": "Operational Efficiency", "value": "+75%"},
                    {"label": "Response Time Latency", "value": "-95%"},
                    {"label": "Human Hand-off Rate", "value": "<8%"}
                ],
                "architecture_steps": [
                    {"title": "Agent Graph", "desc": "Maps state definitions and transitions between specialized agent nodes."},
                    {"title": "Tool Call SDK", "desc": "Provides safe interfaces for agents to interact with internal ERP, CRM, and APIs."},
                    {"title": "Human-in-the-Loop", "desc": "Halts agent loop to prompt human review for high-value or ambiguous decisions."},
                    {"title": "Persistence Layer", "desc": "Maintains agent state history to support pause, resume, and audit trails."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Flow Mapping", "duration": "Weeks 1-2", "details": "Model current manual processes and specify operational decision boundaries."},
                    {"phase": "Phase 2: Tooling Build", "desc": "Construct secure Python integration wrappers for ERP, Salesforce, or Stripe.", "duration": "Weeks 3-5"},
                    {"phase": "Phase 3: Graph Tuning", "desc": "Programming agent roles, feedback loops, and automated self-correction logic.", "duration": "Weeks 6-8"},
                    {"phase": "Phase 4: Pilot Test", "desc": "Deploying agents in a sandbox with historical inputs; comparing agent outcomes vs humans.", "duration": "Weeks 9-11"}
                ],
                "faq": [
                    {
                        "q": "What happens if an agent gets stuck in an infinite loop?",
                        "a": "Our graphs run with strict token, step, and budget limits. If a threshold is exceeded, the loop terminates immediately, resets state, and alerts an engineer or operator."
                    },
                    {
                        "q": "How do you ensure agents don't make unauthorized payments?",
                        "a": "All critical operational pathways (e.g. wire transfers, system deletions, external notifications) require human-in-the-loop approvals before executing."
                    }
                ]
            },
            {
                "id": "document-intelligence",
                "slug": "document-intelligence",
                "name": "Document Intelligence",
                "tagline": "Automated Data Extraction & Compliance Analysis",
                "icon": "file-text",
                "short_description": "Convert complex PDFs, invoices, contracts, and application forms into clean, verified structured data formats.",
                "overview": (
                    "Enterprise contracts, compliance records, and logistics bills are highly unstructured. "
                    "Our Document Intelligence suite extracts key clauses, tables, metadata, and dates with near-perfect "
                    "accuracy, feeding clean JSON data directly into your relational databases and downstream enterprise workflows."
                ),
                "business_problems": [
                    "Manual data entry teams processing thousands of PDF invoices, leading to errors and delays.",
                    "Unstructured legal contracts requiring extensive reviews to map obligations and renewal dates.",
                    "Regulatory audits delayed due to difficulty finding missing compliance clauses across historic records."
                ],
                "solution": (
                    "We implement computer vision and multimodal parser models combined with rule-based verification. "
                    "The system extracts layout grids, checks values mathematically, and alerts operations only when "
                    "discrepancies arise."
                ),
                "benefits": [
                    {"label": "Processing Speed", "value": "15x"},
                    {"label": "Data Input Errors", "value": "-99%"},
                    {"label": "Audit Preparation Time", "value": "-70%"}
                ],
                "architecture_steps": [
                    {"title": "OCR & Extraction", "desc": "Scans document pages and transcribes characters with spatial location mapping."},
                    {"title": "Visual Parser", "desc": "Identifies headers, footnotes, tables, signatures, and form fields."},
                    {"title": "JSON Schema Validation", "desc": "Validates types, checks math (e.g., item sums), and maps output format."},
                    {"title": "CRM/ERP Exporter", "desc": "Streams structured fields into databases, SAP, or Salesforce via APIs."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Audit", "duration": "Weeks 1", "details": "Analyze document diversity (forms, formats, languages) and design schema."},
                    {"phase": "Phase 2: Model Training", "desc": "Fine-tuning layouts and document extraction classifiers on representative files.", "duration": "Weeks 2-4"},
                    {"phase": "Phase 3: Integration", "desc": "Connecting email inboxes, file uploads, and ERP targets.", "duration": "Weeks 5-6"},
                    {"phase": "Phase 4: Run & Refine", "desc": "Monitoring edge cases, refining confidence thresholds, and launching human review portal.", "duration": "Weeks 7-8"}
                ],
                "faq": [
                    {
                        "q": "How does the system handle low-quality scans or handwritten text?",
                        "a": "Our pipelines utilize state-of-the-art vision models that specialize in noise removal and handwriting analysis. If OCR confidence drops below a set threshold (e.g., 90%), the file is routed to the human verification queue."
                    }
                ]
            },
            {
                "id": "ai-automation",
                "slug": "ai-automation",
                "name": "AI Automation",
                "tagline": "End-to-End Workflow Optimization & API Integration",
                "icon": "git-branch",
                "short_description": "Upgrade legacy RPA systems with intelligent decision layers. Integrate tools, databases, and APIs without manual intervention.",
                "overview": (
                    "Traditional Robotic Process Automation (RPA) breaks when website layouts shift or forms change. "
                    "AI Automation brings cognitive intelligence to workflow streams. By incorporating semantic classification "
                    "and dynamic page interactions, our workflows adapt dynamically to system changes, ensuring "
                    "continuous operation."
                ),
                "business_problems": [
                    "Fragile RPA scripts requiring constant maintenance when software interfaces update.",
                    "Decentralized operations relying on manual email forwards to link systems.",
                    "High overhead in customer onboarding and order provisioning processes."
                ],
                "solution": (
                    "We develop resilient backend integrations utilizing robust, code-first automation tools. By wrapping "
                    "legacy interfaces with API abstraction layers and using LLMs to format data formats, we build "
                    "self-correcting processes that require zero maintenance."
                ),
                "benefits": [
                    {"label": "Process Resilience", "value": "99.9%"},
                    {"label": "Operational Costs", "value": "-45%"},
                    {"label": "Process Throughput", "value": "8.5x"}
                ],
                "architecture_steps": [
                    {"title": "API Wrapper", "desc": "Creates robust endpoints over systems lacking native API capabilities."},
                    {"title": "Cognitive Router", "desc": "Uses AI to determine where incoming data should route based on intent."},
                    {"title": "Sync Engine", "desc": "Coordinates tasks asynchronously and guarantees reliable order delivery."},
                    {"title": "Error Monitor", "desc": "Intercepts errors, retries dynamically, and updates webhook logs."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Mapping", "duration": "Weeks 1-2", "details": "Analyze business steps, trace system data pathways, and outline API requirements."},
                    {"phase": "Phase 2: Pipeline Build", "desc": "Constructing core queues, webhook handlers, and retry mechanism scripts.", "duration": "Weeks 3-5"},
                    {"phase": "Phase 3: AI Classifier Setup", "desc": "Configuring LLM routers to format incoming messages and execute validations.", "duration": "Weeks 6-7"},
                    {"phase": "Phase 4: Launch", "desc": "Staged cut-over, performance stress tests, and final deployment setup.", "duration": "Weeks 8-9"}
                ],
                "faq": [
                    {
                        "q": "Can this connect to old internal legacy servers?",
                        "a": "Yes. We specialize in building secure lightweight microservice agents that run inside your local secure intranet, exposing secure endpoints for our cloud workflow managers."
                    }
                ]
            },
            {
                "id": "generative-ai-apps",
                "slug": "generative-ai-apps",
                "name": "Generative AI Applications",
                "tagline": "Tailored LLM Applications & Custom Chat Interfaces",
                "icon": "sparkles",
                "short_description": "Build modern chat interfaces, content generation engines, and customer-facing copilot applications powered by proprietary LLMs.",
                "overview": (
                    "Enterprise applications require customized user interfaces to truly drive adoption. "
                    "We build bespoke web apps, design interfaces, and create developer tooling tailored to your business rules. "
                    "Our apps feature responsive design, rich dashboards, and state-of-the-art interactive graphics."
                ),
                "business_problems": [
                    "Generic chat UI alternatives posing data leaks and offering no custom data integration.",
                    "Inefficient copywriting and asset generation pipelines slowing marketing and design teams.",
                    "Customer-facing portals lacking helpful, human-like automated guide systems."
                ],
                "solution": (
                    "We build responsive frontends integrated with custom-tuned language models. "
                    "By implementing enterprise security keys, local model configurations, and role-based permissions, "
                    "we deliver client portals and internal apps that ensure corporate brand consistency."
                ),
                "benefits": [
                    {"label": "Productivity Spike", "value": "180%"},
                    {"label": "Time to Market", "value": "-50%"},
                    {"label": "User Adoption Rate", "value": "92%"}
                ],
                "architecture_steps": [
                    {"title": "UI Interface", "desc": "Fast, modern web designs featuring smooth interactive states."},
                    {"title": "Model Hub", "desc": "Centralized engine managing prompts, parameters, and tokens."},
                    {"title": "PII Filtering", "desc": "Masks personal identity markers before passing payload to LLMs."},
                    {"title": "Logging Portal", "desc": "Tracks performance, prompt metrics, and user feedback."}
                ],
                "timeline": [
                    {"phase": "Phase 1: UX Wireframing", "duration": "Weeks 1-2", "details": "Drafting responsive app flows, interfaces, and prompt parameters."},
                    {"phase": "Phase 2: Frontend Dev", "desc": "Building custom React/Vite frontends with Tailwind and interactive components.", "duration": "Weeks 3-5"},
                    {"phase": "Phase 3: API Integration", "desc": "Wiring the frontend with backends, model routers, and identity handlers.", "duration": "Weeks 6-7"},
                    {"phase": "Phase 4: Launch & Optimize", "desc": "User telemetry installation, performance tuning, and final cloud setup.", "duration": "Weeks 8-9"}
                ],
                "faq": [
                    {
                        "q": "How do you protect customer data privacy?",
                        "a": "All applications run with enterprise-grade encryption. We configure models with zero data retention clauses, meaning external AI providers are contractually blocked from using your data for training."
                    }
                ]
            },
            {
                "id": "enterprise-search",
                "slug": "enterprise-search",
                "name": "Enterprise Search",
                "tagline": "Hybrid Search Architectures & Dense Vector Retrieval",
                "icon": "search",
                "short_description": "Upgrade database discovery with hybrid lexical-semantic search, enabling users to instantly locate files and records.",
                "overview": (
                    "Locating information in legacy systems often requires exact keywords. "
                    "Enterprise Search merges BM25 keyword matching with dense vector retrieval. "
                    "This hybrid search system understands synonym mappings, intent contexts, and user profiles, "
                    "ensuring accurate, fast access to the documents you need."
                ),
                "business_problems": [
                    "Employees unable to find records due to spelling mistakes or missing exact keywords.",
                    "Siloed document servers forcing users to repeat searches across multiple folders.",
                    "Slow database query speeds affecting customer support and application performance."
                ],
                "solution": (
                    "We implement Elasticsearch or Qdrant cluster indexing setups, mapping raw documents "
                    "to vectors. The search engine dynamically weights query metrics, delivering fast, relevant results."
                ),
                "benefits": [
                    {"label": "Search Click-through", "value": "95%"},
                    {"label": "Query Speed Response", "value": "<85ms"},
                    {"label": "Irrelevant Results", "value": "-75%"}
                ],
                "architecture_steps": [
                    {"title": "Ingestion Queue", "desc": "Parses files, cleans formatting, and generates text segments."},
                    {"title": "Hybrid Encoder", "desc": "Creates sparse search matrices and dense vector representations."},
                    {"title": "Query Matcher", "desc": "Combines matching scores across lexical and semantic layers."},
                    {"title": "Analytics Tracker", "desc": "Analyzes searches that return zero results to guide future model optimization."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Audit", "duration": "Weeks 1", "details": "Analyze current search indexes, data fields, and compile query dictionaries."},
                    {"phase": "Phase 2: Engine Config", "desc": "Spinning up dedicated vector clusters and structuring retrieval algorithms.", "duration": "Weeks 2-4"},
                    {"phase": "Phase 3: System Sync", "desc": "Configuring automatic indexing workflows that update the search database as documents change.", "duration": "Weeks 5-6"},
                    {"phase": "Phase 4: Launch", "desc": "A/B testing current search results against semantic search parameters, deploying updates.", "duration": "Weeks 7-8"}
                ],
                "faq": [
                    {
                        "q": "What database systems are supported?",
                        "a": "We support search indexes on PostgreSQL, MongoDB, Elasticsearch, OpenSearch, AWS Aurora, Snowflake, and localized folder structures."
                    }
                ]
            },
            {
                "id": "custom-ai-dev",
                "slug": "custom-ai-dev",
                "name": "Custom AI Development",
                "tagline": "Specialized Model Fine-Tuning & Private Cloud Deployment",
                "icon": "code",
                "short_description": "Train open-weight models (Llama-3, Mistral) on your private data. Deploy optimized inference endpoints on your cloud.",
                "overview": (
                    "For companies with strict compliance, proprietary codebases, or specialized domains, "
                    "relying on public APIs is not an option. Custom AI Development builds bespoke models "
                    "tailored specifically to your corporate protocols. We fine-tune models, perform quantization "
                    "for lower latency, and deploy private inference endpoints on AWS, Azure, or GCP."
                ),
                "business_problems": [
                    "High API usage costs for large-scale summarization or data processing workflows.",
                    "Strict regulations preventing the transmission of data to external AI servers.",
                    "Off-the-shelf models lacking deep understanding of proprietary industry terminology."
                ],
                "solution": (
                    "We design end-to-end model pipelines: curating training data, executing fine-tuning runs (QLoRA), "
                    "verifying model performance, and deploying containerized models via vLLM inside your private cloud."
                ),
                "benefits": [
                    {"label": "Model API Cost Savings", "value": "72%"},
                    {"label": "Data Privacy Risk", "value": "0%"},
                    {"label": "Inference Latency", "value": "40ms"}
                ],
                "architecture_steps": [
                    {"title": "Data Curation", "desc": "Cleans, structures, and formats your internal datasets into training inputs."},
                    {"title": "Fine-Tuning Loop", "desc": "Runs parameter-efficient fine-tuning on enterprise cloud clusters."},
                    {"title": "Evaluation Matrix", "desc": "Compares model accuracy, speed, and cost parameters against baseline metrics."},
                    {"title": "Inference Server", "desc": "Deploys models using vLLM in Docker container configurations."}
                ],
                "timeline": [
                    {"phase": "Phase 1: Feasibility", "duration": "Weeks 1-2", "details": "Audit training data availability, choose base models, and estimate GPU resource needs."},
                    {"phase": "Phase 2: Fine-Tuning", "desc": "Running training iterations and evaluating model performance metrics.", "duration": "Weeks 3-6"},
                    {"phase": "Phase 3: Infrastructure Setup", "desc": "Provisioning GPU instances and configuring containerized inference engines.", "duration": "Weeks 7-9"},
                    {"phase": "Phase 4: Integration & Rollout", "desc": "Transitioning applications to the private model and conducting final performance checks.", "duration": "Weeks 10-12"}
                ],
                "faq": [
                    {
                        "q": "What base models do you recommend?",
                        "a": "We primarily work with open-weight models like Meta Llama-3, Mistral, Qwen-2, and DeepSeek, choosing the optimal model based on your task requirements and target latency."
                    },
                    {
                        "q": "Can these models run locally without internet access?",
                        "a": "Yes. Quantized models can run completely offline on local GPU servers, securing sensitive corporate IP."
                    }
                ]
            }
        ]

    @staticmethod
    def get_industries():
        return [
            {
                "slug": "retail",
                "name": "Retail",
                "icon": "shopping-bag",
                "headline": "Demand Forecasting & Real-Time Customer Intelligence",
                "intro": "Navigate dynamic supply chains and deliver personalized customer journeys with AI-powered retail analytics.",
                "challenges": [
                    "Stockouts and overstock losses due to inaccurate inventory forecasting.",
                    "Fragmented customer profiles leading to irrelevant promotional offers.",
                    "Delayed customer support during peak seasonal demand."
                ],
                "solutions": [
                    "Predictive demand forecasting engines trained on historic sales and local weather patterns.",
                    "Personalized recommendation systems connected directly to digital shopping carts.",
                    "Custom shopping copilots that assist customers in finding products and checking store availability."
                ],
                "impact": "18% reduction in inventory hold cost, 22% increase in average cart size."
            },
            {
                "slug": "ecommerce",
                "name": "Ecommerce",
                "icon": "shopping-cart",
                "headline": "Conversational Search & Autonomous Catalog Enrichment",
                "intro": "Enhance product search and automate catalog descriptions to drive customer conversions.",
                "challenges": [
                    "High search bounce rates due to poor product matching.",
                    "Manual catalog listing management limiting catalog scale.",
                    "High support ticket volumes regarding delivery status and returns."
                ],
                "solutions": [
                    "Semantic search engines that understand customer intent and search context.",
                    "Automated catalog generators that write SEO-optimized copy from product images.",
                    "Self-service post-purchase agents that handle updates, returns, and exchanges."
                ],
                "impact": "35% conversion lift on search queries, 80% reduction in catalog publishing time."
            },
            {
                "slug": "manufacturing",
                "name": "Manufacturing",
                "icon": "factory",
                "headline": "Predictive Maintenance & Automated Quality Assurance",
                "intro": "Minimize assembly line downtime and maintain strict quality standards with predictive AI.",
                "challenges": [
                    "Equipment failures halting assembly lines and causing costly delays.",
                    "Manual quality audits missing microscopic defects.",
                    "Outdated machinery manuals slowing down floor technicians."
                ],
                "solutions": [
                    "Predictive maintenance models that analyze sensor feeds to alert technicians before failures.",
                    "Computer vision models that scan assembly lines to flag defects.",
                    "Knowledge assistants that allow mechanics to query complex equipment manuals in seconds."
                ],
                "impact": "30% reduction in downtime, 98.7% quality detection rate on assembly lines."
            },
            {
                "slug": "finance",
                "name": "Financial Services",
                "icon": "dollar-sign",
                "headline": "Automated Underwriting & Real-Time Fraud Audits",
                "intro": "Accelerate loan processing and strengthen security with secure, compliant AI systems.",
                "challenges": [
                    "Slow loan processing times due to manual document collection.",
                    "Increasing sophistication of credit and transaction fraud.",
                    "Rising compliance costs associated with financial regulations."
                ],
                "solutions": [
                    "Document parsing agents that extract financial fields from tax returns and bank statements.",
                    "Real-time fraud classifiers that analyze transaction data for anomalies.",
                    "Compliance copilots that flag policy deviations in customer interactions."
                ],
                "impact": "85% reduction in underwriting turnaround, 40% improvement in fraud detection."
            },
            {
                "slug": "healthcare",
                "name": "Healthcare",
                "icon": "activity",
                "headline": "Medical Record Synthesis & Automated Patient Onboarding",
                "intro": "Streamline administrative tasks and synthesize medical history to allow clinical staff to focus on patients.",
                "challenges": [
                    "Physicians spending hours inputting data into electronic health records.",
                    "Fragmented patient histories leading to clinical translation risks.",
                    "Administrative backlogs in processing patient intake forms."
                ],
                "solutions": [
                    "Voice-to-text dictation models designed for medical terminology.",
                    "Patient history summarization models that highlight key clinical events for physicians.",
                    "Intake extraction tools that import scanned paper forms into medical databases."
                ],
                "impact": "2.2 hours saved daily per physician, 90% reduction in patient onboarding delays."
            },
            {
                "slug": "logistics",
                "name": "Logistics",
                "icon": "truck",
                "headline": "Dynamic Route Optimization & Freight Bill Automation",
                "intro": "Optimize delivery networks and automate freight invoice auditing with intelligent routing and extraction.",
                "challenges": [
                    "Route delays and high fuel consumption due to static schedule planning.",
                    "Discrepancies in freight invoices causing billing bottlenecks.",
                    "Inefficient dispatch communication during unexpected delay events."
                ],
                "solutions": [
                    "Real-time route optimization engines that adapt to traffic and weather conditions.",
                    "Automated invoice matchers that audit bills of lading against rate tables.",
                    "Dispatch copilots that automate alerts and status updates to drivers."
                ],
                "impact": "14% fuel cost savings, 92% reduction in billing audit workloads."
            }
        ]

    @staticmethod
    def get_case_studies():
        return [
            {
                "slug": "retail-analytics",
                "title": "Retail Analytics Copilot",
                "client": "Apex Global Retail",
                "metric": "80% reduction in reporting time",
                "summary": "Built a conversational data assistant enabling non-technical executives to query sales databases and generate visualizations in real time.",
                "challenge": (
                    "Apex Global Retail operated multiple SQL databases across regional warehouses. "
                    "Executive and category managers had to wait up to 4 days for custom data reports, "
                    "slowing inventory decisions."
                ),
                "solution": (
                    "Altimet AI built a customized AI Data Copilot that maps semantic queries into validated SQL. "
                    "We implemented a secure query sandbox with strict column access controls, enabling users "
                    "to generate tables and charts directly in Slack or web dashboards."
                ),
                "architecture_summary": "Semantic query translation graph using fine-tuned Llama-3, structured metadata mapper, and sandboxed execution container.",
                "impact": [
                    "Average query generation and execution time reduced from 4 days to 6 seconds.",
                    "99.4% SQL validity rate across complex database queries.",
                    "Over 400 monthly hours saved for the data analyst team."
                ],
                "tech_stack": ["Snowflake", "Python", "LangChain", "Qdrant", "Flask", "Tailwind CSS"]
            },
            {
                "slug": "manufacturing-assistant",
                "title": "Manufacturing Knowledge Assistant",
                "client": "Vanguard Automotive",
                "metric": "30% reduction in assembly downtime",
                "summary": "Designed a Retrieval-Augmented Generation (RAG) assistant allowing maintenance technicians to query technical manuals via voice commands.",
                "challenge": (
                    "Factory floor mechanics at Vanguard lost valuable time searching through "
                    "thousands of pages of complex manuals when assembly equipment failed.",
                    "Every minute of line downtime cost the company over $10,000."
                ),
                "solution": (
                    "We deployed an Enterprise Knowledge Copilot on local tablets. "
                    "Technicians can ask questions via voice, and the system performs a hybrid semantic-keyword "
                    "search to retrieve the exact repair step, displaying relevant mechanical diagrams."
                ),
                "architecture_summary": "Hierarchical document parsing pipeline, dense vector index cluster, and private cloud model deployment (Mistral-7B).",
                "impact": [
                    "Downtime caused by mechanical lookup issues reduced by 30%.",
                    "Technician onboarding and training time decreased by 25%.",
                    "98.8% accuracy in retrieving relevant diagram references."
                ],
                "tech_stack": ["PostgreSQL (pgvector)", "Python", "Mistral-7B", "vLLM", "Docker"]
            },
            {
                "slug": "executive-reporting",
                "title": "Executive Reporting AI",
                "client": "BlueHorizon Capital",
                "metric": "95% automation of financial reports",
                "summary": "Implemented document extraction pipelines to parse complex financial reports and generate investment briefs.",
                "challenge": (
                    "Investment analysts spent hours manually copying data from quarterly financial reports "
                    "and earnings transcripts to write client investment briefs."
                ),
                "solution": (
                    "We built an AI Document Intelligence pipeline that extracts financial tables "
                    "and metadata. The system compiles key metrics and generates draft briefs for review, "
                    "ensuring analysts can quickly verify information before sending."
                ),
                "architecture_summary": "Multimodal PDF parser, schema validation layer, and brief generation prompt templates with complete source citations.",
                "impact": [
                    "Brief creation time reduced from 3 hours to 8 minutes.",
                    "Zero transcription errors across processed tables.",
                    "95% automation rate, allowing analysts to cover double the investments."
                ],
                "tech_stack": ["AWS S3", "Python", "Claude-3-Sonnet", "JSON Schema Validator", "FastAPI"]
            },
            {
                "slug": "agent-automation",
                "title": "AI Agent Automation",
                "client": "Zenith Logistics",
                "metric": "75% operational throughput boost",
                "summary": "Deployed autonomous LangGraph agents to automate shipping operations and resolve invoice disputes.",
                "challenge": (
                    "Discrepancies in freight rates and shipping weights required customer service "
                    "agents to manually verify invoices across three legacy system portals, "
                    "causing shipping backlogs."
                ),
                "solution": (
                    "We designed an autonomous multi-agent system on LangGraph. "
                    "The system monitors incoming email disputes, extracts invoice IDs, fetches records "
                    "from legacy portals, analyzes variances, and drafts response resolutions for customer service review."
                ),
                "architecture_summary": "Stateful agent workflow on LangGraph with custom API tools and human-in-the-loop approvals for financial adjustments.",
                "impact": [
                    "Average invoice dispute resolution time reduced from 2 hours to under 2 minutes.",
                    "75% increase in operational throughput without increasing headcount.",
                    "92% of disputes resolved autonomously without human intervention."
                ],
                "tech_stack": ["LangGraph", "Python", "GPT-4o", "Redis", "Celery", "PostgreSQL"]
            }
        ]

    @staticmethod
    def get_blog_posts():
        return [
            {
                "slug": "building-production-grade-rag",
                "title": "Building Production-Grade RAG: From Prototype to Enterprise Scale",
                "category": "Architecture Guides",
                "read_time": "7 min read",
                "date": "June 15, 2026",
                "author": "Marcus Thorne, Principal Architect",
                "summary": "Moving Retrieval-Augmented Generation from a basic demo to a production-ready enterprise search system requires overcoming hurdles. Learn how to optimize chunking and reranking.",
                "tags": ["RAG", "Enterprise AI", "Vector Databases"],
                "content": (
                    "Building a vector search demo is simple, but scaling it for enterprise use is a challenge. "
                    "Issues like poor text parsing, context window limitations, and lack of metadata control "
                    "can lead to unreliable results. To build a robust system, focus on three areas: "
                    "1. Document Ingestion: Clean and structure PDFs, tables, and images. "
                    "2. Chunking Strategies: Use hierarchical chunking to maintain document context. "
                    "3. Reranking: Apply a hybrid search approach, combining lexical and semantic search "
                    "with cross-encoder reranking to ensure the most relevant results are returned."
                )
            },
            {
                "slug": "why-llm-agents-are-future-of-rpa",
                "title": "Why LLM Agents are the Future of Robotic Process Automation (RPA)",
                "category": "AI Insights",
                "read_time": "5 min read",
                "date": "May 28, 2026",
                "author": "Sarah Lin, Head of AI Research",
                "summary": "Traditional RPA scripts are brittle and break when UI layouts change. Discover how stateful AI agents handle complex workflows and self-correct on the fly.",
                "tags": ["Agents", "Automation", "LangGraph"],
                "content": (
                    "Traditional RPA is useful but fragile. A simple change to a webpage input ID "
                    "can break automation scripts. LLM agents solve this by reasoning through tasks "
                    "rather than just following static steps. Using frameworks like LangGraph, agents can "
                    "interact with APIs, verify outputs, and self-correct. When an agent encounters an error, "
                    "it can analyze the issue and retry, requesting human assistance only for complex edge cases."
                )
            },
            {
                "slug": "roi-of-private-model-finetuning",
                "title": "The ROI of Private Model Fine-Tuning: Open-Weights vs. Proprietary APIs",
                "category": "Whitepapers",
                "read_time": "8 min read",
                "date": "April 12, 2026",
                "author": "Julian Sterling, Director of Engineering",
                "summary": "Evaluating the economics of fine-tuning open models like Llama-3 compared to API calls. Analyze cost inflection points, security parameters, and response latency.",
                "tags": ["Fine-Tuning", "GPU", "Llama-3"],
                "content": (
                    "Many enterprises start with APIs like OpenAI or Anthropic, but as usage scales, "
                    "subscription costs can rise quickly. For applications processing millions of tokens, "
                    "fine-tuning an open-weight model like Llama-3 or Mistral and deploying it on private GPUs "
                    "can be more cost-effective. In addition to lower costs, private deployments ensure complete data privacy, "
                    "making them ideal for highly regulated industries."
                )
            }
        ]

    @classmethod
    def search(cls, query):
        """Fuzzy search across services, industries, case studies, and blog posts."""
        if not query:
            return []
        
        query = query.lower()
        results = []
        
        # Search Services
        for s in cls.get_services():
            if query in s["name"].lower() or query in s["tagline"].lower() or query in s["short_description"].lower():
                results.append({
                    "title": s["name"],
                    "category": "Service",
                    "url": f"/services/{s['slug']}",
                    "snippet": s["tagline"]
                })
                
        # Search Industries
        for ind in cls.get_industries():
            if query in ind["name"].lower() or query in ind["headline"].lower() or query in ind["intro"].lower():
                results.append({
                    "title": ind["name"],
                    "category": "Industry",
                    "url": f"/industries/{ind['slug']}",
                    "snippet": ind["headline"]
                })
                
        # Search Case Studies
        for cs in cls.get_case_studies():
            if query in cs["title"].lower() or query in cs["client"].lower() or query in cs["summary"].lower():
                results.append({
                    "title": cs["title"],
                    "category": "Case Study",
                    "url": f"/case-studies/{cs['slug']}",
                    "snippet": f"Client: {cs['client']} - {cs['metric']}"
                })
                
        # Search Blogs
        for b in cls.get_blog_posts():
            if query in b["title"].lower() or query in b["summary"].lower() or any(query in t.lower() for t in b["tags"]):
                results.append({
                    "title": b["title"],
                    "category": "Blog",
                    "url": f"/blog/{b['slug']}",
                    "snippet": b["summary"]
                })
                
        return results[:10]  # Return top 10 matches
