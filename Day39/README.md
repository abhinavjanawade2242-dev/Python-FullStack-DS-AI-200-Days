# Day 39: Online Retail Data Analysis

## Project Overview
This project analyzes an online retail transaction dataset to identify sales trends, high-value customers, and top-performing countries using Python.

## Objectives
- Clean the dataset by removing duplicate records.
- Analyze cancellation invoices and their impact on sales value.
- Calculate monthly sales trends.
- Identify the top 10 customers by sales value.
- Identify the top 10 countries by sales value.
- Generate business insights and visualizations.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Excel dataset (`Online Retail.xlsx`)

## Key Findings
- **Total sales value excluding cancellation invoices:** 10,619,986.68
- **Top country:** United Kingdom
- **UK contribution to sales value:** 84.55%
- **Highest-value customer:** Customer ID 14646
- **Highest customer sales value:** 280,206.02
- **Best-performing month:** November 2011
- **Highest monthly sales value:** 1,503,866.78
- **Countries analyzed:** 38

## Project Structure
```text
Day39/
├── day39.py
├── README.md
├── dataset/
│   └── Online Retail.xlsx
└── output/
    ├── monthly_sales.csv
    ├── top_10_customers.csv
    ├── country_sales.csv
    ├── monthly_sales.png
    ├── top_10_customers.png
    └── top_10_countries.png
```

## How to Run
1. Install Python.
2. Install the required libraries:
   `pip install pandas numpy matplotlib seaborn openpyxl`
3. Place `Online Retail.xlsx` inside the `dataset` folder.
4. Run the script:
   `python day39.py`
5. Check the `output` folder for exported CSV files and charts.

## Conclusion
This project demonstrates data cleaning, exploratory data analysis, grouping and aggregation, sales trend analysis, customer analysis, country-level comparisons, and data visualization.

**Note:** Sales figures represent transaction values after excluding cancellation invoices. Other negative-quantity transactions may still affect the totals.
