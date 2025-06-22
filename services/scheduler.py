from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

# Example of a scheduled job
@scheduler.scheduled_job('interval', minutes=1)
async def scheduled_task():
    print("This job runs every minute.")

def start_scheduler():
    scheduler.start()