
import pandas as pd
import os
low_memory=False

df = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})


# Cummulative sum
df1 = df.cumsum(axis = 0, skipna = True)
print(df1.dtypes)
