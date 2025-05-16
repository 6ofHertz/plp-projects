
# COVID-19 Global Data Analysis Project

## Project Overview
This project analyzes global COVID-19 data to track cases, deaths, and vaccination progress across different countries, with a focus on Kenya, United States, India, South Africa, and United Kingdom.

## Data Source
The project uses data from Our World in Data's COVID-19 dataset:
- **Source URL**: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
- **Data Columns**: 67 columns including:
  - Cases (total and new)
  - Deaths (total and new)
  - Vaccinations
  - Hospital/ICU data
  - Testing data
  - Demographics
  - Economic indicators

## Analysis Performed
1. **Data Loading & Cleaning**
   - Loading CSV data
   - Handling missing values
   - Date formatting
   - Country filtering

2. **Exploratory Data Analysis**
   - Total cases trends
   - Death rate analysis
   - Vaccination progress
   - Global cases distribution

3. **Visualizations Generated**
   - `total_cases_trend.png`: Line chart of cases over time
   - `death_rates.png`: Bar chart of death rates by country
   - `vaccination_progress.png`: Vaccination progress comparison
   - `global_cases_map.html`: Interactive choropleth map

## Generated Reports
- `covid_analysis_report.md`: Contains key findings including:
  - Highest total cases
  - Highest death rates
  - Vaccination progress
  - Summary of visualizations

## Project Structure
```
Covid19/
├── main.py                    # Main analysis script
├── covid_analysis_report.md   # Analysis findings
├── death_rates.png           # Death rates visualization
├── global_cases_map.html     # Interactive world map
├── total_cases_trend.png     # Cases trend visualization
└── vaccination_progress.png  # Vaccination data visualization
```

## Running the Analysis
The analysis can be run using the "Run" button, which executes the COVID Analysis workflow configured in `.replit`.
