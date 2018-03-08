from sklearn import datasets, metrics
from scipy import sparse
from sklearn.cross_validation import train_test_split
#Choose one of the dataset using the datasets features in the scikit-learn
from sklearn import svm
from sklearn.datasets import load_boston,load_digits
import numpy as np
#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)

C = 1.0
#getting the data and response of the dataset
#choosing
digits=load_digits() #load dataset
a=digits.data
b=digits.target
#According to your dataset, split the data to 20% testing data, 80% training data(you can also use any other number)
a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.2)
#Apply SVC with Linear kernel
model = svm.SVC(kernel='linear')
model.fit(a_train,b_train)
b_pred=model.predict(a_test)
print("Accuracy for linear kernel in SVC " + str(metrics.accuracy_score(b_test,b_pred)))
#Apply SVC with RBF kernel
model = svm.SVC(kernel='rbf')
model.fit(a_train,b_train)
b_pred=model.predict(a_test)
print("Accuracy for rbf kernel in SVC " + str(metrics.accuracy_score(b_test,b_pred)))