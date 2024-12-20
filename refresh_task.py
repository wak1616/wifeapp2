from app import refresh_all_data
import pytz
from datetime import datetime

if __name__ == "__main__":
    eastern = pytz.timezone('America/New_York')
    print(f"Starting scheduled refresh at {datetime.now(eastern)}")
    refresh_all_data()
    print(f"Completed scheduled refresh at {datetime.now(eastern)}")
