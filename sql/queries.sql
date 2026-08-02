-- ============================================
-- Query 1 : Top 5 Funds by AUM
-- ============================================

SELECT
    d.scheme_name,
    d.fund_house,
    f.aum_crore
FROM fact_performance f
INNER JOIN dim_fund d
ON f.amfi_code = d.amfi_code
ORDER BY f.aum_crore DESC
LIMIT 5;


-- ============================================
-- Query 2 : Average NAV Per Month
-- ============================================

SELECT
    SUBSTR(date,1,7) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY SUBSTR(date,1,7)
ORDER BY month;


-- ============================================
-- Query 3 : SIP Year-wise Growth
-- ============================================

SELECT
    STRFTIME('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year
ORDER BY year;


-- ============================================
-- Query 4 : Transactions By State
-- ============================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- ============================================
-- Query 5 : Funds Having Expense Ratio Less Than 1%
-- ============================================

SELECT
    d.scheme_name,
    f.expense_ratio_pct
FROM fact_performance f
INNER JOIN dim_fund d
ON f.amfi_code=d.amfi_code
WHERE expense_ratio_pct < 1;


-- ============================================
-- Query 6 : Top 10 Highest NAV
-- ============================================

SELECT
    d.scheme_name,
    n.date,
    n.nav
FROM fact_nav n
INNER JOIN dim_fund d
ON n.amfi_code=d.amfi_code
ORDER BY n.nav DESC
LIMIT 10;


-- ============================================
-- Query 7 : Average 1-Year Return By Fund House
-- ============================================

SELECT
    d.fund_house,
    ROUND(AVG(f.return_1yr_pct),2) AS average_return
FROM fact_performance f
INNER JOIN dim_fund d
ON f.amfi_code=d.amfi_code
GROUP BY d.fund_house
ORDER BY average_return DESC;


-- ============================================
-- Query 8 : Transactions By Payment Mode
-- ============================================

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;


-- ============================================
-- Query 9 : Total Investment By Category
-- ============================================

SELECT
    d.category,
    SUM(t.amount_inr) AS total_investment
FROM fact_transactions t
INNER JOIN dim_fund d
ON t.amfi_code=d.amfi_code
GROUP BY d.category
ORDER BY total_investment DESC;


-- ============================================
-- Query 10 : Top 5 Funds With Highest 1-Year Return
-- ============================================

SELECT
    d.scheme_name,
    f.return_1yr_pct
FROM fact_performance f
INNER JOIN dim_fund d
ON f.amfi_code=d.amfi_code
ORDER BY f.return_1yr_pct DESC
LIMIT 5;
