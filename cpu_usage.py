#!/usr/bin/env python3
import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUT: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded.")
else:
    print("Everything is OK.")

print("Here is a change.")
print("Adding another change.")
