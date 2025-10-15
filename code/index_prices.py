import pandas as pd
import numpy as np

def cummulative_3m(df,columns_to_process,rolling_value=3,comp_freq=4):
    for col in columns_to_process:
        cummulative_3m = (1+df[col]).rolling(rolling_value).apply(np.prod, raw=True) - 1
        df[f'{col}_{rolling_value}m'] = cummulative_3m
        cummulative_3m_ann = (1+cummulative_3m)**comp_freq-1
        df[f'{col}_{rolling_value}m_ann'] = cummulative_3m_ann
    return df

    
    # spy_3m = (1 + df['SPY']).rolling(3).apply(np.prod, raw=True) - 1
    # vbmfx_3m = (1 + df['VBMFX']).rolling(3).apply(np.prod, raw=True) - 1
    # spy_3m_ann = (1 + spy_3m)**4 - 1
    # vbmfx_3m_ann = (1 + vbmfx_3m)**4 - 1
