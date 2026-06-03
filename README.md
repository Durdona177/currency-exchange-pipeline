# Currency Exchange Data Pipeline

# Currency Exchange Data Pipeline

## Project Overview

This project implements a Medallion Architecture data pipeline for currency exchange rates.

The pipeline extracts exchange rate data from the Frankfurt Exchange Rate API, stores raw data in a Bronze layer, transforms and cleans data in a Silver layer, and generates analytics in a Gold layer.

---

## Architecture

### Bronze Layer
Stores raw API responses as JSON.

Table:
- raw_rates

Features:
- Raw API storage
- Incremental loading
- Duplicate prevention

### Silver Layer
Transforms and cleans exchange rate data.

Table:
- cleaned_rates

Features:
- JSON parsing
- Data type enforcement
- Invalid value filtering
- Deduplication

### Gold Layer
Stores aggregated analytics.

Table:
- aggregated_rates

Features:
- Exchange rate trend analysis
- Percentage change calculation
- 7-day moving average

---

## Technologies Used

- Python
- SQL Server
- SQLAlchemy
- Pandas
- APScheduler
- Pytest
- Git/GitHub

---

## Data Source

Frankfurter API

https://www.frankfurter.app

Currencies processed:

- USD
- EUR
- GBP
- RUB
- UZS

---

## Database Schema

### Bronze

```sql
raw_rates
```

### Silver

```sql
cleaned_rates
```

### Gold

```sql
aggregated_rates
```

---

## Project Structure

```text
currency-exchange-pipeline/
│
├── pipeline/
│   ├── extract.py
│   ├── load_bronze.py
│   ├── transform_silver.py
│   ├── transform_gold.py
│   ├── scheduler.py
│   ├── backfill.py
│   └── logger_config.py
│
├── sql/
│   └── schema.sql
│
├── tests/
│   └── test_extract.py
│
├── logs/
│   └── pipeline.log
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Run:

```sql
sql/schema.sql
```

inside SQL Server Management Studio.

---

## Running the Pipeline

### Extract and Load Bronze

```bash
python -m pipeline.load_bronze
```

### Transform Silver

```bash
python -m pipeline.transform_silver
```

### Build Gold Layer

```bash
python -m pipeline.transform_gold
```

---

## Scheduler

Run scheduled pipeline:

```bash
python -m pipeline.scheduler
```

The scheduler automatically executes the pipeline daily.

---

## Backfill

Load historical data:

```bash
python -m pipeline.backfill
```

---

## Testing

Run tests:

```bash
pytest
```

Current test coverage includes:

- API response validation

---

## Logging

Pipeline activity is logged to:

```text
logs/pipeline.log
```

---

## Assumptions

- SQL Server is running locally.
- ODBC Driver 17 for SQL Server is installed.
- Internet access is available for API requests.
- Currency rates are loaded once per day.

---

## Author

Durdona