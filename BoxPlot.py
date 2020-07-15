#Import seaborn as sns

import seaborn as sns
# Create box plot with Seaborn's default settings
_=sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_=plt.xlabel('Species')
_=plt.ylabel('Percent of petal length')


# Show the plot
plt.show()
