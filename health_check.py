#!/usr/bin/env python3

'''
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
'''

import shutil
import psutil
import os
import emails
import socket

from_email = "automation@example.com"
to_email = "{}@example.com".format(os.environ.get('USER'))

max_cpu_usage = 80
max_disk_usage = 20
max_memory_usage = 500
localhost_ip = "127.0.0.1"

def check_cpu_usage():
    current_cpu_usage = psutil.cpu_percent(interval=3)
    return current_cpu_usage > max_cpu_usage

def check_disk_usage():
    current_disk_usage = shutil.disk_usage("/")
    return current_disk_usage.free / current_disk_usage.total * 100 < max_disk_usage

def check_memory_usage():
    current_memory_usage = psutil.virtual_memory().available / (1024 ** 2)
    return current_memory_usage < max_memory_usage

def check_localhost():
    return localhost_ip != socket.gethostbyname("localhost")

def send_email(alert, from_email, to_email):
    content = {
        "sender": from_email,
        "receiver": to_email,
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    message = emails.generate_email(content)
    emails.send_email(message)

def main():
    alert = ""
    if check_cpu_usage():
        alert = f"Error - CPU usage is over {max_cpu_usage}%"
    elif check_disk_usage():
        alert = f"Error - Available disk space is less than {max_disk_usage}%"
    elif check_memory_usage():
        alert = f"Error - Available memory is less than {max_memory_usage}MB"
    elif check_localhost():
        alert = f"Error - localhost cannot be resolved to {localhost_ip}"

    if alert:
        send_email(alert, from_email, to_email)
    else:
        print("Healthchecks green")

if __name__ == "__main__":
    main()