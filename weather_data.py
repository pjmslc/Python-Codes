from dateutil import parser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stg=pd.read_csv('stg_weather.csv',dtype={'DATE':'str'},low_memory=False,na_values='NaN')
slc=pd.read_csv('slc_weather.csv',dtype={'DATE':'str'},low_memory=False)
slc_dates=slc['DATE'].tolist()
stg_dates=stg['DATE'].tolist()
slc['DATE']=pd.to_datetime(pd.Series(slc_dates))
stg['DATE']=pd.to_datetime(pd.Series(stg_dates))

slc.index=slc['DATE']
stg.index=stg['DATE']

del slc['DATE']
del stg['DATE']



slc[['temp','visibility','dp','ws','wgs','p','pt','precip_amt']]=slc[['temp','visibility','dp','ws','wgs','p','pt','precip_amt']].apply(pd.to_numeric,errors='coerce')


#GRAPHING#
slc.loc['Jun 2008':'August 2008',['temp','dp']].plot(title='Summer 2008 Temp and Dewpoint')
plt.ylabel('Degrees F')
plt.show()


#upsample to threeday maxes and mins -because monsoon surges tend to last in days not weeks
temp_maxs=slc.temp['Jun 2008': 'August 2008'].resample('D').max()
temp_mins=slc.temp['Jun 2008': 'August 2008'].resample('D').min()
dewpoint=slc.dp['Jun 2008':'August 2008'].resample('D').mean()


temp_spreads=temp_maxs-temp_mins



temp_spreads.plot(title='Daily Temp Spread and Dewpoint')
dewpoint.plot()
plt.ylabel('Degrees F')
plt.show()
