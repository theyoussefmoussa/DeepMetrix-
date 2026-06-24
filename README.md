# Walmart M5 Sales Forecasting

> **DEPI Data Science Track | Team: DeepMetrix-**
> Predicting daily unit sales for 3,049 Walmart products across 10 stores using the [M5 Forecasting Kaggle dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy).

---

## Team

| Name | LinkedIn |
|------|----------|
| Youssef Moussa | [theyoussefmoussa](https://www.linkedin.com/in/theyoussefmoussa) |
| Malak Abdallah | [malak-abdallah](https://www.linkedin.com/in/malak-abdallah/) |
| Zyad Ashraf | [zyad-ashraff](https://www.linkedin.com/in/zyad-ashraff/) |
| Hamza Ahmed | [hamzaahmedamin](https://www.linkedin.com/in/hamzaahmedamin/) |
| Rahma Essam | [rahma-essam](https://www.linkedin.com/in/rahma-essam/) |
| Sara Mostafa | [sara--mostafa](https://www.linkedin.com/in/sara--mostafa/) |

---

---
## Current Milestone — Feature Engineering
| Step | Status |
|------|--------|
| Data Collection | Done |
| Calendar Understanding | Done |
| Sales Train Understanding | Done |
| Sell Prices Understanding | Done |
| Calendar Cleaning | Done |
| Sales Train Cleaning | Done |
| Sell Prices Cleaning | Done |
| Merge & Validate | Done |
| Feature Engineering | In Progress |
| EDA | Upcoming |
| Modeling | Upcoming |
| Deployment | Upcoming |
---
## Project Structure
```
GRADUATION_PROJECT/
├── data/
│   ├── raw/
│   │   ├── calendar.csv
│   │   ├── sales_train_evaluation.csv
│   │   └── sell_prices.csv
│   └── processed/
│       ├── calendar_cleaned.parquet
│       ├── sales_train_cleaned.parquet
│       ├── sell_prices_cleaned.parquet
│       ├── df_merged.parquet
│       ├── time_features.parquet
│       └── lag_features.parquet
│       └── rolling_features.parquet
│
├── notebooks/
│   ├── data_understanding/
│   │   ├── calendar_understanding.ipynb
│   │   ├── sales_train_understanding.ipynb
│   │   └── sell_prices_understanding.ipynb
│   ├── data_cleaning/
│   │   ├── calendar_cleaning.ipynb
│   │   ├── sales_train_cleaning.ipynb
│   │   └── sell_prices_cleaning.ipynb
│   ├── data_merging/
│   │   └── merge.ipynb
│   └── feature_engineering/
│       └── lag_features.ipynb
│       └── time_features.ipynb
│       └── rolling_features.ipynb
│
├── src/
│   ├── data_cleaning/
│   │   ├── __init__.py
│   │   ├── calendar_cleaning.py
│   │   ├── sales_train_cleaning.py
│   │   └── sell_prices_cleaning.py
│   ├── data_merging/
│   │   ├── __init__.py
│   │   └── merge.py
│   └── feature_engineering/
│       ├── __init__.py
│       ├── time_features.py
│       └── lag_features.py
│       └── rolling_features.py
│
├── utils/
│   ├── __init__.py
│   ├── cleaning_utils.py
│   └── formatting.py
│
├── docs/
│   ├── cleaning_docs/
│   │   ├── calendar_cleaning.md
│   │   ├── sales_train_cleaning.md
│   │   └── sell_prices_cleaning.md
│   ├── data_merging/
│   │   └── merge.md
│   ├── feature_engineering_docs/
│   │   └── time_features.md
|   |   └── lag_features.md
│       └── rolling_features.md
│   ├── columns.md
│   └── insights.md
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```
---
## Datasets
| File | Rows | Cols | Description |
|------|------|------|-------------|
| `calendar.csv` | 1,969 | 14 | Daily calendar with events and SNAP flags |
| `sales_train_evaluation.csv` | 30,490 | 1,947 | Unit sales per item per day (wide format) |
| `sell_prices.csv` | ~6.8M | 4 | Weekly sell price per item per store |
| `df_merged.parquet` | ~59.2M | 18 | Merged long-format dataset ready for feature engineering |
| `time_features.parquet` | ~59.2M | 9 | `day_number`, `walmart_year_week`, `month_name`, `weekday`, `year`, `month`, `week`, `day`, `quarter`, `is_weekend`, `is_month_start`, `is_month_end` |
| `lag_features.parquet` | ~59.2M | 4 | `item_store_id`, `day_number`, `sales`, `lag_7`, `lag_28` |
| `rolling_features.parquet` | ~59.2M | 6 | `item_store_id`, `day_number`, `sales`, `rolling_mean_7`, `rolling_mean_28`, `rolling_std_7` |
## Setup & Usage

```bash
# 1. Clone the repo
git clone https://github.com/theyoussefmoussa/DeepMetrix-.git
cd DeepMetrix-

# 2. Install dependencies
pip install -r requirements.txt
```

---

## Dependencies

```
pandas>=2.0
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
python-dotenv==1.2.2
pyarrow>=14.0
polars>=1.42    
```

---

## Dataset Source

Kaggle — [M5 Forecasting - Accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy)

---

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/theyoussefmoussa)
[![X](https://img.shields.io/badge/X-follow-black?style=for-the-badge&logo=x)](https://x.com/theyosefmusa)