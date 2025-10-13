import datetime
import pandas as pd

"""Function to clean up fred data"""

def yoy_change(df):#yoy change
    return df.pct_change(12,fill_method=None)

def mom_change(df):#month over month change
    return df.pct_change(1,fill_method=None)

def forward_fill(df):
    x = df.copy()
    x.index = pd.to_datetime(x.index)
    x = x.ffill()
    return x.ffill()

def resample_me(df):
    return df.resample("ME").last()

def shift_lag(df,lag_months=1):
    return df.shift(lag_months)

def rolling_3m(df,columns_to_process):
    new_df = pd.DataFrame()
    for col in columns_to_process:
        new_col_name_3m = f"{col}_rolling_3m_avg"
        new_col_name_annualized = f"{col}_annual_rolling_3m"
        avg_3m_rolling = df[col].rolling(window=3).mean()
        new_df[new_col_name_3m] =avg_3m_rolling 
        new_df[new_col_name_annualized] = ((1 + avg_3m_rolling)**12) - 1 
    return new_df

def rename_columns(df,columns_dictionary):
    return df.rename(columns=columns_dictionary,inplace=True)





