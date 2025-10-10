import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import numpy as np
import xlwings as xw
from pathlib import Path
import fred_fuctions

def get_etf_monthly_data(state_date,end_date):
    try:
        # get ETF historical prices from Yahoo Finance
        etf_tickers = ['SPY','AGG','TLT','IEF','SHY','VBMFX','^SP500TR']
        # we need to get the dialy returns and then calculate the monthly
        # for historical performance analysis we set the auto_adjust = True to get adjusted close price
        etf_daily_data = yf.download(etf_tickers, start=state_date, end=end_date, auto_adjust=True)['Close']
        etf_monthly_data = etf_daily_data.resample("M").last()
        etf_simple_monthly_returns = etf_monthly_data.pct_change().dropna()
        etf_simple_monthly_returns.rename(columns={'SPY':'spy_return', 'AGG':'agg_return','TLT':'tlt_return','IEF':'ief_return'},inplace=True) 
        # Need to calculate the monthly log returns
        etf_log_monthly_returns = np.log(etf_monthly_data/etf_monthly_data.shift(1)).dropna()
        etf_log_monthly_returns.rename(columns={'SPY':'spy_log_return', 'AGG':'agg_log_return','TLT':'tlt_log_return','IEF':'ief_log_return'},inplace=True) 
        
        return etf_monthly_data, etf_simple_monthly_returns, etf_log_monthly_returns, 
        # print(etf_log_monthly_returns)


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
        'UNRATE': 'UnemployRate'
    }


    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    macro_data = web.DataReader(list(fred_series.keys()),'fred',start,end)
    macro_data.rename(columns=fred_series)

    macro_month_end = macro_data.resample("M").last()
    print(macro_month_end)   





    
    
    
    
    
    
    
    
    




    # return macro_data



# df = get_macro_data('2004-01-01','2025-10-01')
# out = Path.home() / "Documents" / "data.xlsx"
# df.to_excel(out, index=True)  # index=True is default; keep if you want the index
# print(out)

print(type(get_macro_data('2004-01-01','2025-10-01')))
# get_etf_monthly_data('2004-01-01','2025-10-01')