import json

from sqlalchemy import create_engine
from pipeline.extract import get_latest_rates
from pipeline.logger_config import setup_logger


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

    check_query = """
    SELECT COUNT(*)
    FROM raw_rates
    WHERE fetch_date = ?
      AND base_currency = ?
    """

    insert_query = """
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
            check_query,
            (
                data["date"],
                data["base"]
            )
        )

        existing_count = cursor.fetchone()[0]

        if existing_count > 0:

            logger.warning(
                f"Data already exists for {data['date']}"
            )

            print(
                f"Skipped duplicate load for {data['date']}"
            )

            return

        cursor.execute(
            insert_query,
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