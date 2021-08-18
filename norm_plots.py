import pandas as pd
import numpy as np
data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")
print("BEFORE STANDARDIZATION")
print(np.mean(data["ms"]))
print(np.var(data["ms"]))

data1=pd.read_csv("C:\\Users\\dell\\desktop\\afterNORM.csv")
#data1["ms"].plot(kind='bar')
print("\nAFTER STANDARDIZATION")
print(np.mean(data1["ms"]))
print(np.var(data1["ms"]))
data1["ms"].plot(kind="bar")



