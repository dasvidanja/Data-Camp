#Binomial CDF
# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n=100, p=0.05, size =10000)

# Compute CDF: x, y
x,y = ecdf(n_defaults)

# Plot the CDF with axis labels
_= plt.plot(x,y, marker = '.', linestyle = 'none')
_=plt.xlabel('values')
_=plt.ylabel('probability')

# Show the plot
plt.show()

#BINOMIAL PMF
# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, normed=True, bins= bins)

# Label axes
_=plt.xlabel('values')
_=plt.ylabel('Probability')


# Show the plot
plt.show()

