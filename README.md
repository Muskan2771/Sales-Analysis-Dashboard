# 📊 Sales Analysis Dashboard

A professional Sales Data Analysis Dashboard built using **Python, Pandas, and Matplotlib**.  
This project analyzes sales data from a CSV file and generates business insights through KPI metrics and visualizations.

---

## 🚀 Project Overview

This dashboard performs:

- Data loading from CSV
- Data cleaning & transformation
- Revenue calculation
- KPI generation
- Product-wise revenue analysis
- Region-wise revenue analysis
- Monthly sales trend visualization
- Professional multi-chart dashboard layout

---

## 🛠 Technologies Used

- **Python** – Core programming language
- **Pandas** – Data analysis and manipulation
- **Matplotlib** – Data visualization

---

## 📂 Project Structure

```
Sales-Analysis-Dashboard/
│
├── sales_data.csv
├── sales_dashboard.py
└── README.md
```

---

## 📈 Key Features

### 🔹 KPI Summary
- Total Revenue
- Total Units Sold
- Top Performing Product
- Top Performing Region

### 🔹 Visualizations
- Revenue by Product (Bar Chart)
- Revenue by Region (Bar Chart)
- Monthly Revenue Trend (Line Chart)

---

## 📊 How It Works

1. The dataset is loaded using `pd.read_csv()`
2. Date column is converted using `pd.to_datetime()`
3. Revenue is calculated:
   ```
   Revenue = Units_Sold × Price
   ```
4. Data is grouped using `groupby()` for insights
5. Dashboard layout is created using Matplotlib subplots

---

## ▶️ How to Run

### Step 1: Install Required Libraries

```bash
pip install pandas matplotlib
```

### Step 2: Run the Project

```bash
python sales_dashboard.py
```

---

## 🧠 Business Insights Generated

- Identifies highest revenue-generating product
- Determines best performing region
- Tracks monthly sales performance
- Provides decision-support analytics

---

## 📌 Sample Dashboard Output

The dashboard displays:

- KPI Summary Panel
- Product Revenue Bar Chart
- Region Revenue Bar Chart
- Monthly Revenue Line Chart

All visualized in a structured 2x2 professional layout.

---

## 💡 Future Improvements

- Add interactive filters
- Convert to Streamlit Dashboard
- Add profit margin calculation
- Include year-over-year comparison
- Integrate real-world large dataset

---

## 👩‍💻 Author

**Muskan**  
Aspiring Data Analyst | Python | Pandas | Data Visualization

---

⭐ If you like this project, feel free to fork and contribute!
