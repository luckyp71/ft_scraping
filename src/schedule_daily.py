from apscheduler.schedulers.blocking import BlockingScheduler
from src.orchestrate import run_pipeline

scheduler = BlockingScheduler()

# Schedule to run every day at 6:00 AM
scheduler.add_job(run_pipeline, 'cron', hour=6, minute=0)

if __name__ == "__main__":
    print("Daily scheduler started...")
    scheduler.start()
