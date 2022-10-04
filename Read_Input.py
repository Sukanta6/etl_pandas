
import pandas as pd
import os
#low_memory=False

df = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})


# Cummulative sum
df1 = df.cumsum(axis = 0, skipna = True)
print(df1.dtypes)


lst = [['AAA',2019,15],['BBB',2019,16],['BBB',2020,22],['AAA',2020,-20],['CCC',2019,11],['AAA',2021,10]]
df = pd.DataFrame(lst,columns = ['name','year','val'])


#df.loc[df['name'].isin(df.loc[df['val'].lt(0), 'name']), 'val'] = 1

df.loc[df['val'].lt(0).groupby(df['name']).transform('any'), 'val'] = 1

df['new_col'] = df.groupby('name')['val'].transform(lambda x: (x < 0).any() )



print(df1.dtypes)