#Author Name: Muhammad Fiaz
#Url: https://github.com/muhammad-fiaz
#import time module 
import time 
  
  
# localtime() method used to 
# get the object containing 
# the local time. 
Time = time.localtime() 
  
# strftime() method used to 
# create a string representing 
# the current time. 
currentTime = time.strftime("%H:%M:%S", Time) 
print(currentTime) 
