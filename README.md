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