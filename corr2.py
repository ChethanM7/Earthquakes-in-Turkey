import pandas as pd
import numpy as np # linear algebra

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import time
import datetime
from datetime import datetime
import collections
data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()