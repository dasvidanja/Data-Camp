# Make a scatter plot
_=plt.plot(versicolor_petal_length,versicolor_petal_width, marker="o", linestyle='none')

# Label the axes
_=plt.xlabel('Petal Length')
_=plt.ylabel('Petal Width')

# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

#[1,0] or[0,1] for x & y cov, else x&x or y&y
# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[1,0]

# Print the length/width covariance
print(petal_cov)

#Correlation  function
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat= np.corrcoef(x,y)


    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r= pearson_r(versicolor_petal_length,versicolor_petal_width)

# Print the result
print(r)
