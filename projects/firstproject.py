#!/usr/bin/python

from datetime import datetime
import calendar
import time

# current date and time.
currentdate = datetime.now()
print("")
print('The current date is:', currentdate,".\n")

# receive today's date from computer and convert to a number for day of week.
currentdayofweek = currentdate.isoweekday()
print('There are 7 days in a week.  Today is #', currentdayofweek)
print("")

# check to make sure 7 days (0-6) are being received.
while(currentdayofweek < 7):

# date / time library starts with 0 being Sunday.
    if (currentdayofweek == 0):
        print("The day of the week is Sunday\n")
        break # break(s) are in b/c it kept looping.

    elif(currentdayofweek == 1):
        print("The day of the week is Monday\n")
        break

    elif(currentdayofweek == 2):
        print("The day of the week is Tuesday\n")
        break

    elif(currentdayofweek == 3):
        print("The day of the week is Wednesday\n")
        break

    elif(currentdayofweek == 4):
        print("The day of the week is Thursday\n")
        break

    elif(currentdayofweek == 5):
        print("The day of the week is Friday\n")
        break

    elif (currentdayofweek == 6):
        print("The day of the week is Saturday\n")
        break
    
    else:
        print("There is no other day of week\n")
        break

