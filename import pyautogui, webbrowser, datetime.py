import pyautogui, webbrowser, datetime
from time import sleep

# default variables
flag = 1

# ids person target
id = '100053577584692'

# hour to be sended
hour_to_send = '23:18'

def send():
    # open messenger
    webbrowser.open(f'https://www.messenger.com/t/{id}')

    # wait 5 seconds
    sleep(5)

    # send message
    pyautogui.typewrite("TE AMO")
    pyautogui.press("enter")
    return 0

# cycle
while flag:
    # hour actual
    hour = datetime.datetime.now().strftime('%I:%M')
    if hour == hour_to_send:
        # send message and finish the program
        flag = send()
