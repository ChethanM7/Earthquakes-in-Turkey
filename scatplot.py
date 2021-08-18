import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")
x=data.md
y=data.ms
plt.scatter(x,y)
plt.title('Scatter plot b/w Richter and Depth')
plt.xlabel('Duration magnitude [MD]')
plt.ylabel('Surface wave Magnitude [MS]')
plt.show()
corr, _=pearsonr(x,y)
print(corr)