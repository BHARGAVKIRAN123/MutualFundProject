-- ===========================================
-- Table : dim_fund
-- ===========================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);

-- ===========================================
-- Table : dim_date
-- ===========================================

CREATE TABLE dim_date (

    date DATE PRIMARY KEY,

    year INTEGER,

    month INTEGER,

    day INTEGER

);

-- ===========================================
-- Table : fact_nav
-- ===========================================

CREATE TABLE fact_nav (

    amfi_code INTEGER,

    date DATE,

    nav REAL

);

-- ===========================================
-- Table : fact_transactions
-- ===========================================

CREATE TABLE fact_transactions (

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT

);

-- ===========================================
-- Table : fact_performance
-- ===========================================

CREATE TABLE fact_performance (

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER

);