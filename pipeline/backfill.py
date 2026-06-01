import pandas as pd
from sqlalchemy import create_engine

from datetime import datetime, timedelta

from extract import get_latest_rates
from load_bronze import load_to_bronze


def run_backfill(days=30):

    end_date = datetime.today()

    start_date = end_date - timedelta(days=days)

    current_date = start_date

    while current_date <= end_date:

        date_string = current_date.strftime("%Y-%m-%d")

        try:

            data = get_latest_rates(date_string)

            load_to_bronze(data)

            print(f"Loaded {date_string}")

        except Exception as e:

            print(f"Skipped {date_string}: {e}")

        current_date += timedelta(days=1)


if __name__ == "__main__":

    run_backfill(30)

    