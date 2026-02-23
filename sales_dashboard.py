import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("sales_data.csv")

# Fix date format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Create Revenue column
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Extract Month
df["Month"] = df["Date"].dt.month

# -----------------------------
# KPI Calculations
# -----------------------------

total_revenue = df["Revenue"].sum()
total_units = df["Units_Sold"].sum()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

# -----------------------------
# Grouped Data
# -----------------------------

product_sales = df.groupby("Product")["Revenue"].sum()
region_sales = df.groupby("Region")["Revenue"].sum()
monthly_sales = df.groupby("Month")["Revenue"].sum()

# -----------------------------
# Dashboard Layout
# -----------------------------

plt.figure(figsize=(14, 8))

# KPI Text Section
plt.subplot(2, 2, 1)
plt.axis("off")
plt.text(0.1, 0.8, f"Total Revenue: ₹{total_revenue}", fontsize=14)
plt.text(0.1, 0.6, f"Total Units Sold: {total_units}", fontsize=14)
plt.text(0.1, 0.4, f"Top Product: {top_product}", fontsize=14)
plt.text(0.1, 0.2, f"Top Region: {top_region}", fontsize=14)
plt.title("Sales KPI Summary")

# Product Revenue Chart
plt.subplot(2, 2, 2)
product_sales.plot(kind="bar")
plt.title("Revenue by Product")

# Region Revenue Chart
plt.subplot(2, 2, 3)
region_sales.plot(kind="bar")
plt.title("Revenue by Region")

# Monthly Trend Chart
plt.subplot(2, 2, 4)
monthly_sales.plot(kind="line")
plt.title("Monthly Revenue Trend")

plt.tight_layout()
plt.show()