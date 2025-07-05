import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set_style('darkgrid')  # Only one style allowed here: darkgrid, whitegrid, etc.
sns.set_style('ticks')
# Load dataset
tips = sns.load_dataset('tips')
print("Tips Dataset:")
print(tips.head())

# Countplot by gender, separated by smoker status
sns.countplot(x='sex', data=tips, hue='smoker')  # hue adds color separation
sns.despine(top=True, right=True)  # Removes top and right borders

plt.title("Count of Customers by Gender and Smoking Status")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
