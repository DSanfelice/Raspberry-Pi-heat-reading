# File: create_daily_git_pull.py
# Company: The San Diego Drone Pro
# Author: Daniel "Dragon" Sanfelice
# Description: Monitor the temperature of your Raspberry Pi zero and send an email if it gets too hot

import time
import os
import subprocess
import argparse
import sys

#cpu_temp = os.system("vcgencmd measure_temp")

#def get_temp():
#    os.system("#!/bin/bash")
#    os.system("while :")
#    os.system("do")
#    os.system("	    vcgencmd measure_temp")
#    os.system("	    sleep 30")
#    os.system("done")

cpu_temp = os.popen("vcgencmd").read()

while cpu_temp <70:
    print("cpu temp")

else:
    print("The CPU is too hot. Current CPU temp is " + cpu_temp)
