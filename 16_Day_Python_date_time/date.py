from datetime import datetime, timedelta

# Get the current day, month, year, hour, minute, and timestamp
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

# Format the current date in the specified format
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# Convert the string "Today is 5 December, 2019" to a datetime object
time_string = "5 December, 2019"
time_converted = datetime.strptime(time_string, "%d %B, %Y")

# Calculate the time difference between now and New Year
new_year = datetime(current_year + 1, 1, 1)
time_until_new_year = new_year - now

# Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch