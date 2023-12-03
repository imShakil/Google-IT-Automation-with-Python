#!/usr/bin/env python3


import os
import smtplib
import getpass
import mimetypes
from email.message import EmailMessage


msg = EmailMessage()
print(msg)

sender = "mhiceiuk@gmail.com"
recipient = "shakil@gluu.org"

msg['From'] = sender
msg['To'] = recipient
print(msg)

# add mail subject
msg['Subject'] = "Greetings from {} to {}".format(sender, recipient)

# add mail body
body = """Hi there!

This email confirms that we have are able to connect each other. Please reply if you recieve this mail.

Regards,
Mobarak Hosen
gluu.org"""

msg.set_content(body)
print(msg)

# add attachment

attachments = "../topic.txt"
file_name = os.path.basename(attachments)

mime_type, _ = mimetypes.guess_type(attachments)
print(mime_type)

mime_type, mime_sub_type = mime_type.split('/', 1)
print(mime_type, mime_sub_type)

with open(attachments, "rb") as ap:
    msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_sub_type, filename=file_name)
    
print(msg)

# send mail

mail_server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)
mail_server.send_message(msg)
mail_server.quit()

