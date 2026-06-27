import polars as pl


def price_features():
    df = pl.read_parquet(
        "/home/youssef/Projects/walmart-stores/data/processed/df_merged.parquet",
        columns=["item_store_id", "day_number", "sell_price", "store_id"]
    )

    df = df.sort(["item_store_id", "day_number"])

    df = df.with_columns([
        (pl.col("sell_price") - pl.col("sell_price").shift(1)).over("item_store_id").alias("price_change"),
        pl.col("sell_price").shift(1).rolling_mean(4).over("item_store_id").alias("price_rolling_mean_4w"),
        (pl.col("sell_price") / pl.col("sell_price").mean().over("store_id")).alias("price_relative_to_store"),
    ])

    df =  df.drop(['store_id', 'sell_price'])

    print(f"Price Features Shape: {df.shape}")
    print(f"Memory Usage: {df.estimated_size('mb'):.1f} MB")

    output_path = "/home/youssef/Projects/walmart-stores/data/processed/price_features.parquet"
    df.write_parquet(output_path)
    print("price_features.py: Done")


if __name__ == "__main__":
    price_features()