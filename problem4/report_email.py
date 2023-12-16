#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def process_report_data(dir):
    json_data_list = ""

    for file in os.listdir(dir):
        print(file)
        lines = open(dir + file, 'r').read().split('\n')
        data = 'name: ' + lines[0] + '<br/>'
        data += 'weight: ' + lines[1] + '<br/><br/>'
        json_data_list += str(data)

    return json_data_list

def dateForm(format='%B %d, %Y'):
    return datetime.datetime.now().strftime(format)

if __name__ == "__main__":
    sender = 'automation@example.com'
    recipent = 'student@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment = '/tmp/processed.pdf'
    report_title = 'Processed Update on {}'.format(dateForm())
    report_data = process_report_data('supplier-data/descriptions/')
    print(report_data)
    reports.generate(filename=attachment, title=report_title, paragraph=report_data)
    msg = emails.generate_email(sender=sender, recipient=recipent, subject=subject, body=body, attachment=attachment)
    emails.send_email(msg)


