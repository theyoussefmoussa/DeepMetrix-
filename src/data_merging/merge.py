import pandas as pd
import os

def merge(): 
    # Load Data
    calendar = pd.read_parquet('/home/youssef/Projects/walmart-stores/data/processed/calendar_cleaned.parquet')
    sales = pd.read_parquet('/home/youssef/Projects/walmart-stores/data/processed/sales_train_cleaned.parquet')
    price = pd.read_parquet('/home/youssef/Projects/walmart-stores/data/processed/sell_prices_cleaning.parquet')

    # Merging Sales days
    sales_long = pd.melt(
    sales,
    id_vars=["item_store_id", "item_id", "dept_id", "cat_id", "store_id", "state_id"],
    var_name="day_number",
    value_name="sales"
        )
    sales_long["day_number"] = sales_long["day_number"].astype("int16")

    # merge sales with calendar 
    sales_calendar = sales_long.merge(
    calendar, 
    on='day_number',
    how='left'
    )

    # merge sales_calendar with price
    df_merged = sales_calendar.merge(
    price,
    on=["store_id", "item_id", "walmart_year_week"],
    how="left"
    )


    # Save Output
    output_path = os.path.join('/home/youssef/Projects/walmart-stores', 'data', 'processed', 'df_merged.parquet')
    df_merged.to_parquet(output_path, engine='pyarrow', index=False)
    print("merge.py: Done")
    print(f"Dataset Merged: {df_merged.shape[0]:,} rows, {df_merged.shape[1]} columns")
    print(f"Missing Valuse Count After Merging: {df_merged["sell_price"].isnull().sum()}")
