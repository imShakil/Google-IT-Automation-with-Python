#!/usr/bin/env python3

import os
import email.message
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment=None):
    msg = email.message.EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    if attachment:
        filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(filename)
        mime_type, mime_sub_type = mime_type.split('/', 1)

        with open(attachment, 'rb') as af:
            msg.add_attachment(af.read(), maintype=mime_type, subtype=mime_sub_type, filename=filename)
    
    return msg


def send_email(message):
    mail_server = smtplib.SMTP(host='localhost')
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == "__main__":
    sender = 'automation@example.com'
    recipent = 'student@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment = 'proccessed.pdf'
    msg = generate_email(sender, recipent, subject, body, attachment)
    send_email(msg)

