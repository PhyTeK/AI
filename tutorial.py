from sklearn.datasets import make_multilabel_classification

# this will generate a random multi-label dataset
x, y = make_multilabel_classification(sparse = True, n_labels = 20,return_indicator = 'sparse', allow_unlabeled = False)

print(y)
#print(y)
