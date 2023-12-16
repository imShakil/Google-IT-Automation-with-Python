#!/usr/bin/env python3


import os
import shutil
import psutil
import emails
import platform
import subprocess


"""_summary_
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 100MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""


def cpu_overload(thershold):
    cpu_usage = float(psutil.cpu_percent())
    return cpu_usage > thershold


def disk_low(thershold):
    disk_stats = psutil.disk_usage(os.getcwd())  # sdiskusage(total=344384794624, used=241299521536, free=75898085376, percent=76.1)
    disk_avail_percent = float(100.0) - float(disk_stats[3])
    return disk_avail_percent < thershold


def memory_low(thershold):
    thershold = thershold * 1024 * 1024 # in bytes
    avl_mem = int(psutil.virtual_memory().available) # bytes
    return avl_mem < thershold


def ping(host):
    """
    Args:
        host (string): hostname

    Returns:
        boolean: return True if hostname resolved False otherwise
    """
    param = '-c'
    if platform.system().lower() == 'windows':
        param = '-n'
    cmd = ['ping', param, '1', host]
    return subprocess.call(cmd) != 0


if __name__ == "__main__":
    sender = 'automation@example.com'
    recipent = 'student@example.com'
    body = 'Please check your system and resolve the issue as soon as possible'
    error = None
    cpu_thershold = 80.0
    disk_thershold = 20.0
    memory_thershold = 100
    hostname = 'localhost'

    if cpu_overload(thershold=cpu_thershold):
        error = "Error - CPU usage is over {}%".format(int(cpu_thershold))
    if disk_low(thershold=disk_thershold):
        error = "Error - Available disk space is less than {}%".format(int(disk_thershold))
    if memory_low(thershold=memory_thershold):
        error = "Error - Available memory is less than {}MB".format(int(memory_thershold))
    if ping(host=hostname):
        error = "Error - {} cannot be resolved to 127.0.0.1".format(hostname)
    
    if error:
        print(error)
        msg = emails.generate_email(sender=sender, recipient=recipent, subject=error, body=body)
        emails.send_email(msg)
        print('Error reported successfully')
