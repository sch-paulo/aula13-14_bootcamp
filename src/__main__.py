import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource
from lib.classes.JsonSource import JsonSource

# Function to check new files
def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Scheduling the execution of the function check_for_new_files() every second
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()

# Runs the main loop
while True:
    schedule.run_pending()
    # time.sleep(0.5) # Wait one second so the loop does not consume too much processing
