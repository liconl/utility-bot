import os
import discord
from twilio.rest import Client

TWILIO_ID =os.getenv("TWILIO_ACCOUNT_SID") 
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

client = discord.Client()
client = discord.Client()
twilio_client = Client(TWILIO_ID,TWILIO_TOKEN)


# $0.02 per text
# create your dictionary of all phone numbers from environment variables 
all_phone_numbers = dict(
    luis=os.getenv("LUIS_PHONE_NUMBER"),
    jackie=os.getenv("JACKIE_PHONE_NUMBER"),
    ricky=os.getenv("RICKY_PHONE_NUMBER"),
    jorge=os.getenv("JORGE_PHONE_NUMBER")
)

# You can also specify specific members
weekend_only_phone_numbers = dict(
    luis=os.getenv("LUIS_PHONE_NUMBER"),
    ricky=os.getenv("RICKY_PHONE_NUMBER"),
 
)

# Content of text message
twilio_message_ready= "We are all ready, get on discord!"
twilio_message_status= "Comment on discord for your availability" 

# Sends message to every phone number with basic message
def twilio_send_all(user):
    twilio_client.api.account.messages.create(
    to=all_phone_numbers[user],
    from_=os.getenv("TWILIO_PHONE_NUMBER"),
    body=twilio_message_ready)


class SendSMSMessage():
    def __init__(self,sender,receiver,message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
    
    def twilio_send(self):
        for user in self.sender:
            twilio_client.api.account.message.create(
                to= self.receiver,
                from_= user,
                body= self.message
        )
    twilio_send()

 


