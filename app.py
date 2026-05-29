import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("📊 Sales Analysis Dashboard")

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Revenue"] = df["Units_Sold"] * df["Price"]
df["Month"] = df["Date"].dt.month

# KPIs
total_revenue = df["Revenue"].sum()
total_units = df["Units_Sold"].sum()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

st.subheader("📌 KPI Metrics")
st.write("Total Revenue:", total_revenue)
st.write("Total Units Sold:", total_units)
st.write("Top Product:", top_product)
st.write("Top Region:", top_region)

# Charts
st.subheader("📈 Product Revenue")
fig1, ax1 = plt.subplots()
df.groupby("Product")["Revenue"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

st.subheader("📈 Region Revenue")
fig2, ax2 = plt.subplots()
df.groupby("Region")["Revenue"].sum().plot(kind="bar", ax=ax2)
st.pyplot(fig2)

st.subheader("📈 Monthly Trend")
fig3, ax3 = plt.subplots()
df.groupby("Month")["Revenue"].sum().plot(kind="line", ax=ax3)
st.pyplot(fig3)
