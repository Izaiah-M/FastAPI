import random
import Client # this is supposed to be from the twilio lib that you download....so download..then import it properly
#  Supposed to be "from twilio import Client"

otp = random.randint(100000, 999999)

# From twilio
account_sid = None

# Still from twilio

auth_token = None

# Create a client
client = Client(account_sid, auth_token)

# Create the msg that you will send to the user
msg = client.messages.create (

    body = f"Your Otp is {otp}",
    from_ = "7842397423", # should be the virtual number twilio gives you
    to = "75648882" # phone number of the user
)