# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:38:18 2022

@author: RAVI
"""
import pandas as pd
from datetime import date
from nsepy import get_history
'''
from py5paisa import FivePaisaClient


cred={
    "APP_NAME":"5P57637993",
    "APP_SOURCE":"7720",
    "USER_ID":"e1L12fr6iRt",
    "PASSWORD":"PWqz3zxldBT",
    "USER_KEY":"iSihDpbbJvK7T6nIa3OZQh2lIOQrZHrg",
    "ENCRYPTION_KEY":"JehOKyqhZwx8SNZqMDJN357dIOD1SfYO"
    }

client = FivePaisaClient(email="rk.maven@gmail.com", passwd="#MY5paisa", dob="19901129",cred=cred)
client.login()
'''

FP_df = pd.read_csv(r'F:\algoTrading\KiteApi\scripmaster-csv-format.csv')
FP_df.rename(columns = {'Name':'Symbol'}, inplace = True)
FP_df.drop(FP_df[FP_df['Exch'] == 'B'].index, inplace = True)
FP_df.drop(FP_df[FP_df['ExchType'] != 'C'].index, inplace = True)
#FP_df.drop(FP_df[FP_df['Series'] != 'EQ'].index, inplace = True)
FP_df = FP_df.loc[(FP_df['Series'] == 'EQ') | (FP_df['Series'] == 'BE')]


nifty500_df = pd.read_csv(r'F:\algoTrading\KiteApi\nifty500list.csv')

print('Files Loaded...')


code_df=FP_df.loc[FP_df['Symbol'].isin(nifty500_df['Symbol'])]
code_df.reset_index(inplace = True)
code_df.drop(['index','Expiry'],axis=1,inplace = True)

data_df = pd.DataFrame()

his_data = {}

len_n500 = len(code_df)


try:
    for i in range(2) :
        symbol = get_history(symbol=code_df.Symbol[0]
        close = (,start=date(2010,1,1),end=date(2022,1,1))).Close.reset_index()#YYYY,MM,DD
        his_data[](close)

except Exception:
    
    print(Exception())


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





