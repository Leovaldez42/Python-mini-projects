import time
from plyer import notification      # can be installed by pip install plyer

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink Water",
            message = 'You are really not drinking enough water now a days. Go drink some   without delay.',
            app_icon = "icon.png",
            timeout = 10        # Will stay for 10 seconds.
        )
        time.sleep(6)       # Will remind after one hour.
        
        # In case you want to close the program and the notification should keep coming run the program using pythonw ./main.py ( after going to the folder ).

        ## End ##