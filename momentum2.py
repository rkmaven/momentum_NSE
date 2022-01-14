# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:17:05 2022

@author: RAVI
"""


import pandas as pd
from datetime import date
from nsepy import get_history
nifty500_df = pd.read_csv(r'F:\algoTrading\KiteApi\nifty500list.csv')

print('Files Loaded...')


his_data = {}

len_n500 = len(nifty500_df)


try:
    for i in range(501) :
        symbol = nifty500_df.Symbol[i]
        print('Fetching--',i,'   ',symbol)
        #YYYY,MM,DD
        close = (get_history(symbol,start=date(2010,1,1),end=date(2022,1,1))).Close.reset_index()
        his_data[symbol]= close
except Exception as e:
    print('############################################',e)


'''
    dfObj= FP_df[FP_df['Symbol'] == symbol]
    #historical_data(<Exchange>,<Exchange Type>,<Scrip Code>,<Time Frame>,<From Data>,<To Date>)
    #X=client.historical_data('N','D',41998,'15m','2021-09-26','2021-10-25')
    # Clean NaN values
    #df = dropna(df)
    #X = get_history(symbol=ind,start=date(2010,1,1),end=date(2022,1,1))#YYYY,MM,DD
    #Y = X.filter(['Close'])
    #his_data[ind]= Y
    #print('Fetching data -- ',i,'   Symbol: ',ind)

df1 = pd.merge(FP_df,nifty500_df, on='Symbol')
df1.drop(df1[df1['ExchType'] == ''].index, inplace = True)
#df1.drop(df1[df1['ExchType'] == ''].index, inplace = True)

#his_data = {}
scrip_code=[]
ind=[]
#nifty500_df['Scripcode'] = FP_df['Scripcode'].where(FP_df['Symbol'] == nifty500_df['Symbol'])




X=[]
for i in range(len(djhh)):
    symbol = djhh.loc[i,'Scripcode']
    value = client.historical_data('N','D',symbol,'1d','2021-01-01','2021-01-02')
    X.append(value)
'''





