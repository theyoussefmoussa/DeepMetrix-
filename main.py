from src.data_cleaning.calendar_cleaning import calendar_cleaning
from src.data_cleaning.sales_train_cleaning import sales_train_cleaning
from src.data_cleaning.sell_prices_cleaning import sell_prices_cleaning
from src.data_merging.merge import merge
from utils.formatting import separator
from src.feature_engineering.time_features import time_features
from src.feature_engineering.lag_features import lag_features
from src.feature_engineering.rolling_features import rolling_features
from src.feature_engineering.price_features import price_features
from src.eda.univariate_analysis import univarite_analysis
if __name__ == "__main__":
    separator(title='Calendar Cleaning')
    calendar_cleaning()
    separator(title='Sales Train Cleaning')
    sales_train_cleaning()
    separator(title='Sell Prices Cleaning')
    sell_prices_cleaning()
    separator(title='Merging')
    merge()
    separator(title="Time Features")
    time_features()
    separator(title='Lag Features')
    lag_features()
    separator(title='Rolling Features')
    rolling_features()
    separator(title='Price Features')
    price_features()
    separator("EDA: Univariate Analysis")
    univarite_analysis()