from datetime import datetime

time = datetime.now()
time_log = time.strftime("%d-%m-%Y %H:%M:%S")

print(time_log)