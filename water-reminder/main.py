import time
from plyer import notification      # can be installed by pip install plyer
import argparse

def create_arg_parser():
    parser = argparse.ArgumentParser(description='Simple Application to remind you to drink water after specific period of time.')
    parser.add_argument("-t", "--timelimit", type=str, required=False, help="Enter Timeinterval after which you want notification")
    return parser

parser = create_arg_parser()
args = parser.parse_args()

time_interval = 6
if args.timelimit:
    time_interval = args.timelimit

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink Water",
            message = 'You are really not drinking enough water now a days. Go drink some   without delay.',
            app_icon = "icon.png",
            timeout = 10        # Will stay for 10 seconds.
        )
        time.sleep(time_interval)       # Will remind after one hour.
        
        # In case you want to close the program and the notification should keep coming run the program using pythonw ./main.py ( after going to the folder ).

        ## End ##