
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('sales_data.csv')

# Total Revenue
total_revenue = data['Revenue ($)'].sum()

# Best-selling Product with quantity
product_sales = data.groupby('Product')['Quantity Sold'].sum()
best_selling = product_sales.idxmax()
best_selling_quantity = product_sales[best_selling]

# Day with Highest Sales
highest_sales_day = data.groupby('Date')['Revenue ($)'].sum().idxmax()

# Save summary to a file
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    f.write(f"Best-Selling Product: {best_selling} ({best_selling_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {highest_sales_day}\n")

# Print the summary
print("\n📊 Sales Summary:")
print(f"💰 Total Revenue: ${total_revenue:,.2f}")
print(f"🏆 Best-Selling Product: {best_selling} ({best_selling_quantity} units sold)")
print(f"📅 Highest Sales Day: {highest_sales_day}")

# Visualize daily sales trends
plt.figure(figsize=(10, 6))
daily_sales = data.groupby('Date')['Revenue ($)'].sum()
sns.lineplot(x=daily_sales.index, y=daily_sales.values)
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.close()

# Product-wise revenue visualization
plt.figure(figsize=(10, 6))
product_revenue = data.groupby('Product')['Revenue ($)'].sum()
sns.barplot(x=product_revenue.index, y=product_revenue.values)
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('product_revenue.png')
plt.close()
