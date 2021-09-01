import os
from twilio.rest import Client
import smtplib


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCOUNT_SID  = "your-account-sid"
AUTH_TOKEN = "your-auth-token"



class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, message_to_send):
        message = self.client.messages \
            .create(
            body=message_to_send,
            from_='your-trial-number',
            to='your-phone-number'
        )

    def send_email(self, target_email, message_to_send, google_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="your-email", password="your-password")
            connection.sendmail(from_addr="your-email", to_addrs=target_email, msg=(f"Subject:Low Flight Price Alert\n\n{message_to_send}\n{google_link}").encode('utf-8'))
