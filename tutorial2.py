from sklearn.datasets import make_multilabel_classification
from sklearn.model_selection import train_test_split

x, y = make_multilabel_classification(sparse = True, n_labels = 5,
    return_indicator = 'sparse', allow_unlabeled = False)
print(x)
# using binary relevance
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.naive_bayes import GaussianNB

# initialize binary relevance multi-label classifier
# with a gaussian naive bayes base classifier
#classifier = BinaryRelevance(GaussianNB())

# train
#classifier.fit(x_train, y_train)

# predict
#predictions = classifier.predict(x_test)
