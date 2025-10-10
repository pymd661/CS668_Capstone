import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import numpy as np
import xlwings as xw
from pathlib import Path
import fred_functions

 
def get_etf_monthly_data(start_date,end_date):
    try:
        # get ETF historical prices from Yahoo Finance
        etf_tickers = ['SPY','AGG','TLT','IEF','SHY','VBMFX','VUSTX']
        etf_daily_data = yf.download(etf_tickers, start=start_date, end=end_date, auto_adjust=True,interval="1d",actions=False,progress=False,threads=False,repair=False)['Close']
        return etf_daily_data


    except Exception as e:
        print(f"Error:{e}")
        return None
    

def get_macro_data(start_date,end_date):

    fred_series = {
        'CPIAUCSL': 'CPI',
        'CPILFESL': 'CoreCPI',
        'INDPRO': 'IndustrialProd',
        'RSXFS': 'RealRetail',
        'DGS10': 'UST10Y',
        'DGS2': 'UST2Y',
        'DGS3MO':'UST3M',
        'DFII10': 'TIPS10Y',
        'MORTGAGE30US': "Mort30Y",
        'PERMIT': 'Permits',
        'DBAA': 'CorpBAA',
        'DAAA': 'CorpAAA',
        'BAMLCC0A0CMTRIV': 'CorpTotRetIndex',
        'DFF': 'FedFundsRate',
        'GDPC1': 'RealGDP',
        'UNRATE': 'UnemploymentRate'
    }

    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    macro_data = web.DataReader(list(fred_series.keys()),'fred',start,end)
    macro_data.rename(columns=fred_series,inplace=True)

    print(macro_data)
    # return macro_data


df = get_etf_monthly_data('2004-01-01','2025-10-01')
print (df)

# df = get_macro_data('2004-01-01','2025-10-01')
# out = Path.home() / "Documents" / "data.xlsx"
# df.to_excel(out, index=True)  # index=True is default; keep if you want the index
# print(out)

# print(type(get_macro_data('2004-01-01','2025-10-01')))