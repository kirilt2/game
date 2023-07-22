import datetime
import pytz


def get_israel_time():
    # Get the current UTC time
    utc_time = datetime.datetime.utcnow()

    # Get the Israel time zone
    israel_tz = pytz.timezone('Israel')

    # Convert the UTC time to Israel time
    israel_time = utc_time.astimezone(israel_tz)
    return israel_time

# Get the current time in Israel
current_time_israel = get_israel_time()
print(f"Current time in Israel!@: {current_time_israel.strftime('%Y-%m-%d %H:%M:%S')}")
