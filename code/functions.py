# column groups

def column_order():
    # index fund groups
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
    # macro_groups
    realgdp_group = ["RealGDP", "RealGDP_3m"]
    unemp_group = ["UnemploymentRate_r3m", "UnemploymentRate_ann_r3m"]
    permits_group = ["Permits", "Permits_1m_r3m", "Permits_1m_ann_r3m", "Permits_1m_yoy"]
    cpi_group = ["CPI", "CPI_1m_r3m", "CPI_1m_ann_r3m", "CPI_1m_yoy"]
    corecpi_group = ["CoreCPI", "CoreCPI_1m_r3m", "CoreCPI_1m_ann_r3m", "CoreCPI_1m_yoy"]
    indprod_group = ["IndustrialProd", "IndustrialProd_1m_r3m", "IndustrialProd_1m_ann_r3m", "IndustrialProd_1m_yoy"]
    realretail_group = ["RealRetail", "RealRetail_1m_r3m", "RealRetail_1m_ann_r3m", "RealRetail_1m_yoy"]

    # rates_group
    rate_group = ['Mort30Y', 'UST10Y', 'UST2Y', 'UST3M','CorpBAA', 'CorpAAA','FedFundsRate'] # 'TIPS10Y' removed

    mort30_group = ["Mort30Y_Delta1m", "Mort30Y_Delta3m"]
    ust10y_group = ["UST10Y_Delta1m", "UST10Y_Delta3m"]
    ust2y_group  = ["UST2Y_Delta1m", "UST2Y_Delta3m"]
    ust3m_group  = ["UST3M_Delta1m", "UST3M_Delta3m"]
    # tips10y_group = ["TIPS10Y_Delta1m", "TIPS10Y_Delta3m"]
    corpbaa_group = ["CorpBAA_Delta1m", "CorpBAA_Delta3m"]
    corpaaa_group = ["CorpAAA_Delta1m", "CorpAAA_Delta3m"]
    ff_group = ["FedFundsRate_Delta1m", "FedFundsRate_Delta3m"]

    slope_10y_2y_group = ["Slope_10Y_2Y", "Slope_10Y_2Y_Delta1m", "Slope_10Y_2Y_Delta3m"]
    slope_10y_3m_group = ["Slope_10Y_3M", "Slope_10Y_3M_Delta1m", "Slope_10Y_3M_Delta3m"]
    slope_10y_ff_group = ["Slope_10Y_FF", "Slope_10Y_FF_Delta1m", "Slope_10Y_FF_Delta3m"]

    aaa_minus_10y_group = ["AAA_minus_10Y", "AAA_minus_10Y_Delta1m", "AAA_minus_10Y_Delta3m"]
    baa_minus_10y_group = ["BAA_minus_10Y", "BAA_minus_10Y_Delta1m", "BAA_minus_10Y_Delta3m"]
    baa_minus_aaa_group = ["BAA_minus_AAA", "BAA_minus_AAA_Delta1m", "BAA_minus_AAA_Delta3m"]

    # list of the groups
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

    result = [f for l in GROUPS for f in l]
    return result
