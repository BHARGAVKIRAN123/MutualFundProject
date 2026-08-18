# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The **Bluestock Mutual Fund Analytics Capstone** is an end-to-end data analytics project focused on analyzing mutual fund performance, investor transactions, NAV trends, AUM, SIP inflows, benchmark performance, and investor behavior.

The project follows a complete analytics workflow:

**Raw Data → Data Cleaning → ETL Pipeline → SQLite Database → SQL Analysis → Exploratory Data Analysis → Performance Analysis → Advanced Analytics → Power BI Dashboard → Reports**

The project combines Python, SQL, SQLite, Jupyter Notebook, and Power BI to transform raw mutual fund datasets into meaningful business insights.

---

## Objectives

The main objectives of this project are:

- Clean and transform raw mutual fund datasets.
- Build a reusable ETL pipeline using Python.
- Store processed datasets in a SQLite database.
- Analyze mutual fund AUM and fund-house performance.
- Analyze SIP inflows and category-level investment trends.
- Analyze scheme returns and risk.
- Study benchmark index performance.
- Analyze investor transactions and portfolio behavior.
- Generate advanced investment analytics such as Sharpe Ratio, Sortino Ratio, CAGR, Alpha, VaR and CVaR.
- Build an interactive Power BI dashboard.
- Generate business insights and fund recommendations.

---

## Project Architecture

```text
                         RAW DATA
                            |
                            v
                  +-------------------+
                  |   Data Cleaning    |
                  |      Python       |
                  +-------------------+
                            |
                            v
                  +-------------------+
                  |   Processed CSVs   |
                  +-------------------+
                            |
                            v
                  +-------------------+
                  |   SQLite Database  |
                  +-------------------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
         SQL Analysis      EDA       Advanced Analytics
             |              |              |
             +--------------+--------------+
                            |
                            v
                  +-------------------+
                  |   Power BI        |
                  |    Dashboard      |
                  +-------------------+
                            |
                            v
                  Business Insights