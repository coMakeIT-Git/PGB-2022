#Calculate the date 4 months from the current date 
import datetime
print((datetime.date.today() + datetime.timedelta(4*365/12)).isoformat())