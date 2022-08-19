import time
from plyer import notification 

while True:
    notification.notify(title='Take a break',
                        message ='Take a break! its been an hour',
                       timeout = 5)  #will show the notif. for 5sec
    time.sleep(3600)  #this will run the alert evry hour