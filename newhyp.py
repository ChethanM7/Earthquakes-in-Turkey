import pandas as pd
import statistics as st
data=pd.read_csv("C:\\Users\\dell\\desktop\\afterNORM.csv")
def twoSampZ(x1,x2,mudiff,sd1,sd2,n1,n2):
    from numpy import sqrt,abs,round
    from scipy.stats import norm
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z=((x1-x2)-mudiff)/pooledSE
    pval=2*(1-norm.cdf(abs(z)))
    return round(z,3), round(pval,4)

north=data[data.direction=='north']
south=data[data.direction=='south']
s1=north.richter.mean()
s2=south.richter.mean()
sd1=st.stdev(north.richter)
sd2=st.stdev(south.richter)
n1=576
n2=605
z,p=twoSampZ(s1,s2,0,sd1,sd2,n1,n2)
print(z) #-0.086
print(p) #0.9313
