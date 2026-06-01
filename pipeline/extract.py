import requests
from logger_config import setup_logger

logger = setup_logger()


def get_latest_rates(date="latest"):

    url = (
        f"https://api.frankfurter.app/{date}"
        "?from=USD"
        "&to=UZS,RUB,EUR,GBP"
    )

    response = requests.get(url)

    response.raise_for_status()

    logger.info(
        f"Successfully fetched data for {date}"
    )

    return response.json()


if __name__ == "__main__":

    data = get_latest_rates()

    print(data)