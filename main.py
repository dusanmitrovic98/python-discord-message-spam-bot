import discord
import random
import asyncio

# Your bot's token
TOKEN = ''

# ID of the target server and channel
SERVER_ID = 123456
CHANNEL_ID = 123456

# List of random messages
random_messages = [
    "Hello, world!",
    "How's everyone doing?",
    "Just dropping by to say hi!",
    "Hope you're having a great day!",
    "Keep shining bright!",
    "Smile and spread positivity!",
    "You're capable of amazing things!",
    "Sending good vibes your way!",
    "Believe in yourself and your dreams.",
    "You're unique and wonderful!",
    "Every day is a new opportunity.",
    "You're making a difference!",
    "Embrace the journey of life.",
    "You're stronger than you think!",
    "Today is full of possibilities.",
    "You're a ray of sunshine!",
    "Chase your dreams with passion.",
    "You're valued and appreciated.",
    "Stay positive and keep moving forward.",
    "The world is better with you in it.",
    "You're capable of overcoming anything.",
    "Your kindness makes a difference.",
    "Keep your head high and stay strong.",
    "You're doing better than you know.",
    "Your potential is limitless!",
    "Spread kindness and positivity.",
    "Believe in the power of positivity.",
    "You're a true inspiration.",
    "Keep smiling and keep shining.",
    "You're making progress every day.",
    "You bring joy to those around you.",
    "Keep pushing through challenges.",
    "You're meant for great things!",
    "Your positivity is contagious.",
    "Take pride in your accomplishments.",
    "You're a beacon of hope.",
    "Keep your heart open to new possibilities.",
    "You're changing lives with your actions.",
    "Stay true to yourself and your values.",
    "You're capable of overcoming any obstacle.",
    "Your positivity brightens the world.",
    "Keep chasing your dreams!",
    "You're making a positive impact.",
    "Your journey is an inspiring one.",
    "Keep spreading love and positivity.",
    "You're an amazing individual.",
    "Believe in the beauty of each moment.",
    "You're a source of strength for others.",
    "Stay focused and keep moving forward.",
    "You're making a difference one step at a time.",
    "Your presence brings positivity to the room.",
]

intents = discord.Intents.default()  # Create a default intents object
intents.typing = False  # You can customize these based on your bot's needs
intents.presences = False

client = discord.Client(intents=intents)  # Pass the intents object when creating the client

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    while True:
        random_message = random.choice(random_messages)
        server = client.get_guild(SERVER_ID)
        channel = server.get_channel(CHANNEL_ID)
        await channel.send(random_message)
        await asyncio.sleep(5)

client.run(TOKEN)
