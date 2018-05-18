import numpy as np  # a conventional alias
from sklearn.feature_extraction.text import CountVectorizer

filenames = ['data/austen-brontë/Austen_Emma.txt',
                 'data/austen-brontë/Austen_Pride.txt',
                 'data/austen-brontë/Austen_Sense.txt',
                 'data/austen-brontë/CBronte_Jane.txt',
                 'data/austen-brontë/CBronte_Professor.txt',
                 'data/austen-brontë/CBronte_Villette.txt']
vectorizer = CountVectorizer(input='filename')
dtm = vectorizer.fit_transform(filenames)  # a sparse matrix
vocab = vectorizer.get_feature_names()  # a list
print(type(dtm))
dtm = dtm.toarray()
vocab = np.array(vocab)
print( filenames[0] == 'data/austen-brontë/Austen_Emma.txt')
house_idx = list(vocab).index('house')
print(dtm[0, house_idx])
print(dtm[0, vocab == 'house'])


from sklearn.metrics.pairwise import euclidean_distances
dist = euclidean_distances(dtm)
print(np.round(dist, 1))
print(dist[1, 3])
print(dist[3, 5])
from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(dtm)
print(np.round(dist, 2))


import os
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]

names = [os.path.basename(fn).replace('.txt', '') for fn in filenames]

# color-blind-friendly palette
for x, y, name in zip(xs, ys, names):
     color = 'orange' if "Austen" in name else 'skyblue'
     plt.scatter(x, y, c=color)
     plt.text(x, y, name)

plt.show()

mds = MDS(n_components=3, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2]))
for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
     ax.text(x, y, z, s)
plt.show()

# Ward's method
from scipy.cluster.hierarchy import ward, dendrogram
linkage_matrix = ward(dist)
# match dendrogram to that returned by R's hclust()
print(dendrogram(linkage_matrix, orientation="right", labels=names))
plt.tight_layout()
plt.show()


# Exercise_1

situation_idx = list(vocab).index('situation')
print(dtm[0, situation_idx])
print(dtm[0, vocab == 'situation'])

# Exercise_2

text1 = "Indeed, she had a rather kindly disposition."

text2 = "The real evils, indeed, of Emma's situation were the power of having rather too much her own way, and a disposition to think a little too well of herself;"

text3 = "The Jaccard distance is a way of measuring the distance from one set to another set."


texts = [text1,text2,text3]

#vectorizer = CountVectorizer(input='content')
vectorizer = CountVectorizer()
dtm = vectorizer.fit_transform(texts)  # a sparse matrix
vocab = vectorizer.get_feature_names()  # a list
print(type(dtm))
dtm = dtm.toarray()
print(dtm)
vocab = np.array(vocab)
print(vocab)

#Exercise_3
eudist = euclidean_distances(dtm)
print("Euclidean distance")
print(eudist)

#from scipy.spatial.distance import jaccard
from sklearn.metrics import jaccard_similarity_score as jaccard
#print(help(jaccard))
print("Jaccad distance")
print('[',end='')
for i in range(0,3):
    print('[',end='')
    for j in range(0,3):
        dist = 1.0 - jaccard(dtm[i],dtm[j])
        print('{0:0.8f}'.format(dist),end='\t'),

    print(']',end='\n')
print(']',end='\n')
from sklearn.metrics.pairwise import cosine_distances
cosdist = cosine_distances(dtm)
print("Cosine distance")
print(cosdist)
