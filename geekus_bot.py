import discord
import sys
from random import randint
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='gs!')

@bot.event
async def on_ready():
    print ("Bot Username: " + bot.user.name)
    print ("User ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Hello there, {}!".format(ctx.message.author.mention))
    print ("{} has pinged.".format(ctx.message.author.mention))

# @bot.command(pass_context=True)
# async def info(ctx, user: discord.Member):
#     await bot.say("The users name is: {}".format(user.name))
#     await bot.say("The users ID is: {}".format(user.id))
#     await bot.say("The users status is: {}".format(user.status))
#     await bot.say("The users highest role is: {}".format(user.top_role))
#     await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def commands(ctx):
    filename = "commands.txt"
    file = open(filename)

    builder = discord.Embed()
    builder.title = "Command List"
    builder.description = "This is a list of commands for Geekus! Prefix all commands with 'gs!' for correct use."
    builder.color = discord.Colour.blue()
    
    for line in file:
        values = line.split('$')
        builder.add_field(name=values[0], value=values[1], inline=False)

    await bot.say(embed=builder)

@bot.command(pass_context=True)
async def rules(ctx):
    filename = "rules.txt"
    file = open(filename)

    builder = discord.Embed()
    builder.title = "Rules"
    builder.description = file.read()
    builder.color = discord.Colour.blue()    
    
    await bot.say(embed=builder)

@bot.command(pass_context=True)
async def calendar(ctx):
    builder = discord.Embed()
    builder.title = "Calendar"
    builder.set_image(url="https://scontent-yyz1-1.xx.fbcdn.net/v/t1.0-9/26230257_553527274999131_1913313773842237932_n.jpg?oh=3eae5a83f93859ff3fd65e93844026df&oe=5AED37FF")
    builder.color = discord.Colour.blue()  
    await bot.say(embed=builder)

@bot.command(pass_context=True)
async def roll(ctx, face):
    result = randint(1, int(face))

    await bot.say("{} rolled a . . . {}".format(ctx.message.author.mention, result))

@bot.command(pass_context=True)
async def bye(ctx):
    await bot.say("Goodbye, {}".format(ctx.message.author.mention))
    sys.exit()

bot.run("Mzg1MjM5NjA3MTAyNTM3NzI5.DTR8QA.cWkLefBA8J0JMFmXANFiFL-qrNg")