import time
from win10toast import ToastNotifier

time_to_notify = input("Input Time in 24hr format(HH:MM:SS) to set reminder: ")
notification_message = input("Enter your message: ")
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == time_to_notify:
        print(current_time)
        break

notify = ToastNotifier()
notify.show_toast("Notification",notification_message)
