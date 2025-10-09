import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import numpy as np


def get_etf_monthly_data(state_date,end_date):
    try:
        # get ETF historical prices from Yahoo Finance
        etf_tickers = ['SPY','AGG']
        # we need to get the dialy returns and then calculate the monthly
        # for historical performance analysis we set the auto_adjust = True to get adjusted close price
        etf_daily_data = yf.download(etf_tickers, start=state_date, end=end_date, auto_adjust=True)['Close']
        etf_monthly_data = etf_daily_data.resample("M").last()
        etf_simple_monthly_returns = etf_monthly_data.pct_change().dropna()
        etf_simple_monthly_returns.rename(columns={'SPY':'spy_return', 'AGG':'agg_return'},inplace=True) 
        # Need to calculate the monthly log returns
        etf_log_monthly_returns = np.log(etf_monthly_data/etf_monthly_data.shift(1)).dropna()
        etf_log_monthly_returns.rename(columns={'SPY':'spy_log_return', 'AGG':'agg_log_return'},inplace=True) 

        print(etf_log_monthly_returns)


    except Exception as e:
        print(f"Error:{e}")
        return None
    

def get_macro_data(start_date,end_date):

    fred_series = {
        'CPIAUCSL': 'CPI_YoY',
        'CPILFESL': 'Core CPI',
        'INDPRO': 'Industrial Production',
        'RSXFS': 'Real Retail Sales',
        'DGS10': '10_Yr_Treasury_Yield',
        'DGS2': '2_Yr_Treasury_Yield',
        'DGS3MO':'3_Month_Treasury_Yield',
        'DFII10': '10_Yr_Tips',
        'MORTGAGE30US': "30_Year_Avg_Mortgage",
        'PERMIT': 'PERMIT',
        'BAA': 'Corporate_Yield_1',
        'AAA': 'Corporate_Yield_2',
        'FEDFUNDS': 'Fed_Funds_Rate',
        'GDPC1': 'GDP_Real',
        'UNRATE': 'Unemployment_Rate'
    }


    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    macro_data = web.DataReader(list(fred_series.keys()),'fred',start,end)
    print(macro_data)

get_macro_data('2004-01-01','2025-10-01')
# get_etf_monthly_data('2004-01-01','2025-10-01')