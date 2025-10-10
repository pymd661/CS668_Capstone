import datetime
import pandas as pd

"""Function to clean up fred data"""

def yoy_change(x):#yoy change
    return x.pct_change(12)

def mom_change(x):#month over month change
    return x.pct_change(1)

def forward_fill_monthly(x):
    s = s.copy()
    s.index = pd.to_datetime(s.index)
    return s.resample("M").ffill()