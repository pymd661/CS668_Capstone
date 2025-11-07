import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import numpy as np
import xlwings as xw
from pathlib import Path
import fred_functions

def get_etf_monthly_data(start_date,end_date):
    """Gets the daily adjusted close returns"""
    try:
        # get ETF historical prices from Yahoo Finance
        etf_tickers = ['SPY','AGG','TLT','IEF','SHY','VBMFX','VUSTX','VFITX',"VFISX","VT","EFA","EWU","EWS","EWJ","EWG","EWH","EWC","MDY","VGTSX","VTIAX","VTMGX",'ACWX']
        etf_daily_data = yf.download(etf_tickers, start=start_date, end=end_date, auto_adjust=True,interval="1d",actions=False,progress=False,threads=False,repair=False)['Close']
        return etf_daily_data
    except Exception as e:
        print(f"Error:{e}")
        return None
    
def get_macro_data(start_date,end_date):
    """Gets the macro indicators"""
    try:
        fred_series = {
            'GDPC1': 'RealGDP',
            'UNRATE': 'UnemploymentRate',
            'PERMIT': 'Permits',
            'CPIAUCSL': 'CPI',
            'CPILFESL': 'CoreCPI',
            'INDPRO': 'IndustrialProd',
            'MRTSSM44000USS': 'RetailTrade',
            'MORTGAGE30US': "Mort30Y",
            'DGS10': 'UST10Y',
            'DGS2': 'UST2Y',
            'DGS3MO':'UST3M',
            'DBAA': 'CorpBAA',
            'DAAA': 'CorpAAA',
            'BAMLCC0A0CMTRIV': 'CorpTotRetIndex',
            'DFF': 'FedFundsRate'
        }

        #  'DFII10': 'TIPS10Y' - data only available in for 2003
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        macro_data = web.DataReader(list(fred_series.keys()),'fred',start,end)
        macro_data.rename(columns=fred_series,inplace=True) #rename columns using dictionary
        return macro_data
    except Exception as e:
        print(f"Error:{e}")
        return None

def to_excel(df,file_name):
    out = Path.home() /"Documents"/"cs668"/"CS668_Capstone"/file_name
    df.to_excel(out, index=True)  # index=True is default; keep if you want the index

# Create a dataframe for macro indicators and for returns
df_macro = get_macro_data('1985-01-01','2025-10-01')
df_returns = get_etf_monthly_data('1985-01-01','2025-10-01')

# Call to_excel function to save as excel
to_excel(df_macro,"df_macro.xlsx")
to_excel(df_returns,"df_prices.xlsx")