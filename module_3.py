'''
from email.message import EmailMessage
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import os.path
import mimetypes
import smtplib
import getpass

styles = getSampleStyleSheet()

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

body = """Hey there!

I'm sending this from Python!"""

message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greetings from {} to {}!".format(sender, recipient)

message.set_content(body)

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

print(message)
'''

# cars.py

#!/usr/bin/env python3

import json
import locale
import sys
import reports
import os
import emails

def from_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

def car_dict(car):
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

def data_analysis(data):
    locale.setlocale(locale.LC_ALL, 'C.UTF-8')
    max_revenue = {"revenue": 0}
    max_sales = {"max_sold" : 0} 
    pop_car = {}

    for item in data:
        if item["total_sales"] > max_sales["max_sold"]:
            max_sales["max_sold"] = item["total_sales"]
            max_sales["car"] = car_dict(item)

        if item["price"] > max_revenue["revenue"]:
            max_revenue["revenue"] = item["price"]
            max_revenue["car"] = car_dict(item)

        pop_car[item["car_model"]] = item["total_sales"]

    summary = [
        "The {} generated the most revenue: ${}".format(max_revenue["car"], max_revenue["revenue"]),
        "The {} had the most sales: {}".format(max_sales["car"], max_sales["max_sold"]),
        "The most popular car model is {} with {} sales.".format(max(pop_car, key=pop_car.get), pop_car[max(pop_car, key=pop_car.get)])
    ]

    return summary

def convert_table(car_data):
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], car_dict(item), item["price"], item["total_sales"]])
    return table_data

def main(argv):
    data = from_data("/mnt/c/users/vincentm/pythonscripts/car_sales.json")
    summary = data_analysis(data)
    print(summary)

if __name__ == "__main__":
    main(sys.argv)