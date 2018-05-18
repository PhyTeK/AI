import numpy as np
X = np.random.randint(5, size=(10, 100))
y = np.array([1, 2, 3, 4, -3, 6,7,8,9,10])
#print(X)
#print(y)
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
print(X[2:3])
print(clf.predict(X[4:5]))
