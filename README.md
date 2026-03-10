# Module-2-Project
Module 2 Project

Netflix Global Talent & Market Pipeline
📌 Project Overview
This project establishes an automated ELT (Extract, Load, Transform) Pipeline to analyze Netflix's global content library. By transforming raw CSV data into a clean Star Schema in Google BigQuery, the pipeline identifies high-value talent (Top 5 Directors) and strategic production hubs (Top 10 Countries).

Key Business Value:
Data Trust: Integrated "Circuit Breaker" Quality Gates prevent "Unknown" or duplicate data from reaching executive reports.

Talent Analytics: Automated identification of prolific directors for strategic partnership decisions.

Market Insight: Geographical analysis of content density to inform regional investment.

🏗️ Technical Architecture
The pipeline follows a modern data stack approach, utilizing VS Code as the central orchestrator.

Ingestion: Python script uploads netflix_titles.csv to BigQuery raw_source.

Transformation (dbt): * Staging: Filters nulls and enforces "Zero-Unknown" policy.

Marts: Creates Fact and Dimension tables (Star Schema).

Data Quality: Automated dbt test validates referential integrity and uniqueness.

Analytics: Python/Matplotlib generates high-fidelity business dashboards.

🚀 Getting Started
Prerequisites
Python 3.9+

dbt-core & dbt-bigquery

Google Cloud Service Account (JSON Key)

Installation & Setup
Clone the Repo:

Bash
git clone https://github.com/your-username/netflix-data-pipeline.git
Setup Profiles:
Ensure your ~/.dbt/profiles.yml is configured to point to your BigQuery project.

Run the Pipeline:
This project uses VS Code Tasks for automation. Press Ctrl + Shift + B to execute the full pipeline:

Bash
# Manual Alternative:
dbt run && dbt test && python audit_quality.py && python netflix_analysis.py

🛡️ Data Quality Audit
This pipeline features a mandatory Quality Gate. If the data contains missing keys or "Unknown" values, the visual report is suppressed to protect decision-making integrity.

Recent Audit Status:

✅ DQ PASSED: 5,332 records verified as 100% clean.

📊 Business Insights
The pipeline generates an executive_report.png containing:

Top 5 Prolific Directors: Talent volume metrics.

Top 10 Market Hubs: Regional production density.

Content Rating Distribution: Audience demographic breakdown.

📂 Project Structure
models/: SQL transformation logic (Staging/Marts).

audit_quality.py: Final audit
netflix_analysis.py: Visualization engine.

.vscode/tasks.json: Automation orchestrator.

data/: Source datasets.


📈 Data Pipeline Lineage
The following diagram illustrates the flow of data through the quality gates:

Raw CSV → Ingested to BigQuery.

Staging → Deduplication and Null handling.

Dimensions/Fact → Star Schema creation.

Audit Gate → Python-based circuit breaker.

Analytics → Matplotlib visualization.

