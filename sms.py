# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Input any text you want to send',
    from_='use the random number that twilio gives you.',
    to='use any number you wan this to be sent'
)

print(message.sid)
