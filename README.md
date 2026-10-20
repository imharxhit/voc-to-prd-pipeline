# voc-to-prd-pipeline

Automated Voice-of-Customer (VoC) triage and PRD problem-statement generator that links unstructured user feedback (app-store reviews, NPS verbatims, support tickets) with SQL account-tier revenue data to prioritize product backlogs by **Monthly Recurring Revenue (MRR) at risk**.

## How It Works
1. **Ingestion & Funnel Clustering (`src/triage_pipeline.py`)**: Classifies raw user feedback into specific product funnel stages using structured JSON schema outputs.
2. **SQL Revenue-at-Risk Join**: Joins ticket `account_id` against `dim_customer_subscriptions` to compute total MRR exposed per friction cluster.
3. **RICE & JIRA Specification Generator**: Calculates RICE priority scores and auto-generates JIRA issues complete with User Stories and Gherkin (`Given / When / Then`) acceptance criteria.
