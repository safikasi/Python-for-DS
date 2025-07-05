import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
np.random.seed(42)  # For reproducible results

dates = pd.date_range(start='2024-01-01', periods=100)
df = pd.DataFrame({
    'Sales': np.random.normal(200, 25, size=100),
    'Profit': np.random.normal(50, 10, size=100),
    'Expenses': np.random.normal(150, 20, size=100)
}, index=dates)

print("Head of the DataFrame:\n", df.head())

# 1️⃣ Line Plot (default)
df.plot(title="Line Plot of Sales, Profit, and Expenses", figsize=(10, 5))
plt.grid(True)
plt.show()

# 2️⃣ Histogram of Sales
df['Sales'].plot.hist(bins=20, alpha=0.7, color='skyblue', title="Histogram of Sales")
plt.xlabel("Sales")
plt.show()

# 3️⃣ Box Plot
df.plot.box(title="Box Plot of All Metrics")
plt.grid(True)
plt.show()

# 4️⃣ Area Plot
df.plot.area(alpha=0.4, title="Area Plot")
plt.show()

# 5️⃣ Bar Plot (using monthly average)
df_monthly = df.resample('M').mean()
df_monthly.plot.bar(rot=45, figsize=(10, 5), title="Monthly Averages (Bar Plot)")
plt.tight_layout()
plt.show()

# 6️⃣ Scatter Plot (Sales vs Profit)
df.plot.scatter(x='Sales', y='Profit', title="Sales vs Profit", color='red')
plt.grid(True)
plt.show()
