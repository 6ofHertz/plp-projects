
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

# App title and description
st.title('📊 COVID-19 Global Dashboard')
st.markdown('Interactive analysis of COVID-19 data worldwide')

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header('📌 Filters')
countries = sorted(df['location'].unique())
selected_countries = st.sidebar.multiselect('Select Countries', countries, 
                                          default=['United States', 'India', 'United Kingdom'])

min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input('Select Date Range',
                                  value=(max_date - timedelta(days=30), max_date),
                                  min_value=min_date,
                                  max_value=max_date)

# Filter data
mask = (df['location'].isin(selected_countries) & 
        (df['date'] >= pd.Timestamp(date_range[0])) &
        (df['date'] <= pd.Timestamp(date_range[1])))
filtered_df = df.loc[mask]

# Layout in columns
col1, col2 = st.columns(2)

with col1:
    # Total Cases Trend
    fig_cases = px.line(filtered_df, 
                        x='date', 
                        y='total_cases',
                        color='location',
                        title='Total COVID-19 Cases')
    st.plotly_chart(fig_cases, use_container_width=True)

    # Vaccination Progress
    fig_vax = px.line(filtered_df,
                      x='date',
                      y='total_vaccinations',
                      color='location',
                      title='Vaccination Progress')
    st.plotly_chart(fig_vax, use_container_width=True)

with col2:
    # Daily New Cases
    fig_new = px.bar(filtered_df,
                     x='date',
                     y='new_cases',
                     color='location',
                     title='Daily New Cases')
    st.plotly_chart(fig_new, use_container_width=True)

    # ICU Patients
    if 'icu_patients' in filtered_df.columns:
        fig_icu = px.line(filtered_df,
                         x='date',
                         y='icu_patients',
                         color='location',
                         title='ICU Patients')
        st.plotly_chart(fig_icu, use_container_width=True)

# Key metrics
st.header('🔑 Key Metrics')
latest_data = filtered_df.groupby('location').last()

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
for country in selected_countries:
    country_data = latest_data.loc[country]
    with metrics_col1:
        st.metric(f"{country} - Total Cases", f"{int(country_data['total_cases']):,}")
    with metrics_col2:
        st.metric(f"{country} - Total Deaths", f"{int(country_data['total_deaths']):,}")
    with metrics_col3:
        if pd.notna(country_data.get('total_vaccinations')):
            st.metric(f"{country} - Total Vaccinations", f"{int(country_data['total_vaccinations']):,}")
