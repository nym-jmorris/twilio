
#works!

import os
from dotenv import load_dotenv

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()


# print(os.getenv('account_sid'))
# print(os.getenv('auth_token'))

origin = '+15183802912'
destination = '+15188593257'
corpus = "let's get this right..."

client = Client(os.getenv('account_sid'), os.getenv('auth_token'))


message = client.messages \
                .create(
                     body=corpus,
                     from_=origin,
                     to=destination
                 )

print('\nMessage with body "{}" sent to {}\nMessage ID: {}\n'.format(corpus,destination,message.sid))