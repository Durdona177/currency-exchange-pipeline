import json

from sqlalchemy import create_engine
from extract import get_latest_rates
from logger_config import setup_logger

logger = setup_logger()


def get_engine():

    connection_string = (
        "mssql+pyodbc://@localhost/CurrencyExchangeDB"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)


def load_to_bronze(data):

    engine = get_engine()

    query = """
    INSERT INTO raw_rates
    (
        fetch_date,
        base_currency,
        raw_json
    )
    VALUES
    (
        ?,
        ?,
        ?
    )
    """

    with engine.raw_connection() as conn:

        cursor = conn.cursor()

        cursor.execute(
            query,
            (
                data["date"],
                data["base"],
                json.dumps(data)
            )
        )

        conn.commit()


    logger.info(
    f"Bronze loaded for {data['date']}"
    )

    print(
        f"Bronze loaded for {data['date']}"
    )


if __name__ == "__main__":

    data = get_latest_rates()

    load_to_bronze(data)