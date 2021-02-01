import os

is_connected = (os.system('ping google.com') == 0)

print(is_connected)
