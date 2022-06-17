#!/usr/bin/env python

import subprocess

subprocess.call("sudo ifconfig eth0 down", shell=True)
subprocess.call("sudo ifconfig eth0 hw ether 22:8a:54:34:71:60", shell=True)
subprocess.call("sudo ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)

print("thanks baby")

