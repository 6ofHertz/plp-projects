import pandas as pd

# Load CSV file
data = pd.read_csv('sales_data.csv')

# Total Revenue
total_revenue = data['Revenue ($)'].sum()

# Best-selling Product
best_selling = data.groupby('Product')['Quantity Sold'].sum().idxmax()

# Day with Highest Sales
highest_sales_day = data.groupby('Date')['Revenue ($)'].sum().idxmax()

# Save summary to a file
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue}\n")
    f.write(f"Best-Selling Product: {best_selling}\n")
    f.write(f"Highest Sales Day: {highest_sales_day}\n")

# Print the summary
print("📊 Sales Summary:")
print(f"Total Revenue: ${total_revenue}")
print(f"Best-Selling Product: {best_selling}")
print(f"Highest Sales Day: {highest_sales_day}")
