from src.data_cleaning.calendar_cleaning import calendar_cleaning
from src.data_cleaning.sales_train_cleaning import sales_train_cleaning
from src.data_cleaning.sell_prices_cleaning import sell_prices_cleaning
if __name__ == "__main__":
    calendar_cleaning()
    sales_train_cleaning()
    sell_prices_cleaning()