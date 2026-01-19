# project_a_sales_analytics
Beginner sales analytics project using SQL, Python, PostgreSQL, and Power BI
# Sales Performance Analytics
## Project Path

This repository is the first step in a progressive sales analytics series:

**Project 0 (this repo)** →  
[Project 1 — Intermediate Star Schema & ELT](https://github.com/promiseekwurumadu/project_intermediate_star_schema_elt.git) →  
[Project 2 — Advanced Sales Analytics & Customer Segmentation](https://github.com/promiseekwurumadu/Project_sales_analytics_advanced.git)


## Project Overview
This project analyses sales transaction data to answer key business questions related to revenue, customer behaviour, and product performance.

## Business Questions
- How does revenue trend over time?
- Which products and categories drive the most revenue?
- Who are the top customers and how concentrated is revenue?
- What is the repeat purchase rate?
- How does performance vary by country?

## Tech Stack
- Python (data cleaning and loading)
- PostgreSQL (data storage and analytics)
- SQL (business metrics)
- Power BI (visualisation)


## Key Findings

- Monthly revenue shows seasonality, with a peak in March 2011 and a dip in February.
- Approximately 65.6% of customers made repeat purchases, indicating strong customer retention.
- Revenue is therefore likely driven primarily by returning customers rather than one-off buyers.

## Dashboard

![Sales Analytics Dashboard](dashboard/dashboard_overview.png)

An interactive Power BI dashboard connected directly to a PostgreSQL database.
It allows users to explore sales performance using:
- Date range slicing
- Country-level filtering
- Revenue trends and product-level comparisons

## Architecture

Excel (raw data)
→ Python cleaning script (`src/load_and_clean_data.py`)
→ Clean CSV (`data/online_retail_clean.csv`)
→ PostgreSQL (`online_retail` table)
→ SQL analysis (`sql/`)
→ Power BI dashboard (`dashboard/`)

## Next Step: Project 1

In Project 1, this sales data is restructured into a proper analytical model using a star schema and ELT principles.

**What Project 1 adds:**
- Fact and dimension tables
- Star schema modelling
- SQL-based transformations
- Cohort-ready data structures

➡ Continue here:  
https://github.com/promiseekwurumadu/project_intermediate_star_schema_elt.git

