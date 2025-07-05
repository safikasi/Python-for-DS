import seaborn as sns 
import matplotlib.pyplot as plt
#Distribution plotting in seaborn
tips=sns.load_dataset('tips')

print(tips.head())

sns.histplot(tips['total_bill'],kde=True,bins=30) #hist plot
sns.rugplot(tips['total_bill']) #rug plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg') #joint plot
sns.pairplot(tips,hue='sex',palette='coolwarm')#pair plot
plt.show()


