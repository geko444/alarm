# alarm
Selenium alarm clock setter for onlineclock.net.

This is a simple script for setting a range of alarms on onlineclock.net in Chrome using the Selenium webdriver. Selenium must be running to use this script.

The script asks for start time, end time and step interval. Times can be entered as either '8:30' or '830' and must be entered in a 24 hour format. Hours can be entered as '8', '800' or '8:00'.

Start? 730
End? 8
Step? 10

The above example will open a new Chrome window, and set alarms for 7:30, 7:40, 7:50 and 8:00 in seperate tabs.
