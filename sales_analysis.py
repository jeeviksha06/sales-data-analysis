"""
Sales Data Analysis
This script loads sales data, checks for missing values,
and generates a summary report with key business metrics.
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display first few rows
print(df.head())

# Basic info about dataset
print(df.info())

print("\n--- BASIC STATISTICS ---")

# Total revenue
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Best-selling product (by quantity)
best_product = df.groupby('Product')['Quantity'].sum().idxmax()
print(f"Best-Selling Product: {best_product}")

# Average sale value
avg_sale = df['Total_Sales'].mean()
print(f"Average Sale Value: ₹{avg_sale:,.2f}")

# Highest single sale
max_sale = df['Total_Sales'].max()
print(f"Highest Single Sale: ₹{max_sale:,.2f}")

# Region with most sales
top_region = df.groupby('Region')['Total_Sales'].sum().idxmax()
print(f"Top Performing Region: {top_region}")


# Check for missing values
print("\n--- MISSING VALUES CHECK ---")
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()

print("\n" + "="*40)
print("SALES ANALYSIS REPORT")
print("="*40)
print(f"Total Records Analyzed: {len(df)}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{avg_sale:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Top Performing Region: {top_region}")
print("="*40)