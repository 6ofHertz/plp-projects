# iris_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Add species names
df['species'] = df['target'].map(dict(zip(range(3), iris.target_names)))

# Display basic info
print("First 5 rows:")
print(df.head())
print("\nData Types and Missing Values:")
print(df.info())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Grouped means by species
print("\nGrouped Mean by Species:")
print(df.groupby("species").mean(numeric_only=True))

# Visualization
sns.set(style="whitegrid")
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Line chart
axs[0, 0].plot(df.index, df["petal length (cm)"], color="teal")
axs[0, 0].set_title("Petal Length Over Sample Index")
axs[0, 0].set_xlabel("Sample Index")
axs[0, 0].set_ylabel("Petal Length (cm)")

# Bar chart
sns.barplot(x="species",
            y="petal length (cm)",
            data=df,
            ax=axs[0, 1],
            palette="muted")
axs[0, 1].set_title("Average Petal Length by Species")

# Histogram
sns.histplot(df["sepal length (cm)"],
             bins=10,
             kde=True,
             ax=axs[1, 0],
             color="coral")
axs[1, 0].set_title("Distribution of Sepal Length")

# Scatter plot
sns.scatterplot(
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    data=df,
    ax=axs[1, 1],
)
axs[1, 1].set_title("Sepal vs Petal Length")

plt.tight_layout()
plt.show()
