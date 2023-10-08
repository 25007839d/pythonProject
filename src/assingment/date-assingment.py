#1. Python program to get Current Time
from datetime import datetime, date, timedelta

now = datetime.now()
time = now.strftime('%H:%M:%S:%f')
# print(now)
# print(time)


#2. Get Current Date and Time using Python

current_date_tiem = datetime.now()
''' 
to remove milisecond use formate
'''

current_date_tiem1=current_date_tiem.strftime('%d-%m-%Y  %H:%M:%S')

# print(current_date_tiem1)
#3. Python | Find yesterday’s, today’s and tomorrow’s date

yesterday= (datetime.now()-timedelta(1)).strftime('%d-%m-%Y')
'''
to fetxh only date from time stamp use #strftime
'''
tomorrow = (datetime.now()+timedelta(1)).strftime('%d-%m-%Y')
# print(tomorrow)
# print(yesterday)


#4. Python program to convert time from 12 hour to 24 hour format




#5. Python program to find difference between current time and given time

#6. Python Program to Create a Lap Timer
#7. Convert date string to timestamp in Python


string = "20/01/2020"

element = datetime.strptime(string, "%d/%m/%Y")

timestamp = datetime.timestamp(element)
print(timestamp)
print(element)
#8. How to convert timestamp string to datetime object in Python?
#9. Find number of times every day occurs in a Year
