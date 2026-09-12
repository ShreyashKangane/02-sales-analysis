"""
Sales Data Analysis with Pandas
Dataset: sample_sales.csv (220 sample orders across FY2025)
"""
import pandas as pd

pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

df = pd.read_csv("sample_sales.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.strftime("%b")
df["MonthNum"] = df["Date"].dt.month

# ---------------- Key Metrics ----------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_units = df["Units"].sum()
num_orders = len(df)
aov = df["Sales"].mean()
profit_margin = total_profit / total_sales

print("=== KEY METRICS ===")
print(f"Total Orders:     {num_orders}")
print(f"Total Sales:      ${total_sales:,.2f}")
print(f"Total Profit:     ${total_profit:,.2f}")
print(f"Profit Margin:    {profit_margin:.1%}")
print(f"Units Sold:       {total_units:,}")
print(f"Avg Order Value:  ${aov:,.2f}")

# ---------------- Top Products ----------------
top_products = (
    df.groupby("Product")
    .agg(Sales=("Sales", "sum"), Units=("Units", "sum"), Orders=("Order ID", "count"))
    .sort_values("Sales", ascending=False)
    .head(5)
)
print("\n=== TOP 5 PRODUCTS BY SALES ===")
print(top_products)

# ---------------- By Category ----------------
by_category = (
    df.groupby("Category")
    .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order ID", "count"))
    .assign(Margin=lambda d: d["Profit"] / d["Sales"])
    .sort_values("Sales", ascending=False)
)
print("\n=== SALES BY CATEGORY ===")
print(by_category)

# ---------------- By Region ----------------
by_region = (
    df.groupby("Region")
    .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order ID", "count"))
    .assign(AOV=lambda d: d["Sales"] / d["Orders"])
    .sort_values("Sales", ascending=False)
)
print("\n=== SALES BY REGION ===")
print(by_region)

# ---------------- By Month (time period) ----------------
by_month = (
    df.groupby(["MonthNum", "Month"])
    .agg(Sales=("Sales", "sum"), Orders=("Order ID", "count"))
    .reset_index()
    .sort_values("MonthNum")
    .drop(columns="MonthNum")
    .set_index("Month")
)
print("\n=== MONTHLY SALES TREND ===")
print(by_month)

best_month = by_month["Sales"].idxmax()
worst_month = by_month["Sales"].idxmin()
best_category = by_category.index[0]
best_region = by_region.index[0]
best_product = top_products.index[0]
best_margin_cat = by_category["Margin"].idxmax()

# Save summaries for reference
top_products.to_csv("summary_top_products.csv")
by_category.to_csv("summary_by_category.csv")
by_region.to_csv("summary_by_region.csv")
by_month.to_csv("summary_by_month.csv")

print("\n=== HEADLINE FINDINGS ===")
print(f"Best-selling product: {best_product}")
print(f"Top category: {best_category}")
print(f"Top region: {best_region}")
print(f"Highest-margin category: {best_margin_cat}")
print(f"Best month: {best_month}, Weakest month: {worst_month}")
