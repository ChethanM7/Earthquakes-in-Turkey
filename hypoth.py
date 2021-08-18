#independent t test
#NULL HYP - there is no significant diff in the avg richter of east and west directed earthquakes
#ALT HYP - there is significant diff in the avg richter of east and west directed earthquakes
import pandas as pd
import statistics as st
data=pd.read_csv("C:\\Users\\dell\\desktop\\earthquake.csv")
east=data[data.direction=='east']
west=data[data.direction=='west']


data1=pd.read_csv("C:\\Users\\dell\\desktop\\earthquake.csv")

print(st.variance(data1.richter))


mean1=data1.richter.groupby(data1.direction).mean()
print(mean1)

north=data1[data1.direction=='north']
south=data1[data1.direction=='south']

#from scipy.stats import ttest_ind
#import scipy.stats
from scipy import stats
hyp=stats.zcore(east.richter,west.richter)#equal_var=False)
print(hyp)

#pvalue = 0.3204 > 0.05
#Hence NULL hypothesis is not rejected