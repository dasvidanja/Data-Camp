# Create bee swarm plot with Seaborn's default settings
_= sns.swarmplot(x='species', y= 'petal length (cm)', data= df)

# Label the axes
_=plt.xlabel('Species')
_=plt.ylabel('Sepal length (cm)')


# Show the plot
plt.show()
