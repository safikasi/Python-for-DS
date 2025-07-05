import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

# Grids in seaborn

# Load iris dataset
iris = sns.load_dataset('iris')
print("Iris Dataset:")
print(iris.head())

# Create a PairGrid object
p = sns.PairGrid(iris)

# Apply different plot types
p.map_diag(sns.histplot, kde=True)      # Histograms on the diagonal
p.map_upper(sns.scatterplot)            # Scatter plot on upper triangle
p.map_lower(sns.kdeplot, fill=True)     # KDE plot on lower triangle

plt.show()


#load tips dataset

tips = sns.load_dataset('tips')
print("Tips Dataset:")
print(tips.head())

g=sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.histplot,'total_bill',kde=True)
plt.show()

