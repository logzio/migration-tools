from datetime import datetime
from time import sleep
from time import time

import progressbar
from datadog import initialize, api

api_key = input("Enter your api key:")
application_key = input("enter your application key:")
options = {
    'api_key': api_key,
    'app_key': application_key
}

initialize(**options)

# Taking the last 24hours
from_time = int(time()) - 3600
end = int(time())  # Specify the time period over which you want to fetch the data in seconds
start = end - 3600

result = api.Metric.list(from_time)
metric_count = len(result['metrics'])
i = 0

print(datetime.now())
print("collecting data please wait. Its may take some time...")
bar = progressbar.ProgressBar(maxval=metric_count,
                              widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
bar.update(i + 1)
total_dpm = 0
f = open("dd.csv", "a")
for metric_name in (result['metrics']):
    query = metric_name + '{*}'
    results = api.Metric.query(start=start, end=end, query=query)
    count = len(results['series'][0]['pointlist'])
    time_frame = results['series'][0]['interval']
    total_dpm = total_dpm + (count / time_frame)
    f.write(str(metric_name) + ";" + str(time_frame) + ";" + str(count))
    f.write("\n")
    bar.update(i + 1)
    i = i + 1
    sleep(3)
f.write("total DPM: " + str(total_dpm))
f.close()
# print(result)

print(datetime.now())
