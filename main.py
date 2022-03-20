import discord
import random
import os
from dotenv import load_dotenv
from twilio.rest import Client
from mongoDB.index import item_1
import io
import aiohttp
from mongoDB.index import images
import asyncio # To get the exception
from services.twilio import twilio_send_all

load_dotenv()

TOKEN = os.getenv("DEV_TOKEN")
TWILIO_ID =os.getenv("TWILIO_ACCOUNT_SID") 
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

client = discord.Client()
twilio_client = Client(TWILIO_ID,TWILIO_TOKEN)

commands = dict(
    flip="Flip a coin head or tails",
    geton="Text the squad a Get On message",
    ricky="Call Ricky a  spaceman",
    jackie="Call Jackie a gorilla",
)

# $0.02 per text
phone_numbers = dict(
    luis=os.getenv("LUIS_PHONE_NUMBER"),
    jackie=os.getenv("JACKIE_PHONE_NUMBER"),
    ricky=os.getenv("RICKY_PHONE_NUMBER"),
    tyler=os.getenv("TYLER_PHONE_NUMBER"),
    jorge=os.getenv("JORGE_PHONE_NUMBER")
)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    int = random.random()
    if message.author == client.user:
        return
    if message.content.startswith('$flip'):
        if int > 0.5:
            await message.channel.send("Heads")
        else:
            await message.channel.send("Tails")
    if message.content.startswith("$geton"):
        for user in phone_numbers:
            twilio_send_all(user)
        await message.channel.send("Avengers Assemble!")
    # Target single memembers with a custom text
    if message.content.startswith("$jackie"):
        await message.channel.send("Jackie loves to go to the zoo 🦍")
    if message.content.startswith("$ricky"):
        await message.channel.send("Ricky is a spaceman 🚀")\
     # Lists of all commands
    if message.content.startswith("$commands"):
        await message.channel.send("\n".join(["${} : {}".format(k,v) for k,v in sorted(commands.items())]))  
    # Testing Mongo connection with sample image
    if message.content.startswith("$test"):
        await message.channel.send(file=discord.File('./images/sample.jpg'))
    if message.content.startswith("$testMongo"):
        await images_service_test(message)
    if message.content.startswith("$showimage"):
        await on_showImage(message)
    if message.content.startswith("$addimage"):
        await on_addImage(message)



async def images_service(message,topic):
    print(message)
    print(type(topic))
    async with aiohttp.ClientSession() as session:
        async with session.get(images.find_one({"topic":topic}).get("url")) as resp:
            if resp.status != 200:
             return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))


async def images_service_test(message):
    async with aiohttp.ClientSession() as session:
        async with session.get(images.find_one({"topic":"bird"}).get("url")) as resp:
            if resp.status != 200:
             return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))



async def add_image(message):
    await message.channel.send("Adding an image to the database in the next 10 seconds. Add in [target, topic, url] formmat. If there is no target, use any")

    try:
        msg = await client.wait_for("message", check=check, timeout=10) # 30 seconds to reply
    except asyncio.TimeoutError:
        await message.send("Sorry, you didn't reply in time!")

@client.event
async def on_addImage(message):
     
    if message.content.startswith('$addimage'):
        channel = message.channel
        await channel.send('Adding an image to the database. To add: \"image target topic url\" \n If there is no target, us any. Example: image any varloant google.com ')

        def check(m):
            user_response = m.content.split()
            target= user_response[1]
            topic= user_response[2]
            url= user_response[3]
            return "image" in m.content and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Added new image to database!'.format(msg))

@client.event
async def on_showImage(message):
    if message.content.startswith('$showimage'):
        channel = message.channel
        await channel.send('To show an image from a player: image target topic. Ex: image luis ace')
        print(message.content.split())
        user_response = message.content.split()
        target= user_response[1]
        topic= user_response[2]
        await images_service(message,topic)

        def check(m):
            #send the values to image service 
            return "image" in m.content and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await channel.send('Showing new image!'.format(msg))
        user_response = message.content.split()
        await images_service(message,topic)




client.run(TOKEN)