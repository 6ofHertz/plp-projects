
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# ============================
# Step 1: Data Loading & Exploration
# ============================
print("1️⃣ Loading and exploring data...")

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

# Basic data exploration
print("\n🔍 First few rows:")
print(df.head())

print("\n📊 Data columns:")
print(df.columns.tolist())

print("\n🧹 Missing values:")
print(df.isnull().sum())

# ============================
# Step 2: Data Cleaning
# ============================
print("\n2️⃣ Cleaning data...")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Select countries of interest
focus_countries = ['Kenya', 'United States', 'India', 'South Africa', 'United Kingdom']
df_cleaned = df[df['location'].isin(focus_countries)].copy()

# Handle missing values
numeric_columns = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations']
df_cleaned[numeric_columns] = df_cleaned[numeric_columns].ffill()

# ============================
# Step 3: Exploratory Data Analysis
# ============================
print("\n3️⃣ Performing EDA...")

# Set plot style
plt.style.use('default')

# 1. Total Cases Over Time
plt.figure(figsize=(12, 6))
for country in focus_countries:
    country_data = df_cleaned[df_cleaned['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases by Country')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Covid19/total_cases_trend.png')
plt.close()

# 2. Death Rate Analysis
plt.figure(figsize=(10, 6))
latest_data = df_cleaned.groupby('location').last()
death_rate = (latest_data['total_deaths'] / latest_data['total_cases'] * 100).round(2)
death_rate.plot(kind='bar')
plt.title('COVID-19 Death Rate by Country')
plt.xlabel('Country')
plt.ylabel('Death Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Covid19/death_rates.png')
plt.close()

# 3. Vaccination Progress
plt.figure(figsize=(12, 6))
for country in focus_countries:
    country_data = df_cleaned[df_cleaned['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('COVID-19 Vaccination Progress')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Covid19/vaccination_progress.png')
plt.close()

# 4. Create a choropleth map using Plotly
latest_global = df.groupby('location').last().reset_index()
fig = px.choropleth(latest_global,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='location',
                    color_continuous_scale='Viridis',
                    title='Global COVID-19 Cases')
fig.write_html('Covid19/global_cases_map.html')

# ============================
# Step 4: Generate Insights Report
# ============================
print("\n4️⃣ Generating insights report...")

with open('Covid19/covid_analysis_report.md', 'w') as f:
    f.write("# COVID-19 Global Data Analysis Report\n\n")
    f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}\n\n")
    
    f.write("## Key Findings\n\n")
    
    # Cases Analysis
    highest_cases = latest_data['total_cases'].idxmax()
    f.write(f"1. **Highest Total Cases**: {highest_cases} with {latest_data['total_cases'][highest_cases]:,.0f} cases\n\n")
    
    # Death Rate Analysis
    highest_death_rate = death_rate.idxmax()
    f.write(f"2. **Highest Death Rate**: {highest_death_rate} with {death_rate[highest_death_rate]:.2f}%\n\n")
    
    # Vaccination Progress
    highest_vax = latest_data['total_vaccinations'].idxmax()
    f.write(f"3. **Most Vaccinations**: {highest_vax} with {latest_data['total_vaccinations'][highest_vax]:,.0f} doses\n\n")
    
    f.write("## Visualization Summary\n\n")
    f.write("1. Total Cases Trend (total_cases_trend.png)\n")
    f.write("2. Death Rates Comparison (death_rates.png)\n")
    f.write("3. Vaccination Progress (vaccination_progress.png)\n")
    f.write("4. Global Cases Map (global_cases_map.html)\n")

print("✅ Analysis completed! Check the Covid19 folder for generated reports and visualizations.")
