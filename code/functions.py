# column groups

def column_order():
    # Index fund groups
    spy_group = [
        "SPY",
        "SPY_mom",
        "SPY_3m",
        "SPY_3m_ann",
        "SPY_3m_sd",
        "SPY_3m_ann_sd",
        "SPY_ln_3m",
        "SPY_ann_ln_3m",
    ]

    vbmfx_group = [
        "VBMFX",
        "VBMFX_mom",
        "VBMFX_3m",
        "VBMFX_3m_ann",
        "VBMFX_3m_sd",
        "VBMFX_3m_ann_sd",
        "VBMFX_ln_3m",
        "VBMFX_ann_ln_3m",
    ]

    # Macro groups
    realgdp_group = ["RealGDP", "RealGDP_lag", "RealGDP_mom", "RealGDP_yoy"]

    unemp_group = [
        "UnemploymentRate",
        "UnRate_mom",
        "UnRate_3m",
        "UnRate_yoy",
    ]

    permits_group = [
        "Permits",
        "Permits_Lag_r3m",
        "Permits_Lag_ann_r3m",
        "PermitsLag_yoy",
    ]

    cpi_group = [
        "CPI",
        "CPI_Lag_r3m",
        "CPI_Lag_ann_r3m",
        "CPILag_yoy",
    ]

    corecpi_group = [
        "CoreCPI",
        "CoreCPI_Lag_r3m",
        "CoreCPI_Lag_ann_r3m",
        "CoreCPILag_yoy",
    ]

    indprod_group = [
        "IndustrialProd",
        "IndustrialProd_Lag_r3m",
        "IndustrialProd_Lag_ann_r3m",
        "IndustrialProdLag_yoy",
    ]

    realretail_group = [
        "RetailTrade",
        "RetailTrade_Lag_r3m",
        "RetailTrade_Lag_ann_r3m",
        "RetailTrade_Lag_yoy",
    ]

    # Macro group: lagged + 3m rolling (for regime features)
    macro_3m_1lag = [
        "RealGDP_lag",
        "UnRate_3m",
        "Permits_Lag_r3m",
        "IndustrialProd_Lag_r3m",
        "CPI_Lag_r3m",
        "CoreCPI_Lag_r3m",
        "RetailTrade_Lag_r3m",
    ]

    # Rate level group
    rate_group = [
        "Mort30Y",
        "UST10Y",
        "UST2Y",
        "UST3M",
        "CorpBAA",
        "CorpAAA",
        "FedFundsRate",
    ]

    # Rate deltas
    mort30_group = ["Mort30Y_Delta1m", "Mort30Y_Delta3m"]
    ust10y_group = ["UST10Y_Delta1m", "UST10Y_Delta3m"]
    ust2y_group = ["UST2Y_Delta1m", "UST2Y_Delta3m"]
    ust3m_group = ["UST3M_Delta1m", "UST3M_Delta3m"]
    corpbaa_group = ["CorpBAA_Delta1m", "CorpBAA_Delta3m"]
    corpaaa_group = ["CorpAAA_Delta1m", "CorpAAA_Delta3m"]
    ff_group = ["FedFundsRate_Delta1m", "FedFundsRate_Delta3m"]

    # Slopes
    slope_10y_2y_group = [
        "Slope_10Y_2Y",
        "Slope_10Y_2Y_Delta1m",
        "Slope_10Y_2Y_Delta3m",
    ]
    slope_10y_3m_group = [
        "Slope_10Y_3M",
        "Slope_10Y_3M_Delta1m",
        "Slope_10Y_3M_Delta3m",
    ]
    slope_10y_ff_group = [
        "Slope_10Y_FF",
        "Slope_10Y_FF_Delta1m",
        "Slope_10Y_FF_Delta3m",
    ]

    # Credit spreads
    aaa_minus_10y_group = [
        "AAA_minus_10Y",
        "AAA_minus_10Y_Delta1m",
        "AAA_minus_10Y_Delta3m",
    ]
    baa_minus_10y_group = [
        "BAA_minus_10Y",
        "BAA_minus_10Y_Delta1m",
        "BAA_minus_10Y_Delta3m",
    ]
    baa_minus_aaa_group = [
        "BAA_minus_AAA",
        "BAA_minus_AAA_Delta1m",
        "BAA_minus_AAA_Delta3m",
    ]

    GROUPS = [
        spy_group,
        vbmfx_group,
        realgdp_group,
        unemp_group,
        permits_group,
        cpi_group,
        corecpi_group,
        indprod_group,
        realretail_group,
        macro_3m_1lag,
        rate_group,
        mort30_group,
        ust10y_group,
        ust2y_group,
        ust3m_group,
        corpbaa_group,
        corpaaa_group,
        ff_group,
        slope_10y_2y_group,
        slope_10y_3m_group,
        slope_10y_ff_group,
        aaa_minus_10y_group,
        baa_minus_10y_group,
        baa_minus_aaa_group,
    ]

    result = [col for group in GROUPS for col in group]
    return result


def stock_price(stock_name,single_stock):
    """Provide the stock name and the dataframe(single stock)"""
    print(f'{stock_name} Price in April 1993:', '$',round(single_stock.iloc[0],2))
    print(f'{stock_name} Price in September 2025:', '$',round(single_stock.iloc[-1],2))
    price_change = round((single_stock.iloc[-1] - single_stock.iloc[0]) / single_stock.iloc[0])*100
    print (f'Percent Change from April 1993 to September 2025:  {price_change}%')

def bucket_indicator(row):
    return row['SPY_Sharpe'] - row['VBMFX_Sharpe']

def assign_bucket(row):
    diff = row['SPY_Sharpe'] - row['VBMFX_Sharpe']
    if diff > 0.7: return "80/20"
    elif diff > 0.4: return "70/30"
    elif diff > 0.0: return "60/40"
    else: return "50/50"
