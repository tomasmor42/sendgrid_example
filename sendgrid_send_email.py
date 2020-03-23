import os

import sendgrid
from sendgrid.helpers.mail import Mail


SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_TEMPLATE_ID = os.getenv('SENDGRID_TEMPLATE_ID')


data = {
    "user":
        {
            "name": "olga",
            "last_name": "sergeeva"
        }
}

def send_email(from_email, to_email, template_id, template_data):

    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    message = Mail(
    from_email=from_email,
    to_emails=to_email,
    )
    message.template_id = template_id
    message.dynamic_template_data = template_data
    response = sg.send(message)

if __name__ == '__main__':
    send_email(from_email='from_template@gmail.com', to_email='your_address@gmail.com', 
           template_id=SENDGRID_TEMPLATE_ID, template_data=data)
    