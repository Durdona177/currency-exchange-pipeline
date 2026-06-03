USE CurrencyExchangeDB;
GO

CREATE TABLE raw_rates
(
    id INT IDENTITY(1,1) PRIMARY KEY,
    fetch_date DATE NOT NULL,
    base_currency VARCHAR(10) NOT NULL,
    raw_json NVARCHAR(MAX) NOT NULL
);
GO

CREATE TABLE cleaned_rates
(
    rate_date DATE NOT NULL,
    base_currency VARCHAR(10) NOT NULL,
    target_currency VARCHAR(10) NOT NULL,
    exchange_rate DECIMAL(18,6) NOT NULL
);
GO

CREATE TABLE aggregated_rates
(
    rate_date DATE NOT NULL,
    target_currency VARCHAR(10) NOT NULL,
    exchange_rate DECIMAL(18,6) NOT NULL,
    rate_change_pct DECIMAL(18,4),
    avg_7_day DECIMAL(18,6)
);
GO