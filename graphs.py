import pandas as pd
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns #visualization
#from plotly.offline import init_notebook_mode, iplot

data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")

#graph-1
data.city.value_counts().plot(kind = "bar" , color = "red" ,
                      figsize = (30,10),fontsize = 20)
plt.xlabel("City",fontsize=18,color="blue")
plt.ylabel("Frequency",fontsize=18,color="blue")
plt.show()

#graph-2
