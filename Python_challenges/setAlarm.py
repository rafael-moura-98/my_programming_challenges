from datetime import datetime
import time

def setAlarm(wake_at, file_to_play, message):
    now = datetime.now()

    wake_at_time = wake_at.split(sep=":")
    
    current_time = now.time()
    print(wake_at_time[0])
    print(wake_at_time[1])
    print(current_time.hour)
    print(current_time.minute)
    
    if int(wake_at_time[0]) == current_time.hour:
        print(message)
    

setAlarm("9:26", 0, "Bom dia")








