import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import time
import datetime
from datetime import datetime
import collections
import os

data=pd.read_csv("C:\\Users\\dell\\desktop\\afterDC.csv")


a=data.loc[:,"date"]
b=data.loc[:,"time"]
print (a[0], b[0])
type(a)

temp = a+"_"+b
timeformat="%Y.%m.%d_%H:%M:%S %p"

new=[datetime.strptime(x, timeformat) for x in temp]

print("temp =",type(temp),"\n""new =",type(new),"\n""data.time =",type(data.date))

data.time=new

data.rename(columns={'time': 'newtime'}, inplace=True) 
del data["date"]      #we dont need it anymore as all stored in date.time

tur=data.country == "turkey"
real=data.richter > 3.5


cit=data[tur & real].city
cits=cit.unique()

print("Total Cities =",cit.size)

a=0
for i in cits:
    a=a+1
    if a==len(cits):
        print("Unique Cities = {}".format(a))

f=Counter(cit)
newf=f.most_common()

print(type(f))
print(type(newf))

data["year"]=[int(datetime.strftime(x,"%Y")) for x in data.newtime]
data["month"]=[int(datetime.strftime(x,"%m"))+int(datetime.strftime(x,"%Y"))*12 for x in data.newtime]
data.info()
data.head(2)

def draw(ci,t1,t2,ri,w=1,fre="month",bn=40):
    if ci=="all":
        where=data.city
    else:
        where=data.city == ci
    
    t11=data.year > t1 
    t22=data.year < t2
    real=data.richter > ri
    tur=data.country == "turkey"
    
    if (ci in cit.values or ci=="all"):
        data_tr=data[tur & real & where & t11 & t22]
        print("Recorded Earthquake=",data_tr.size)
        
        if w==1:
            plt.plot(data_tr.newtime,data_tr.richter, color="green",linewidth=0.15,alpha = 0.7)
            plt.title('Intensity of Eartquake & Time in Turkey-{}, intensity >{} between {}-{}'.format(ci[0].upper()+ci[1:],ri,t1,t2))
            plt.ylabel('Richter')
            plt.xlabel('Year') 
        elif w==2:
            plt.scatter(data_tr.month,data_tr.richter,15, color="red",alpha = 0.2)
            plt.title('Intensity of Eartquake & Time in Turkey-{}, intensity >{} between {}-{}'.format(ci[0].upper()+ci[1:],ri,t1,t2)) 
            plt.ylabel('Richter')
            plt.xlabel('Cumulative Months') 
        elif w==3:
            plt.hist(data_tr[fre],bins=bn, color="blue",linewidth=0.15,alpha = 0.7)
            plt.title('Frequency of Eartquake & Year in Turkey-{}, intensity >{} between {}-{}'.format(ci[0].upper()+ci[1:],ri,t1,t2))
            plt.ylabel('Total Number')
            plt.xlabel(fre)
            
        plt.legend(loc='upper right')     
        plt.show()
        
    elif (ci not in cit.values and ci !="all"):
        print("False city name, write existing city name from list")
        print("\n",cits)
    elif t1 not in data[tur & real & where].year.values or t1 not in data[tur & real & where].year.values:
        print("False start or finish year, write existing year from list")
        print("\n",data[tur & real].year.unique())
    else:
        print("Wrong city name and years")
        
draw("all",2004,2017,3)
draw("all",2004,2017,4)
draw("all",2004,2017,3,2)

draw("all",2004,2017,0,3,"year")
draw("all",2004,2017,0,3,"month",10)
draw("all",2004,2017,0,3,"lat",30)
draw("all",2004,2017,0,3,"long",30)
