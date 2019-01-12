import pandas as pd
import numpy as np
obj=pd.Series([3,4,5],index=['a','b','a'])
print(obj)
print(obj[obj>3])

obj=pd.Series(np.arange(4.0),index=['a','b','c','d'])
print(obj)
data=pd.DataFrame(np.arange(16).reshape(4,4),index=['oh','color','utahs','new york'],columns=['one','two','three','four'])
print(data)

print(data[data['one']>5])
data[data<5]=0
print(data)

print(data.loc['utahs',['one','two']])

print(data.iloc[3,[0,2]])

print(data.loc[:'utahs','one'])

ser2=pd.Series(np.arange(3.),index=['a','b','c'])
print(ser2)
print(ser2[-1])
print(ser2.iloc[:1])

obj=pd.Series([4,11,2,3])
print(obj.rank(method='min',ascending=True))

data=pd.DataFrame(np.arange(16).reshape(4,4),index=['oh','color','utahs','new york'],columns=['one','two','three','four'])
print(data)
print(data.unstack())
print(data.unstack().stack())