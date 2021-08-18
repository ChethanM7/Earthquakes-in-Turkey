import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")
names=['id','lat','long','dist','depth','xm','md','richter','ms','mb']
correlations=data.corr()
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(correlations,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=np.arange(0,8,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_xticklabels(names)
plt.show()

