import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

df = pd.read_csv("TrainingData_small.txt",sep='~',header=None)
dc = pd.read_csv("TrainCategoryMatrix.csv",sep=',',header=None)

print(df.head(10))
#print(df.describe())
#print(dc.head(10))
#print(dc.describe())

#dc[12].hist(bins=50)
#plt.plot(df[0],'o-')
#plt.show()

vocab = {}
docs = {}
text = df.values
n = 0
for line in text:
    #print(line[1])
    for word in line[1].split():
        wd = word.lower()
        
        #print(wd)
        # if wd in vocab:
        #     vocab[wd] += 1
        # else:
        #     vocab[wd] = 1
        if wd in docs:
            docs[wd].append(n)
        else:
            docs[wd] = [n]
        
    n += 1
    #if n == 2:break

Ndocs = n-1
for item in docs:
     vocab[item] = len(docs[item])

print('vocab docs',len(docs))
print('vocab length',len(vocab))
# vocab['word'] = [Id,[doc1,doc2,...],[1,23,...]]
#print(docs)
#print(vocab)
#sys.exit()
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
#for i in range(12000,12010):
#        print(vocab_sort[i])
nmax = len(vocab_sort)
print(nmax)
n=0
vocab_idx = {}

for idx in vocab_sort:
    vocab_idx[n] = idx[1]
    n += 1

#vocab.clear()        
#vocab_sort.clear()


#a = len(vocab_idx) - 200
#b = len(vocab_idx)
#x = range(a,b)
#y = np.array([vocab_idx[i] for i in range(a,b)])

#plt.plot(x,y)

#plt.show()


# Plot total count of a word versus documents
x = np.array([])
y = np.array([])
c = np.array([])
#d = 0
#print(docs['locate'])

# while( d < 500):
#     for word in docs:
#         m = docs[word].count(d)
#         if(m > 10):
#             #print(d,m,word)
#             x.append(d)
#             y.append(m)
#             #print(word,docs[word])
        
#     d += 1

# x=np.array([0,1,2,3,4])
# y=np.array([3,3,2,6,4])
# N=5
# area = (20 * np.random.rand(N))**2 
# c = np.sqrt(area)
# s = 10*x**2
# print(c)
# plt.scatter(x,y,marker='>',s=s,c=c)

# plt.show()

# sys.exit()
w = 0

for word in docs:
    ar = docs[word]
    #print(ar)
    for d in ar:
        m = ar.count(d)

        if(m >= 5):
            x = np.concatenate([x,[d]])
            y = np.concatenate([y,[m]])
            c = np.concatenate([c,[w]])
    w += 1

print(len(x))
print(len(y))
Nwords = len(docs)
maxx = np.amax(x)
maxy = np.amax(y)
N = Nwords
area = (40 * y/maxy)**2
print(Nwords,maxx,maxy)
#c = x/maxx
# Create new color map
cmap = plt.cm.jet
cmaplist= [cmap(i) for i in range(cmap.N)]
cmap = cmap.from_list('Custom cmap', cmaplist,cmap.N)
# define the bins and normalize
bounds = np.linspace(0,N,N+1)
norm = mpl.colors.BoundaryNorm(bounds,cmap.N)
color= ['red' if l == 6 else 'blue' for l in c]

s = y
plt.scatter(x,y,marker='.',s=s, c=color, cmap=cmap, norm=norm)
plt.show()

#df.boxplot(column='ApplicantIncome')
#plt.show()
#df.boxplot(column='ApplicantIncome', by = 'Education')
#plt.show()
#df['LoanAmount'].hist(bins=50)
#plt.show()
#df.boxplot(column='LoanAmount')
#plt.show()
