import datetime
import pandas as pd

"""Function to clean up fred data"""

def yoy_change(df):#yoy change
    return df.pct_change(12)

def mom_change(df):#month over month change
    return df.pct_change(1)

def forward_fill(df):
    x = df.copy()
    x.index = pd.to_datetime(x.index)
    x = x.ffill()
    return x.ffill()

def resample_me(df):
    return df.resample("ME").last()


