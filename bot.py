import discord
from discord.ext import commands
import pandas as pd
client = commands.Bot(command_prefix = '!')
rate = 0
#start
@client.event
async def on_ready():
    global rate
    print("Insurance bot ready")

#ask for help command
@client.command()
async def askHelp(cxt):
    global rate
    await cxt.send('Commands: input the number of people currently enrolling into your insurance\n')

# add experienced drivers command
@client.command()
async def addE(cxt, *, numPeople):
    global rate
    await cxt.send('you have added ' + numPeople + ' experienced drivers\n' + 'Experienced Drivers generally have a lower rate because they are more reliable')
    rate += int(numPeople) * 500

#add inexpereienced drivers command
@client.command()
async def addI(cxt, *, numPeople):
    global rate
    await cxt.send('you have added ' + numPeople + ' inexperienced drivers\n' + 'inexperienced drivers generally have a higher rate because they are less reliable')
    rate += int(numPeople) * 1000

#get rate command
@client.command()
async def get(cxt):
    global rate
    await cxt.send('your current qoute is ' + str(rate))

#search city
@client.command()
async def search(cxt, city, state):
    found = False
    location = city + ", " + state
    df = pd.read_excel("Demographics.xlsx")
    dfLocation = df[df["Locations"] == location]
    for row in dfLocation.iterrows():
        await cxt.send('This is the information I have found on this specific location ' + row)
        found = True
    if found == False:
        await cxt.send('This city does not exist. Please try again')

#Clear command
@client.command()
async def clear(cxt, amount = 5):
    await cxt.channel.purge(limit = amount)


client.run('Nzc1MzkzMTE5OTE0ODE5NjE0.X6lrHQ.ezKUXq4LUlo1Hi29XKcq_PRa68s')
