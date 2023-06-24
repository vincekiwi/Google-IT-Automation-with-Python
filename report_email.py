#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_text(text):
    with open(text, 'r') as f:
        lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)

def main():
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    text_files = [f for f in os.listdir(".") if f.endswith(".txt")]
    text_files_processed = [process_text(f) for f in text_files]
    body += "<br/><br/>".join(text_files_processed)

    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)

if __name__ == "__main__":
    main()