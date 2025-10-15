import pandas as pd
import numpy as np

def cummulative_return(df,columns_to_process,rolling_value=3,comp_freq=4):
    for col in columns_to_process:
        cummulative_3m = (1+df[col]).rolling(rolling_value).apply(np.prod, raw=True) - 1
        df[f'{col}_{rolling_value}m'] = cummulative_3m
        cummulative_3m_ann = (1+cummulative_3m)**comp_freq-1
        df[f'{col}_{rolling_value}m_ann'] = cummulative_3m_ann
    return df

def ln_return(df,columns_to_process,rolling_value=3,comp_freq=12):
        ln_3m = np.log1p(df) # calculate the natural log of the returns
        ann_ln_3m = (ln_3m.rolling(window=3).mean()) * 12 # avg of the natural log returns, rolling 3 months
        return ln_3m, ann_ln_3m