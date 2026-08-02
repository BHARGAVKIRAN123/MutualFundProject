# Mutual Fund Data Dictionary

## Table: dim_fund

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique Mutual Fund Code |
| fund_house | TEXT | Mutual Fund Company Name |
| scheme_name | TEXT | Mutual Fund Scheme Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| plan | TEXT | Direct / Regular Plan |
| launch_date | DATE | Fund Launch Date |
| benchmark | TEXT | Benchmark Index |
| fund_manager | TEXT | Fund Manager Name |
| risk_category | TEXT | Risk Category |
| sebi_category_code | TEXT | SEBI Category Code |

---

## Table: dim_date

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Transaction/NAV Date |
| year | INTEGER | Year |
| month | INTEGER | Month Number |
| day | INTEGER | Day Number |

---

## Table: fact_nav

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Mutual Fund Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## Table: fact_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | INTEGER | Mutual Fund Code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | Tier Classification |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Investor Gender |
| annual_income_lakh | REAL | Annual Income (Lakhs) |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | KYC Status |

---

## Table: fact_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Mutual Fund Code |
| return_1yr_pct | REAL | One Year Return (%) |
| return_3yr_pct | REAL | Three Year Return (%) |
| return_5yr_pct | REAL | Five Year Return (%) |
| benchmark_3yr_pct | REAL | Benchmark Return (%) |
| alpha | REAL | Alpha Value |
| beta | REAL | Beta Value |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown (%) |
| aum_crore | REAL | Assets Under Management (Crores) |
| expense_ratio_pct | REAL | Expense Ratio (%) |
| morningstar_rating | INTEGER | Morningstar Rating |