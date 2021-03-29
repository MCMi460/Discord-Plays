import discord
from discord.ext import commands, tasks
import asyncio
import os
import time
import sys
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from setup import token, prefix, activity, textchannelid, myid
from pynput.keyboard import Key, Controller

keyboard = Controller()
keyp = False
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix,intents=intents)
typeStatusPlay = discord.ActivityType.playing
bot.remove_command("help")

@tasks.loop(seconds=25.0)
async def unpresskey():
    global keyp
    if keyp:
        keyboard.release('1')
        keyboard.release('2')
        keyboard.release('q')
        keyboard.release('w')
        keyboard.release('e')
        keyboard.release('r')
        keyp = False

@bot.event
async def on_message(message):
    if message.channel.id == textchannelid:
        if message.content.lower() == "u" or message.content.lower() == "up":
            keyboard.press('q')
            time.sleep(0.2)
            keyboard.release('q')
        elif message.content.lower() == "d" or message.content.lower() == "down":
            keyboard.press('w')
            time.sleep(0.2)
            keyboard.release('w')
        elif message.content.lower() == "l" or message.content.lower() == "left":
            keyboard.press('e')
            time.sleep(0.2)
            keyboard.release('e')
        elif message.content.lower() == "r" or message.content.lower() == "right":
            keyboard.press('r')
            time.sleep(0.2)
            keyboard.release('r')
        elif message.content.lower() == "a":
            keyboard.press('1')
            time.sleep(0.2)
            keyboard.release('1')
        elif message.content.lower() == "b":
            keyboard.press('2')
            time.sleep(0.2)
            keyboard.release('2')
        elif message.content.lower() == "x":
            keyboard.press('3')
            time.sleep(0.2)
            keyboard.release('3')
        elif message.content.lower() == "y":
            keyboard.press('4')
            time.sleep(0.2)
            keyboard.release('4')
        elif message.content.lower() == "lb":
            keyboard.press('5')
            time.sleep(0.2)
            keyboard.release('5')
        elif message.content.lower() == "rb":
            keyboard.press('6')
            time.sleep(0.2)
            keyboard.release('6')
        elif message.content.lower() == "start":
            keyboard.press('7')
            time.sleep(0.2)
            keyboard.release('7')
        elif message.content.lower() == "select":
            keyboard.press('8')
            time.sleep(0.2)
            keyboard.release('8')
        else:
            global keyp
            m = message.content.lower()
            if m.startswith('a '):
                m = m.replace('a ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('1')
                            time.sleep(0.2)
                            keyboard.release('1')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('1')
                        keyp = True
            elif m.startswith('b '):
                m = m.replace('b ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('2')
                            time.sleep(0.2)
                            keyboard.release('2')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('2')
                        keyp = True
            elif m.startswith('x '):
                m = m.replace('x ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('3')
                            time.sleep(0.2)
                            keyboard.release('3')
                            time.sleep(0.1)
                except:
                    pass
            elif m.startswith('y '):
                m = m.replace('y ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('4')
                            time.sleep(0.2)
                            keyboard.release('4')
                            time.sleep(0.1)
                except:
                    pass
            elif m.startswith('u '):
                m = m.replace('u ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('q')
                            time.sleep(0.2)
                            keyboard.release('q')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('q')
                        keyp = True
            elif m.startswith('d '):
                m = m.replace('d ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('w')
                            time.sleep(0.2)
                            keyboard.release('w')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('w')
                        keyp = True
            elif m.startswith('l '):
                m = m.replace('l ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('e')
                            time.sleep(0.2)
                            keyboard.release('e')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('e')
                        keyp = True
            elif m.startswith('r '):
                m = m.replace('r ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('r')
                            time.sleep(0.2)
                            keyboard.release('r')
                            time.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press('r')
                        keyp = True
            elif m.startswith('lb '):
                m = m.replace('lb ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('5')
                            time.sleep(0.2)
                            keyboard.release('5')
                            time.sleep(0.1)
                except:
                    pass
            elif m.startswith('rb '):
                m = m.replace('rb ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('6')
                            time.sleep(0.2)
                            keyboard.release('6')
                            time.sleep(0.1)
                except:
                    pass
            elif m.startswith('start '):
                m = m.replace('start ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('7')
                            time.sleep(0.2)
                            keyboard.release('7')
                            time.sleep(0.1)
                except:
                    pass
            elif m.startswith('select '):
                m = m.replace('select ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press('8')
                            time.sleep(0.2)
                            keyboard.release('8')
                            time.sleep(0.1)
                except:
                    pass
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print(f'Present in {len(bot.guilds)} servers.')
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=typeStatusPlay, name=activity))
    unpresskey.start()

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Report a bug", url="https://mi460.dev/bugs", colour=discord.Colour(0xe07314), description="**You are on the beta build**\n"
    "*Relays button input from a Discord text channel to a game*")

    embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}",icon_url=f"{bot.user.avatar_url}")

    embed.add_field(name="Up D-PAD", value="Type `U`")
    embed.add_field(name="Down D-PAD", value="Type `D`")
    embed.add_field(name="Left D-PAD", value="Type `L`")
    embed.add_field(name="Right D-PAD", value="Type `R`")
    embed.add_field(name="A Button", value="Type `A`")
    embed.add_field(name="B Button", value="Type `B`")
    embed.add_field(name="X Button", value="Type `X`")
    embed.add_field(name="Y Button", value="Type `Y`")
    embed.add_field(name="Start", value="Type `Start`")
    embed.add_field(name="Select", value="Type `Select`")
    embed.add_field(name="Left Trigger", value="Type `LB`")
    embed.add_field(name="Right Trigger", value="Type `RB`")
    embed.add_field(name="Stacking and holding buttons", value="You can stack button presses or hold them, as well. For example, you can press the A button 15 times (which is the max possible to stack) consecutively by typing `A 15`. You can hold the A button for up to 25 seconds by typing `A hold`. The stack function works for every button, but you can only hold the A, B, Up, Down, Left, and Right buttons.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
    if ctx.author.id == myid:
        await ctx.send("Stopping...")
        print("Stopping...")
        await ctx.send("Session ended.")
        sys.exit("Session Ended.")

@bot.command()
async def restart(ctx):
    if ctx.author.id == myid:
        await ctx.send("Restarting/ending session...")
        print("Restarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)

bot.run(token)