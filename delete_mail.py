__author__ = 'Vishal'

import imaplib

'''
Simple script that delete emails from a given sender
params:
-username: Gmail username
-pw: gmail pw
-label: If you have a label that holds the emails, specify here
-sender: the target sender you want to delete

usage: python delete_emails.py

see http://stackoverflow.com/a/5366205 for mode details

'''


def delete_mail():

    args = dict()

    args['username'] = input("Enter your Gmail username: ")
    args['password'] = input("Enter your Gmail password: ")
    args['sender'] = input("Enter your sender username: ")

    print("Logging into Gmail with user %s\n" % args['username'])
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    connection_message = server.login(args['username'], args['password'])
    print(connection_message)

    print("Using inbox")
    server.select("inbox")

    print("Searching emails from %s" % args['sender'])
    result_status, email_ids = server.search(None, '(FROM "%s")' % args['sender'])
    email_ids = email_ids[0].split()

    if len(email_ids) == 0:
        print("No emails found, finishing...")

    else:
        print("%d emails found, sending to trash folder..." % len(email_ids))
        server.store('1:*', '+X-GM-LABELS', '\\Trash')
        server.expunge()

    print("Done!")


if __name__ == '__main__':
    delete_mail()
