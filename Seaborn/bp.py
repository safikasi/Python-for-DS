import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

# Matrix plots in seaborn

# Load datasets
tips = sns.load_dataset('tips')
print("Tips Dataset:")
print(tips.head())

flights = sns.load_dataset('flights')
print("\nFlights Dataset:")
print(flights.head())  # Just previewing first few rows

# Pivot the flights dataset for matrix plotting
fp = flights.pivot_table(index='month', columns='year', values='passengers')

# Heatmap: Passengers by Month & Year
plt.figure(figsize=(12, 6))
sns.heatmap(fp, annot=True, cmap='magma', linewidths=1.5, linecolor='white')
plt.title('Flight Passengers Heatmap')
plt.show()

# Cluster Map
sns.clustermap(fp, cmap='coolwarm')
plt.title('Cluster Map of Flights Data')
plt.show()

# Correlation matrix from tips dataset
tc = tips.corr(numeric_only=True)

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(tc, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
plt.title('Correlation Heatmap of Tips Dataset')
plt.show()

