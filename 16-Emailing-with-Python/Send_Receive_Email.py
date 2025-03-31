#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 17:03:24 2025

@author: darko.velkov
"""

import smtplib
import getpass
import imaplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
M = imaplib.IMAP4_SSL('imap.gmail.com')
#password = input('What is your password ')
email = getpass.getpass('Email: ')
password = getpass.getpass('Waht is your password: ')
#smtp_object.login(email, password)

#from_address = getpass.getpass("Enter your email: ")
#to_address = getpass.getpass("Enter the email of the recipient: ")
#subject = input("Enter the subject line: ")
#message = input("Type out the message you want to send: ")
#msg = "Subject: " + subject + '\n' + message
#smtp_object.sendmail(from_address,to_address,msg)
#smtp_object.close()

M.login(email, password)

M.list()
M.select('inbox')

typ , data = M.search(None, 'SUBJECT "test"')

email_id = data[0]

result , email_data = M.fetch(email_id, '(RFC822)')

email_data