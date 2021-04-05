"Play a simple alert at the passed time."

from datetime import datetime
import winsound

def setAlarm(wake_at, message, file_to_play = "beep"):
    wake_at_time = wake_at.split(sep=":")
    
    ringing = False

    while(not ringing):
        now = datetime.now()
        current_time = now.time()

        if int(wake_at_time[0]) == current_time.hour and int(wake_at_time[1]) == current_time.minute:
            print(message)
            if file_to_play == "beep":
                winsound.Beep(500, 1000)
            ringing = True

    
setAlarm("21:50", "Boa noite")








