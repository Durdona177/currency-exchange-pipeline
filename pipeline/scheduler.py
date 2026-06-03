from apscheduler.schedulers.blocking import BlockingScheduler

from load_bronze import load_to_bronze
from extract import get_latest_rates
from transform_silver import transform_to_silver
from transform_gold import build_gold


def run_pipeline():

    print("Pipeline started")

    data = get_latest_rates()

    load_to_bronze(data)

    transform_to_silver()

    build_gold()

    print("Pipeline completed")


scheduler = BlockingScheduler(
    timezone="Asia/Tashkent"
)

scheduler.add_job(
    run_pipeline,
    trigger="cron",
    hour=8,
    minute=0
)



print(
    "Scheduler started. Waiting for 08:00 Asia/Tashkent..."
)

scheduler.start()