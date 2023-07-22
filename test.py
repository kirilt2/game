import pytz
from datetime import datetime

def get_israel_time():
    # Set the timezone for Israel (IST, UTC+3)
    israel_tz = pytz.timezone('Asia/Jerusalem')

    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Convert the UTC time to Israel time
    israel_now = utc_now.replace(tzinfo=pytz.utc).astimezone(israel_tz)

    return israel_now

if __name__ == "__main__":
    israel_time = get_israel_time()
    print("Current time in Israel:", israel_time.strftime("%Y-%m-%d %H:%M:%S"))
