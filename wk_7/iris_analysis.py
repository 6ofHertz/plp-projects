# iris_analysis.py
# Assignment: Data Loading, Exploration, Analysis, and Visualization using Pandas and Matplotlib

# ============================
# Step 1: Import Libraries
# ============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ============================
# Step 2: Load Dataset with Error Handling
# ============================
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("✅ Dataset loaded successfully!\n")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

# ============================
# Step 3: Display First Rows and Inspect Data
# ============================
print("🔍 First 5 rows of the dataset:")
print(df.head(), "\n")

print("📊 Data types:")
print(df.dtypes, "\n")

print("🧹 Missing values in each column:")
print(df.isnull().sum(), "\n")

# ✅ No missing values found.

# ============================
# Step 4: Basic Data Analysis
# ============================
print("📈 Basic statistics of numerical columns:")
print(df.describe(), "\n")

print("📉 Mean values grouped by species:")
grouped = df.groupby('species').mean()
print(grouped, "\n")

# ============================
# Step 5: Observations
# ============================
print("📌 Observations:")
print(
    "- Setosa has significantly smaller petal size compared to other species.")
print("- Virginica has the largest average petal length and width.")
print("- Sepal dimensions also vary by species but less dramatically.\n")

# ============================
# Step 6: Data Visualization
# ============================
sns.set(style="whitegrid")  # Optional for better style

# Line chart: Simulated trend over index
plt.figure(figsize=(8, 5))
df['sepal length (cm)'].plot(kind='line')
plt.title("Line Chart: Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart_sepal_length.png")
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'], palette="mako")
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.savefig("bar_chart_petal_length.png")
plt.show()

# Histogram: Sepal width distribution
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_sepal_width.png")
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df,
                x='sepal length (cm)',
                y='petal length (cm)',
                hue='species',
                palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.savefig("scatter_plot_sepal_vs_petal.png")
plt.show()

# ============================
# End of Script
# ============================

print("✅ Analysis and visualization completed successfully.")
