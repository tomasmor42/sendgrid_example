import os
import smtplib


def send_email(from_email, to_email, subject, text):
    password = os.getenv('PASS') 

    smtp_server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    smtp_server.login(from_email, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(from_email, to_email, message)
    smtp_server.close()


if __name__ == '__main__':
    subject = "Test email from Python"
    text = "Hello from Python"
    email_from = "yourname@yandex.ru"
    email_to = "name@gmail.com"

    send_email(email_from, email_to, subject, text)