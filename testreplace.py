import pandas as pd

categ_test_c = pd.read_csv("TestTruth.csv",sep=',',header=None)
new = categ_test_c.replace(-1,0)
print(new)

df = pd.DataFrame({0:[-1,-1,1,-1],1:[1,1,-1,-1]})
dfr = df.replace(-1,0)
print(dfr)

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                    'B': [5, 6, 7, 8, 9],
                    'C': ['a', 'b', 'c', 'd', 'e']})
dfr = df.replace(0, 5)
print(dfr)
