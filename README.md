# Currency Exchange Data Pipeline

This project implements a Medallion Architecture pipeline:

- Bronze Layer (Raw API Data)
- Silver Layer (Cleaned Exchange Rates)
- Gold Layer (Aggregated Analytics)

Data Source:
Frankfurter API

Currencies:
USD, UZS, RUB, EUR, GBP

Technology:
- Python
- SQL Server
- SQLAlchemy
- Pandas
- APScheduler

## Architecture

### Bronze Layer
- Stores raw Frankfurter API responses
- Immutable audit log
- Data stored in raw_rates table

### Silver Layer
- Parses JSON data
- Validates exchange rates
- Removes invalid records
- Stores clean data in cleaned_rates table

### Gold Layer
- Creates business-ready analytical data
- Calculates day-over-day percentage change
- Calculates 7-day rolling average
- Stores results in aggregated_rates table

## Technologies

- Python
- SQL Server
- SQLAlchemy
- Pandas
- Requests
- APScheduler
- Pytest

## Project Structure

```text
currency-exchange-pipeline/
│
├── pipeline/
│   ├── extract.py
│   ├── load_bronze.py
│   ├── transform_silver.py
│   ├── transform_gold.py
│   ├── backfill.py
│   ├── scheduler.py
│
├── sql/
│   └── schema.sql
│
├── tests/
│   └── test_extract.py
│
├── logs/
│
├── requirements.txt
├── .env
└── README.md
```

## Database Setup

1. Open SQL Server Management Studio
2. Run sql/schema.sql
3. Verify tables:

- raw_rates
- cleaned_rates
- dim_currencies
- dim_dates
- aggregated_rates

## Running The Pipeline

Load raw data:

```bash
python pipeline/load_bronze.py
```

Create Silver layer:

```bash
python pipeline/transform_silver.py
```

Create Gold layer:

```bash
python pipeline/transform_gold.py
```

## Historical Backfill

```bash
python pipeline/backfill.py
```

Loads historical exchange rate data.

## Scheduler

```bash
python pipeline/scheduler.py
```

Runs automatically every day at 08:00 Asia/Tashkent.

## Testing

```bash
python -m pytest
```

Current Result:

```text
1 passed
```

## Assumptions

- USD is the default base currency
- No intraday updates
- Bronze layer is immutable
- Frankfurter API is the source of truth

## Author

Durdona