from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current Date: ", current_date)
print("Five days: ", five_days_ago)

print(" ")

from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
today = current_date 
tommorrow = current_date + timedelta(days=1)
print("Yerterday: ", yesterday)
print("Today: ", today)
print("Tommorrow: ", tommorrow)

print(" ")

from date import datetime
current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Datetime with microsecond: ", current_datetime)
print("Datetime without microsecond: ", datetime_without_microseconds)

print(" ")

from datetime import datetime
date1 = datetime(2025, 2, 9, 12, 0, 0 )
date2 = datetime(2025, 2, 10, 12, 0 , 0)
time_dif = date2 - date1
seconds_differeence = time_dif.total_seconds()
print("The difference is: ", seconds_differeence)


