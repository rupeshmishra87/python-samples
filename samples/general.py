import sys
import os
import datetime
import time

"""os module has functions to determine the information about the current runtime environment"""
print("#### Environment specific information #####")
print("Current Directory : " + os.getcwd())
print("Environment Variables : " + str(os.environ))
print("Current Home : " + os.getenv('HOME'))

"""sys module has functions to determine information related to the system on which the interpreter is running"""
print("#### Platform/System specific information #####")
print("Platform : " + sys.platform)
print("Version : " + sys.version)
print("Version Info : " + str(sys.version_info))

"""Date and Time related functions"""
print("Un-formatted Date : " + str(datetime.date.today()))
print("Formatted Date : " + str(datetime.date.isoformat(datetime.date.today())))
print("Formatted Time : " + str(time.strftime("%H:%M,%A")))
