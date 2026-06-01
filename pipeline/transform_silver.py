import json
import pandas as pd
from sqlalchemy import create_engine


def get_engine():

    connection_string = (
        "mssql+pyodbc://@localhost/CurrencyExchangeDB"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)


def transform_to_silver():

    engine = get_engine()

    query = """
    SELECT *
    FROM raw_rates
    """

    raw_df = pd.read_sql(query, engine)

    rows = []

    for _, row in raw_df.iterrows():

        payload = json.loads(row["raw_json"])

        for currency, rate in payload["rates"].items():

            if rate is None:
                continue

            if float(rate) <= 0:
                continue

            rows.append({
                "rate_date": payload["date"],
                "base_currency": payload["base"],
                "target_currency": currency,
                "exchange_rate": float(rate)
            })

    clean_df = pd.DataFrame(rows)

    clean_df.drop_duplicates(inplace=True)

    clean_df.to_sql(
        "cleaned_rates",
        engine,
        if_exists="append",
        index=False
    )

    print(f"{len(clean_df)} rows loaded into Silver")


if __name__ == "__main__":

    transform_to_silver()