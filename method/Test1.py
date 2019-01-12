from sklearn import datasets
from sklearn import svm
import pickle

iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)
print("-----targe")
print(digits.target)
print("-----image")
print(digits.images[0])

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))

X, y = iris.data, iris.target
clf.fit(X, y)
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])