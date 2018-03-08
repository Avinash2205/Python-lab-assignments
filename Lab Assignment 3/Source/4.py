from sklearn import neighbors, datasets

# import data
iris = datasets.load_iris()
B = iris.data[:, :]
d = iris.target

# Splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
B_train, B_test, d_train, d_test = train_test_split(B, d, test_size = 0.2, random_state = 123)


from sklearn import metrics
neighbours =  [1,10,15,25,50]
for n in neighbours:
    clf = neighbors.KNeighborsClassifier(n)
    clf.fit(B_train, d_train)
    d_pred = clf.predict(B_test)
    print("Accuracy Score for K = ",n)
    print(metrics.accuracy_score(d_test, d_pred))
