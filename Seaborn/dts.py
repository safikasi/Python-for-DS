import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
#Categorical plotting in seaborn
tips=sns.load_dataset('tips')
print(tips.head())

sns.barplot(x='sex',y='total_bill',data=tips,hue='sex',estimator=np.std) #bar plot
plt.show()
sns.countplot(x='sex',data=tips,hue='sex') #count plot
plt.show()
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker') #box wisker plot
plt.show()
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True) #violen plot
plt.show()
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True) #strip plot like scatter plot
plt.show()
sns.swarmplot(x='day',y='total_bill',data=tips,color='black') #swarm plot
plt.show()
sns.countplot(x='sex',data=tips,hue='sex',kind='bar') #factor plot to create any plot 
plt.show()