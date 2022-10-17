import pywhatkit
pywhatkit.sendwhatmsg(phone_no="+911234567891", message="Your Message", time_hour=17, time_min=0, wait_time=20, tab_close=True, close_time=10)
# wait_time - No of seconds to wait after running command
# tab_close - Closes the tab once the message is sent
# close_time - Time to close tab in seconds

# Send message to groups
pywhatkit.sendwhatmsg_to_group(group_id="AB123CDEFGHijklmn", "Your Message", 23, 0, 10, True, 10) # other parameters are same as the first one

# To find how to get group ID--> Swipe

# To send instant message
pywhatkit.sendwhatmsg_instantly("+911234567891", "Your message", 15, True, 4)

# send an image/gif
pywhatkit.sendwhats_image("+911234567891", "C:\\Image.png", "Question-1", 10, True, 5)
