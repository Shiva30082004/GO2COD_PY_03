'''
GO2COD PYTHON PROGRAMMING INTERNSHIP
TASK 03 : ALARM CLOCK
NAME: SHIV BHAVSAR

This program will use the datetime and time module from
python library to set an alarm for specific time.

'''


import datetime
import time
import winsound

# Function that sets an alarm and plays a sound when the alarm time is reached.
def set_alarm(alarm_time):
    
    print("Alarm is set for",alarm_time)
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        # if current time matches the alarm time print message and play a beep sound for 5 seconds at 440 Hz
        if current_time == alarm_time:
            print("Wake up!")
            winsound.Beep(440, 5000)  
            break
        time.sleep(1)

def main():
    # prompt the user to enter alarm time
    alarm_time = input("Enter the alarm time in 24-Hours format (HH:MM:SS): ")
    
    # exception handling for invalid time format
    try:
        time.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
        
    except ValueError:
        print("Invalid Time Format. Please Enter Time as HH:MM:SS.")
        
main()   
