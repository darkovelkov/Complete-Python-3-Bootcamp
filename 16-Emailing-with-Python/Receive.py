#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 18:02:21 2025

@author: darko.velkov
"""

import imaplib
import email
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.select("INBOX")
typ , data = M.search('All', 'FROM hristina')
sinche = data[0]

result, data1 = M.fetch(sinche, '(RFC822)')

raw_email = data1[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)