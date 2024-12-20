from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=0, minute=0, timezone='America/New_York')
def scheduled_refresh():
    """Trigger a cache refresh at midnight EST"""
    # Get the app's URL from environment variable
    app_url = os.environ.get('APP_URL', 'https://your-app-name.herokuapp.com')
    
    # Make a request to trigger cache refresh
    requests.get(f"{app_url}/")

sched.start() 