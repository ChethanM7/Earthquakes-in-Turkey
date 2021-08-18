import pandas as pd
data=pd.read_csv("C:\\Users\\dell\\desktop\\earthquake.csv")
print(data)

mw_mean=data.mw.mean()
data["mw"].fillna(mw_mean,inplace=True)

print(data)

ms_mean=data.ms.mean()
data["ms"].fillna(ms_mean,inplace=True)

mb_mean=data.mb.mean()
data["mb"].fillna(mb_mean,inplace=True)

richter_mean=data.richter.mean()
data["richter"].fillna(richter_mean,inplace=True)

md_mean=data.md.mean()
data["md"].fillna(md_mean,inplace=True)

xm_mean=data.xm.mean()
data["xm"].fillna(xm_mean,inplace=True)

depth_mean=data.depth.mean()
data["depth"].fillna(depth_mean,inplace=True)

dist_mean=data.dist.mean()
data["dist"].fillna(dist_mean,inplace=True)

long_mean=data.long.mean()
data["long"].fillna(long_mean,inplace=True)

lat_mean=data.lat.mean()
data["lat"].fillna(lat_mean,inplace=True)

print(data)

mainfile=data.to_csv("C:\\Users\\dell\\desktop\\afterDC.csv",index=None,header=True)

from sklearn import preprocessing

import numpy as np

x=data[["mw"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["mw"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["mw"]=pd.DataFrame(standard)


x=data[["ms"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["ms"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["ms"]=pd.DataFrame(standard)

x=data[["mb"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["mb"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["mb"]=pd.DataFrame(standard)

x=data[["richter"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["richter"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["richter"]=pd.DataFrame(standard)

x=data[["md"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["md"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["md"]=pd.DataFrame(standard)


x=data[["xm"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["xm"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["xm"]=pd.DataFrame(standard)

x=data[["depth"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["depth"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["depth"]=pd.DataFrame(standard)


x=data[["dist"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["dist"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["dist"]=pd.DataFrame(standard)


x=data[["lat"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["lat"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["lat"]=pd.DataFrame(standard)

x=data[["long"]].values.astype(float)
min_max_scalar=preprocessing.MinMaxScaler();
x_scaled=min_max_scalar.fit_transform(x)
data["long"]=pd.DataFrame(x_scaled)
standard=preprocessing.scale(x)
data["long"]=pd.DataFrame(standard)

mainfile=data.to_csv("C:\\Users\\dell\\desktop\\afterNORM.csv",index=None,header=True)

