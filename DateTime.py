from datetime import datetime, timedelta
from time import strftime

__author__ = "Ejie Emmanuel Ebuka"


# Date time
# Working with dates, times, deltas and formats

def main():
    # Now
    now = datetime.now()
    utc = datetime.utcnow()
    offset = datetime.utcoffset(now)
    print(f'Now: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {offset}')
    # Time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Micro: {now.microsecond}')
    # Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')
    # Timedelta
    print(f'Next Month: {now + timedelta(days=30) }')
    print(f'Last week: {now + timedelta(weeks=-1) }')
    print(f'10 Hours: {now + timedelta(hours=10) }')
    print(f'50 seconds: {now + timedelta(seconds=50) }')
    print(f'100 Millisecond: {now + timedelta(milliseconds=100) }')
    print(f'30 Microseconds: {now + timedelta(microseconds=30) }')
    # ISO String
    try:
        date = datetime.fromisoformat('2021-12-03 00:00:00.000000')
        print(date)
    except Exception as e:
        print(e.args)
    finally:
        print("Date Time!")

if __name__ == "__main__":
    main()

