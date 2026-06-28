# Sales Data Analysis

## Project Overview
A Python program that analyzes sales data using Pandas
to calculate key business metrics and generate a report.

## Objectives
- Load and explore data using Pandas
- Check and handle missing values
- Calculate key business metrics (revenue, best-selling product, etc.)
- Generate a clean, formatted report

## Setup & Installation
1. Install Python 3.x
2. Install Pandas: pip install pandas
3. Clone this repository
4. Run: python sales_analysis.py

## Code Structure
- `sales_analysis.py` — main analysis script
- `sales_data.csv` — dataset (100 rows, 7 columns)

## Dataset Columns
Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales

## Metrics Calculated
1. Total Revenue
2. Best-Selling Product (by quantity)
3. Average Sale Value
4. Highest Single Sale
5. Top Performing Region

## How It Works
1. Loads sales data from CSV using Pandas
2. Displays dataset overview (rows, columns, data types)
3. Checks for missing values
4. Calculates 5 key business metrics
5. Prints a clean, formatted summary report

## What I Learned
- How to load and explore data using Pandas
- How to use groupby() for category-wise analysis
- How to check and handle missing values
- How to format numerical output for reports