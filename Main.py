# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:28:36 2021

@author: Muhammad Qasim
"""


import os
import smtplib
import mimetypes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def mime_init(from_addr, recipients_addr, subject, body):


    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = ','.join(recipients_addr)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg


def send_email(user, password, from_addr, recipients_addr, subject, body, files_path=None, server='smtp.gmail.com'):

    #   assert isinstance(recipents_addr, list)
    FROM = from_addr
    TO = recipients_addr if isinstance(recipients_addr, list) else recipients_addr.split(' ')
    PASS = password
    SERVER = server
    SUBJECT = subject
    BODY = body
    msg = mime_init(FROM, TO, SUBJECT, BODY)
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user,PASS)
    text = msg.as_string()
    # Send mail
    smtpserver.sendmail(FROM, TO, text)
    smtpserver.quit()
    print("Done")


import os

if __name__ == "__main__":
    file_path = os.listdir('images/')
        
    body = "Your email Body here."

    user = 'your email here'         # Email userID
    password = 'your password here'      # Email password
    from_addr = 'your email here'
    recipients_addr = []
    for file in file_path:
        recipients_addr.append(file[0:len(file)-5]+"@gift.edu.pk")
    print(recipients_addr)
    subject = 'Mail Test'
    # If you want to attach something to the email, you can specify the path of the file in here
    #file_path = ['/Path/file.txt', 'image.png', '/Path/clip.mp4']
    #file_path = 'null'
    send_email(user, password, from_addr, recipients_addr, subject, body, file_path)