import datetime
import pandas as pd

"""Function to clean up fred data"""

def yoy_change(df):#yoy change
    return df.pct_change(12,fill_method=None)

def mom_change(df):#month over month change
    return df.pct_change(1,fill_method=None)

def forward_fill(df): #fills in NA/Missing data using the previous value
    x = df.copy()
    x.index = pd.to_datetime(x.index)
    x = x.ffill()
    return x.ffill()

def resample_me(df):# takes month-end values
    return df.resample("ME").last()

def shift_lag(df,lag_months=1):
    return df.shift(lag_months)

def rolling_3m(df,columns_to_process): # calculates the rolling 3m avg and then annualizes that value
    new_df = pd.DataFrame()
    for col in columns_to_process:
        new_col_name_3m = f"{col}_r3m"
        new_col_name_annualized = f"{col}_ann_r3m"
        avg_3m_rolling = df[col].rolling(window=3).mean()
        new_df[new_col_name_3m] =avg_3m_rolling 
        new_df[new_col_name_annualized] = ((1 + avg_3m_rolling)**12) - 1 
    return new_df

def rename_columns(df,columns_dictionary):
    return df.rename(columns=columns_dictionary,inplace=True)

def credit_spread(df,lag_months,delta_calc=False):
    rate_col =  ['Mort30Y', 'UST10Y', 'UST2Y', 'UST3M', 'TIPS10Y','CorpBAA', 'CorpAAA', 'FedFundsRate']
    # result_col,col1_input,col2_input
    spread_logic = [
        ('Slope_10Y_2Y',"UST10Y","UST2Y"),
        ('Slope_10Y_3M',"UST10Y","UST3M"),
        ('Slope_10Y_FF',"UST10Y","FedFundsRate"),
        ('InfExp_10Y',"UST10Ym","TIPS10Y"),
        ('BAA_minus_10Y','CorpBAA','UST10Y'),
        ('AAA_minus_10Y','CorpAAA','UST10Y'),
        ('BAA_minus_AAA','CorpBAA','CorpAAA')
    ]
    check_col = [col for col in rate_col if col in df.columns]
    if not check_col:
        return pd.DataFrame()
    m = df[check_col].copy()
    m.index=pd.to_datetime(m.index)
    X = m.resample("ME").last()

    for result_col,col1_input,col2_input in spread_logic:
        if col1_input in X.columns and col2_input in X.columns:
            X[result_col] = X[col1_input]-X[col2_input]
    
    if delta_calc==True:
        cols_to_diff = X.columns.copy()
        for period in [1,3]:
            X=X.assign(**{
                f'{col}_Delta{period}m': X[col].diff(period) 
                for col in cols_to_diff
            })
    else:
        pass
    
    if lag_months > 0:
        X =X.shift(lag_months)
    return X.dropna(how='all')






