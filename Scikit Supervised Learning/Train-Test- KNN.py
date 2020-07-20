# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits['data'] #or digits.data (same)
y = digits['target']

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

#Predict
pred = knn.predict(X_test)
#Same thing as Accuracy below
print(sum(pred == y_test)/len(y_test))

# Print the accuracy
print(knn.score(X_test, y_test))
