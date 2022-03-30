#Convert string into a datetime object

print("Conversion of string into a datetime object")
import datetime
def convert(input):
    format='%b %d %Y %I:%M%p' #format for dates and months years
    date_time=datetime.datetime.strptime(input,format)
    return date_time
print(convert('Jun 20 1966 05:20AM'))

print("the date 4 months from the current date :")
print((datetime.date.today() + datetime.timedelta(4*365/12)).isoformat())
