import pandas as pd
from sqlalchemy import create_engine


def get_engine():

    connection_string = (
        "mssql+pyodbc://@localhost/CurrencyExchangeDB"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)


def build_gold():

    engine = get_engine()

    query = """
    SELECT
        rate_date,
        target_currency,
        exchange_rate
    FROM cleaned_rates
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        print("No data found")
        return

    df["rate_date"] = pd.to_datetime(df["rate_date"])

    df = df.sort_values(
        ["target_currency", "rate_date"]
    )

    df["previous_rate"] = (
        df.groupby("target_currency")
        ["exchange_rate"]
        .shift(1)
    )

    df["rate_change_pct"] = (
        (
            df["exchange_rate"]
            - df["previous_rate"]
        )
        / df["previous_rate"]
    ) * 100

    df["avg_7_day"] = (
        df.groupby("target_currency")
        ["exchange_rate"]
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).mean()
        )
    )

    gold_df = df[
        [
            "rate_date",
            "target_currency",
            "exchange_rate",
            "rate_change_pct",
            "avg_7_day"
        ]
    ]

    gold_df.to_sql(
        "aggregated_rates",
        engine,
        if_exists="replace",
        index=False
    )

    print("Gold layer created")


if __name__ == "__main__":

    build_gold()