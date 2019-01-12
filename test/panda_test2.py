
import datetime
import  re
import pandas as pd
import numpy as np
import pandas_datareader.data as web
"""
start = datetime.datetime(2016, 1, 1) # or start = '1/1/2016'
end = datetime.date.today()
prices = web.DataReader('AAPL', 'yahoo', start, end)
print( prices.head())  # print first rows of the prices data


prices.to_csv("d://a.txt")
writer=pd.ExcelWriter("D://output1.xlsx")
prices.to_excel(writer,'Sheet1')
writer.save()
"""

"""
all_data = {ticker: web.get_data_yahoo(ticker)
            for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

all_data=pd.DataFrame(all_data)
writer=pd.ExcelWriter("D://output1.xlsx")
all_data.to_excel(writer,'Sheet1')
writer.save()

print(all_data["AAPL"])
"""
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
print(pd.value_counts(cats))
cats2=pd.qcut(bins,3)
print(pd.value_counts(cats2))

data = pd.DataFrame(np.random.randn(1000, 4))
print(data)

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
print(df)

sampler = np.random.permutation(5)
print(sampler)

str='ppp\\x'
str.find(":")

pattern=r'\\x'

reg=re.compile(pattern)
print(reg.findall(str))