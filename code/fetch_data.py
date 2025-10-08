import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import numpy as np


def get_monthly_data(state_date,end_date):

    # get ETF historical prices from Yahoo Finance
    etf_tickers = ['SPY','AGG']
    # we need to get the dialy returns and then calculate the monthly
    # for historical performance analysis we set the auto_adjust = True to get adjusted close price
    etf_daily_data = yf.download(etf_tickers, start=state_date, end=end_date, auto_adjust=True)['Close']
    etf_monthly_data = etf_daily_data.resample("M").last()
    etf_simple_monthly_returns = etf_monthly_data.pct_change().dropna()
    # Need to calculate the monthly log returns
    etf_log_monthly_returns = np.log(etf_monthly_data/etf_monthly_data.shift(1)).dropna()

    print(etf_simple_monthly_returns)

get_monthly_data('2004-01-01','2025-10-01')
