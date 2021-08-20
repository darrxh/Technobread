import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODc4MzkyNzkzMDMzMjM2NTgx.YSAhCQ.bzGhb5UoRwiwrHSEc1_UluiGkTI')