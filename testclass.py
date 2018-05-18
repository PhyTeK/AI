import numpy as np
from sklearn import preprocessing

lb = preprocessing.LabelBinarizer()
lb.fit(np.array([[0, 1, 1], [1, 0, 0]]))

print(lb.classes_)

print(lb.transform([0, 1, 2, 1]))
