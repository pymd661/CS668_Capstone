# Capstone: Dynamic Rebalancing and Allocation for Index Portfolios

## Abstract
This project explores whether macroeconomic features can be used to identify economic regimes and inform dynamic stock–bond allocation. 

## Parts of Capstone
(1) fetches market and macro data
(2) cleans and transforms features
(3) performs exploratory analysis
(4) trains a regression model to predict stock weight targets across predefined allocations (80/20, 70/30, 60/40, 50/50). 

## Key Results (Sep 2015–Sep 2025)
- **Dynamic Regression Portfolio:** ~10.8% annualized return, ~10.5% annualized volatility, max drawdown ~-22%
- **Static 60/40 (monthly rebalance):** ~10.0% annualized return, ~10.1% annualized volatility, max drawdown ~-20%
- **60/40 Buy & Hold:** ~11.4% annualized return, ~11.5% annualized volatility, max drawdown ~-21.8%
- **Static 100% Stock:** ~15.4% annualized return, ~15.3% annualized volatility, max drawdown ~-23.9%

> Note: Results are period-specific and do not yet demonstrate a consistent advantage over simpler benchmarks.

---

## Repository Structure (Quick Links)

### 1) Code
Main working directory for notebooks/scripts used throughout the project:  
- **[`/code`](./code)**

Within `/code`, major sections:

- **Data Cleansing / Transformation**  
  Feature engineering, alignment, lagging (to simulate reporting delay), resampling, and final modeling dataset creation.  
  - **[`/code/data_cleanse`](./code/data_cleanse_feature_engineering)**

- **Exploratory Data Analysis (EDA)**  
  Visualizations, distribution checks, correlation analysis, regime inspection, and sanity checks.  
  - **[`/code/eda`](./code/eda)**

- **Data Fetching**  
  Scripts/notebooks to pull raw inputs (e.g., prices, returns, macro data) and store locally for downstream steps.  
  - **[`/code/fetch_data`](./code/fetch_data)**
 
- **Train and Test**  
  Scripts to perform pre-processing and testing model
  - **[`/code/experimentation`](./code/preprocessing_experimentation)**
---

## Steps
1. Run **fetch_data** to pull/update raw datasets.
2. Run **data_cleanse_feature_engineering** to generate the cleaned, monthly modeling dataset.
3. Use **eda** to validate features and inspect relationships.
4. Use **preprocessing_experimentation** to train and test model.

## Notes / Limitations
- Results depend on the chosen sample period and feature set.
- Further work: walk-forward validation, transaction costs/turnover, alternative models, and robustness across decades.

## Contact
If you have questions or want to discuss the methodology, feel free to reach out.
