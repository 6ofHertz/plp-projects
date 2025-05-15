
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load CSV file
data = pd.read_csv('sales_data/sales_data.csv')

# Basic Analysis
total_revenue = data['Revenue ($)'].sum()
best_selling = data.groupby('Product')['Quantity Sold'].sum().idxmax()
highest_sales_day = data.groupby('Date')['Revenue ($)'].sum().idxmax()

# Create visualizations
plt.figure(figsize=(10, 6))
daily_sales = data.groupby('Date')['Revenue ($)'].sum()
daily_sales.plot(kind='line', marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_data/sales_trend.png')

# Product performance pie chart
plt.figure(figsize=(8, 8))
product_revenue = data.groupby('Product')['Revenue ($)'].sum()
plt.pie(product_revenue, labels=product_revenue.index, autopct='%1.1f%%')
plt.title('Revenue Share by Product')
plt.savefig('sales_data/product_share.png')

# Save summary to a file
with open('sales_data/sales_summary.txt', 'w') as f:
    f.write(f"Sales Analysis Report\n{'='*20}\n\n")
    f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    f.write(f"Best-Selling Product: {best_selling}\n")
    f.write(f"Highest Sales Day: {highest_sales_day}\n")

# Print the summary
print("\n📊 Sales Analysis Summary:")
print(f"💰 Total Revenue: ${total_revenue:,.2f}")
print(f"🏆 Best-Selling Product: {best_selling}")
print(f"📅 Highest Sales Day: {highest_sales_day}")
print("\n📈 Visualizations saved as 'sales_trend.png' and 'product_share.png'")
