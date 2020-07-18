#Super Light EDA 
#To explore the data
df.head()
df.info()
df.describe()

#Create a countplot with seaborn (kinda like a bar chart)
plt.figure()
sns.countplot(x='missile', hue='party',data=df, palette='RdBu')
plt.show()

#KNN Classifier 
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
#This allows to use the remaining dataset as the features by dropping the target value , .values gives us the numpy array version
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors= 6)

# Fit the classifier to the data, of course we need a train/test data, but this is just to get the jist of it (don't panic just yet)
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))

#Model Performance


