import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

df = pd.read_csv("TrainingData.txt",sep='~',header=None)
dc = pd.read_csv("TrainCategoryMatrix.csv",sep=',',header=None)

print(df.head(10))
#print(df.describe())
#print(dc.head(10))
#print(dc.describe())

#dc[12].hist(bins=50)
#plt.plot(df[0],'o-')
#plt.show()

vocab = {}
par = {}
text = df.values
n = 0
for line in text:
    #print(line[1])
    for word in line[1].split():
        wd = word.lower()

        #print(wd)
        if wd in vocab:
            vocab[wd] += 1
        else:
            vocab[wd] = 1
    n += 1
    #if n==10:break

# vocab['word'] = [Id,[doc1,doc2,...],[1,23,...]]

# wdId = 0
# for line in text:
#     for word in line[1].split():
#         wd = word.lower()
#         wordindoc = 1
#         #print(wd)
#         if wd in vocab:
#             try:
#                 idxdoc = vocab[wd][1].index(n)
#                 vocab[wd][2][idxdoc] += 1
#             except:
#                 vocab[wd][1].append(n)
#                 vocab[wd][2].append(1)

#         else:
            
#             vocab[wd] = [wdId,[n],[1]]
#             wdId += 1

#     n += 1
#     if n==10000:break

# print(vocab[1][100])

# sys.exit()

#voc ={}
#for n in vocab:
#    voc[vocab[1][0]] = sum(vocab[1][2])
vocab_sort = sorted(vocab.items(), key=lambda x: x[1])
for i in range(120000,120010):
        print(vocab_sort[i])
nmax = len(vocab_sort)
print(nmax)
n=0
vocab_idx = {}

for idx in vocab_sort:
    vocab_idx[n] = idx[1]
    n += 1

#vocab.clear()        
#vocab_sort.clear()




a = 127000
b = 127900
x = range(a,b)
y = np.array([vocab_idx[i] for i in range(a,b)])

plt.plot(x,y)

plt.show()


# Analyse each doc using the vocabulary



#df.boxplot(column='ApplicantIncome')
#plt.show()
#df.boxplot(column='ApplicantIncome', by = 'Education')
#plt.show()
#df['LoanAmount'].hist(bins=50)
#plt.show()
#df.boxplot(column='LoanAmount')
#plt.show()
