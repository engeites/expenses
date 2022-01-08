from apscheduler.schedulers.background import BackgroundScheduler

from app.database import Database
from app.utils import sched_task

# Initiate the database here
db = Database()

# Initiate the scheduler to save assets' price every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(func=sched_task, trigger="interval", seconds=300)
