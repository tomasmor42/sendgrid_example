import os
import imaplib
import email
from email.message import EmailMessage
from email.header import decode_header
import pprint

HOST = 'imap.yandex.ru'
USER = 'alena.vorojko@yandex.ru'
PASS = os.getenv('PASS')



def connect_to_server():
    imap_client = imaplib.IMAP4_SSL(HOST)
    imap_client.login(USER, PASS)
    return imap_client


def decode_message_subject(msg):
    subject_list = decode_header(msg['Subject'])
    decoded_list = []
    for subject in subject_list:
        if subject[1]:
            subject = (subject[0].decode(subject[1]))
        elif type(subject[0]) == bytes:
            subject = subject[0].decode('utf-8')
        else:
            subject = subject[0]
        decoded_list.append(subject)
    subject = ''.join(decoded_list)
    return subject

def get_email():
    imap_client = connect_to_server()
    imap_client.select('Inbox')
    status, data = imap_client.search(None, 'ALL')
    for num in data[0].split():
        tmp, data = imap_client.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1],_class = EmailMessage)
        #import pdb; pdb.set_trace()
        print(msg['Subject'])
        decoded_subject = decode_message_subject(msg)
        print(decoded_subject)
        
        break
    imap_client.close()

if __name__ == '__main__':
    get_email()