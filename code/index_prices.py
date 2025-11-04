import pandas as pd
import numpy as np

def cummulative_return(df,columns_to_process,rolling_value=3,comp_freq=4):
    'calculates the cumulative return, user has to give columns, rolling window, and compounding frequency'
    
    df_mod = df.copy()
    for col in columns_to_process:
        cummulative_3m = (1+df_mod[col]).rolling(rolling_value).apply(np.prod, raw=True) - 1 # calculates a growth factor based on a rolling period
        df_mod[f'{col}_{rolling_value}m'] = cummulative_3m # creates rolling cumulative return column
        cummulative_3m_ann = (1+cummulative_3m)**comp_freq-1 # annualized
        df_mod[f'{col}_{rolling_value}m_ann'] = cummulative_3m_ann # creates annualized column
        sd_3m = df_mod[col].rolling(rolling_value).std() # calculates the std
        df_mod[f'{col}_3m_sd'] = sd_3m # creates std column
        df_mod[f'{col}_3m_ann_sd'] = sd_3m * np.sqrt(comp_freq) # creates the annualized std/volatility

    return df_mod

def ln_return(df,columns_to_process,rolling_value=3,comp_freq=12):
    df_mod = df.copy()
    for col in columns_to_process:
        ln_3m = np.log1p(df_mod[col]) # calculate the natural log of the returns
        df_mod[f'{col}_ln_3m'] = ln_3m
        ann_ln_3m = (ln_3m.rolling(window=rolling_value).mean()) * comp_freq # avg of the natural log returns, rolling 3 months
        df_mod[f'{col}_ann_ln_3m'] = ann_ln_3m
    return df_mod