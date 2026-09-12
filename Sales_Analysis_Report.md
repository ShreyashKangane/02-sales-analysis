# Sales Data Analysis Report

**Dataset:** `sample_sales.csv` — 220 sample orders, FY2025
**Tool:** Python (pandas)

## 1. Key Metrics

| Metric | Value |
|---|---|
| Total Orders | 220 |
| Total Sales | $58,961.34 |
| Total Profit | $21,011.81 |
| Profit Margin | 35.6% |
| Units Sold | 1,465 |
| Average Order Value | $268.01 |

## 2. Top 5 Products by Sales

| Product | Sales | Units Sold | Orders |
|---|---|---|---|
| Smart Watch | $13,730.05 | 115 | 16 |
| Tennis Racket | $6,885.01 | 85 | 11 |
| Denim Jacket | $4,704.54 | 86 | 13 |
| Cycling Helmet | $4,256.60 | 107 | 14 |
| Bluetooth Speaker | $3,312.20 | 56 | 9 |

The **Smart Watch** is the standout performer, generating roughly double the sales of the next closest product despite fewer orders — a sign of a high price point driving revenue.

## 3. Sales by Category

| Category | Sales | Profit | Margin |
|---|---|---|---|
| Electronics | $21,212.04 | $7,479.16 | 35% |
| Sports | $15,359.42 | $5,560.79 | 36% |
| Clothing | $11,288.36 | $4,121.52 | 37% |
| Home & Garden | $6,035.36 | $2,179.86 | 36% |
| Books | $5,066.16 | $1,670.48 | 33% |

Electronics leads on total revenue (largely driven by the Smart Watch), but **Clothing carries the highest profit margin (37%)**, and Books the lowest (33%).

## 4. Sales by Region

| Region | Sales | Profit | Orders | AOV |
|---|---|---|---|---|
| South | $15,764.94 | $5,500.52 | 55 | $286.64 |
| West | $15,484.98 | $5,508.36 | 58 | $266.98 |
| East | $15,399.61 | $5,517.26 | 58 | $265.51 |
| North | $12,311.81 | $4,485.67 | 49 | $251.26 |

Regional performance is fairly balanced — South, West, and East are all within 3% of each other on sales. **North trails the other three regions** on both total sales and average order value, making it a candidate for targeted promotion.

## 5. Monthly Sales Trend

| Month | Sales | Orders |
|---|---|---|
| Jan | $3,233.06 | 15 |
| Feb | $4,436.29 | 16 |
| Mar | $5,629.66 | 14 |
| Apr | $2,591.47 | 12 |
| May | $7,086.26 | 25 |
| Jun | $5,896.95 | 22 |
| Jul | $5,219.02 | 20 |
| Aug | $3,700.17 | 19 |
| Sep | $6,895.23 | 21 |
| Oct | $6,591.89 | 23 |
| Nov | $4,321.34 | 14 |
| Dec | $3,360.00 | 19 |

Sales dipped to their lowest point in **April** and peaked in **May**, followed by a second strong run in **September–October**. This pattern doesn't map to an obvious single season, suggesting order volume (not seasonality alone) is the main driver — May and October also had the highest order counts.

## 6. Summary of Findings

- The business generated **$58,961 in sales** and **$21,012 in profit** across 220 orders, a healthy **35.6% margin**.
- **Electronics** is the top revenue category, powered almost entirely by the Smart Watch; **Clothing** is the most profitable category per dollar of sales.
- **South** is the top-performing region, while **North** consistently lags on both sales and order value — worth investigating (pricing, marketing reach, or product mix).
- Sales are **not flat month-to-month**: April is a clear trough and May/September/October are peaks, correlating with higher order counts rather than higher order values.
- **Recommendation:** prioritize inventory and marketing spend around Smart Watch and the Sports category, replicate whatever drove the May/September order spikes, and investigate the North region's underperformance.

*Full analysis code: `analyze_sales.py`. Supporting data: `summary_top_products.csv`, `summary_by_category.csv`, `summary_by_region.csv`, `summary_by_month.csv`.*
