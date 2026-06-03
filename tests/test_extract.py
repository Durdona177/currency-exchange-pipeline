from pipeline.extract import get_latest_rates


def test_api_response():
    data = get_latest_rates()

    assert "base" in data
    assert "date" in data
    assert "rates" in data