import os
import time

os.system('start cmd')
print("?")
time.sleep(0.1)
os.system('taskkill /f /m cmd.exe')
print("!")
