import datetime
import pandas as pd

"""Function to clean up fred data"""

def yoy_change(x):#yoy change
    return x.pct_change(12)

def mom_change(x):#month over month change
    return x.pct_change(1)

def forward_fill_monthly(x):
    x = x.copy()
    x.index = pd.to_datetime(x.index)
    return x.resample("M").ffill()