import discord

client = discord.Client()

fake_database = dict()

#cpu="N/A",gpu="N/A",ram="N/A",mobo="N/A",storage="N/A",thermal="N/A",case="N/A",psu="N/A"



class userpc:
    def __init__(self):
        self.cpu = cpu()
        self.gpu = gpu()
        self.ram = ram()
        self.mobo = mobo()
        self.storage = storage()
        self.thermal = thermal()
        self.case = case()
        self.psu = psu()

    def check_specs(self):

    def addcpu(self):

    def addgpu(self):

    def addram(self):

    def addmobo(self):

class cpu:
    def __init__(self):





class gpu:
    def __init__(self):

class ram:
    def __init__(self):

class mobo:
    def __init__(self):

class storage:
    def __init__(self):


ram_brand_list = ["Corsair","G.Skill","HyperX","Crucial","Kingston","TeamGroup"]
cpu_brand_list = ["AMD","Intel"]
gpu_brand_list = ["Nvidia","AMD"]
mobo_brand_list = ["Asrock","Asus","MSI"]


def has_pc(user):
    for index in fake_database:
        if (user == index):
            return True
        else:
            return False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Ready to rock and roll')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

       msg = message.content.lower()
    if (msg.startswith('$hello')):
        await message.channel.send('Hello!')
    elif (msg.startswith('$addpc'))
        if (has_pc()):
            new_computer = userpc()
            fake_database[user](new_computer)
            await message.channel.send("New Rig added to your profile")
        else:
            await message.channel.send("You already have a PC added to your profile.")





client.run('ODc4MzkyNzkzMDMzMjM2NTgx.YSAhCQ.bzGhb5UoRwiwrHSEc1_UluiGkTI')
