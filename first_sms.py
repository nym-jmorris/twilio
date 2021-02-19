
#works!

import os
from dotenv import load_dotenv

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

# print(os.getenv('account_sid'))
# print(os.getenv('auth_token'))
#'+15183802912'

origin = os.getenv('twilio_number')
destination = '+15188593257'

corpus = 'Hello fart! I am sending you SMS from a computer program I wrote.  Replies don''t go anywhere yet. I love you!'

client = Client(account_sid,auth_token)


message = client.messages \
                .create(
                     body=corpus,
                     from_=origin,
                     to=destination
                 )

print('\nMessage with body "{}" sent to {}\nMessage ID: {}\n'.format(corpus,destination,message.sid))