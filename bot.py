import discord

client = discord.Client()

fake_database = dict()

#cpu="N/A",gpu="N/A",ram="N/A",mobo="N/A",storage="N/A",thermal="N/A",case="N/A",psu="N/A"



class userpc:
    def __init__(self):
        self.cpu = cpu()
        self.gpu = gpu()
        self.ram = ram()
        self.mobo = "N/A"
        self.storage = "N/A"
        self.thermal = "N/A"
        self.case = "N/A"
        self.psu = "N/A"

    def showspecs(self):

        return [self.cpu.model, self.gpu.model, self.ram.model]

    def changecpu(self, cpu_input):

        self.cpu.model = cpu_input

    def changegpu(self, gpu_input):

        self.gpu.model = gpu_input

    def changeram(self, ram_input):

        self.ram.model = ram_input


class cpu:
    def __init__(self, model="N/A"):
        self.model = model

class gpu:
    def __init__(self, model="N/A"):
        self.model = model

class ram:
    def __init__(self, model="N/A"):
        self.model = model

"""
class mobo:
    def __init__(self):

class storage:
    def __init__(self):

"""



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
    print('Ready!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if (msg.startswith('$hello')):
        await message.channel.send('Hello!')

    elif (msg.startswith('$myid')):
        await message.channel.send('your Id is ' + str(client.user.id))
        await message.channel.send('my mention is' + str(client.user.mention))
        await message.channel.send(message.author.avatar_url)
        await message.channel.send('your name is ' + str(message.author.mention))

    elif (msg.startswith('$idof')):
        userid = msg[msg.find('@'):]
        await message.channel.send(userid)


    elif (msg.startswith('$addpc')):
        if (has_pc(client.user.id)):
            await message.channel.send("You already have a PC added to your profile.")
        else:
            new_computer = userpc()
            fake_database.update({client.user.id:new_computer})
            await message.channel.send("New Rig added to your profile")

    elif (msg.startswith('$mypc')):
        if (has_pc(client.user.id)):
            pc_array = fake_database[client.user.id].showspecs()
            await message.channel.send("""
            Your Specs:
            
            CPU: {}
            GPU: {}
            RAM: {}
            
            """)
        else:
            await message.channel.send("You do not have a PC added to your profile")

    elif (msg.startswith('$removepc')):
        if (has_pc(client.user.id)):
            fake_database.pop(client.user.id)
            await message.channel.send("Successfully removed PC from profile")
        else:
            await message.channel.send("You have no PC on your profile to remove")

    elif (msg.startswith('$changecpu')):
        if (has_pc(client.user.id)):
            cpu_model = msg[msg.find(' '):]
            fake_database[client.user.id].changecpu(cpu_model)
            await message.channel.send("Added CPU: " + cpu_model + " to PC profile")
        else:
            await message.channel.send("You have no PC on your profile")

    elif (msg.startswith('$changegpu')):
        if (has_pc(client.user.id)):
            gpu_model = msg[msg.find(' '):]
            fake_database[client.user.id].changegpu(gpu_model)
            await message.channel.send("Added GPU: " + gpu_model + " to PC profile")
        else:
            await message.channel.send("You have no PC on your profile")

    elif (msg.startswith('$changeram')):
        if (has_pc(client.user.id)):
            ram_model = msg[msg.find(' '):]
            fake_database[client.user.id].changeram(ram_model)
            await message.channel.send("Added RAM: " + ram_model + " to PC profile")
        else:
            await message.channel.send("You have no PC on your profile")

client.run('ODc4MzkyNzkzMDMzMjM2NTgx.YSAhCQ.bzGhb5UoRwiwrHSEc1_UluiGkTI')
