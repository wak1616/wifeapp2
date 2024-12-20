from app import refresh_all_data
import schedule
import time
import pytz
from datetime import datetime, timedelta

def job():
    print(f"Running scheduled refresh at {datetime.now(pytz.timezone('America/New_York'))}")
    refresh_all_data()

# Calculate time until next midnight EST
def get_seconds_until_midnight():
    eastern = pytz.timezone('America/New_York')
    now = datetime.now(eastern)
    midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    return (midnight - now).seconds

# Schedule the job
schedule.every().day.at("00:00").do(job)

if __name__ == "__main__":
    # Run immediately if we're starting up after midnight
    if should_refresh_cache():
        job()
    
    while True:
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds
 