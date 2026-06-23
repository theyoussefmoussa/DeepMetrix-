import pandas as pd
import numpy as np

def time_features(): 
    time_cols = ['date', 'day_number', 'walmart_year_week', 'month_name', 'weekday']
    df_time = pd.read_parquet('/home/youssef/Projects/walmart-stores/data/processed/df_merged.parquet', columns=time_cols)

    # Extract Date Features 
    df_time['year'] = df_time['date'].dt.year
    df_time['month'] = df_time['date'].dt.month
    df_time['week'] = df_time['date'].dt.isocalendar().week.astype("int16") 
    df_time['day'] = df_time['date'].dt.day
    df_time['quarter'] = df_time['date'].dt.quarter
    df_time['is_weekend'] = df_time['date'].dt.dayofweek >= 5 # Monday=0, Sunday=6.
    df_time['is_month_start'] = df_time['date'].dt.is_month_start
    df_time['is_month_end'] = df_time['date'].dt.is_month_end


    # downcast numeric columns
    for col in ['year', 'month', 'day', 'quarter']:
        df_time[col] = df_time[col].astype('int16')

    df_time.drop(columns=['date'], inplace=True)

    # memory usage
    print(f"Time Features Shape: {df_time.shape}")
    print(f"Memory Usage: {df_time.memory_usage(deep=True).sum() / 1e6:.1f} MB")


    # Save Outputs
    output_path = '/home/youssef/Projects/walmart-stores/data/processed/time_features.parquet'
    df_time.to_parquet(output_path, index=False)
    print("time_features.py: Done")
