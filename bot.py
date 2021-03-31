import discord
from discord.ext import commands, tasks
import asyncio
import os
import time
import sys
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from setup import token, prefix, activity, textchannelid, myid, k_up, k_down, k_left, k_right, k_a, k_b, k_x, k_y, k_lb, k_rb, k_start, k_select
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
        keyboard.release(k_a)
        keyboard.release(k_b)
        keyboard.release(k_x)
        keyboard.release(k_y)
        keyboard.release(k_up)
        keyboard.release(k_down)
        keyboard.release(k_left)
        keyboard.release(k_right)
        keyp = False

@bot.event
async def on_message(message):
    if message.channel.id == textchannelid:
        if message.content.lower() == "u" or message.content.lower() == "up":
            keyboard.press(k_up)
            await asyncio.sleep(0.2)
            keyboard.release(k_up)
        elif message.content.lower() == "d" or message.content.lower() == "down":
            keyboard.press(k_down)
            await asyncio.sleep(0.2)
            keyboard.release(k_down)
        elif message.content.lower() == "l" or message.content.lower() == "left":
            keyboard.press(k_left)
            await asyncio.sleep(0.2)
            keyboard.release(k_left)
        elif message.content.lower() == "r" or message.content.lower() == "right":
            keyboard.press(k_right)
            await asyncio.sleep(0.2)
            keyboard.release(k_right)
        elif message.content.lower() == "a":
            keyboard.press(k_a)
            await asyncio.sleep(0.2)
            keyboard.release(k_a)
        elif message.content.lower() == "b":
            keyboard.press(k_b)
            await asyncio.sleep(0.2)
            keyboard.release(k_b)
        elif message.content.lower() == "x":
            keyboard.press(k_x)
            await asyncio.sleep(0.2)
            keyboard.release(k_x)
        elif message.content.lower() == "y":
            keyboard.press(k_y)
            await asyncio.sleep(0.2)
            keyboard.release(k_y)
        elif message.content.lower() == "lb":
            keyboard.press(k_lb)
            await asyncio.sleep(0.2)
            keyboard.release(k_lb)
        elif message.content.lower() == "rb":
            keyboard.press(k_rb)
            await asyncio.sleep(0.2)
            keyboard.release(k_rb)
        elif message.content.lower() == "start":
            keyboard.press(k_start)
            await asyncio.sleep(0.2)
            keyboard.release(k_start)
        elif message.content.lower() == "select":
            keyboard.press(k_select)
            await asyncio.sleep(0.2)
            keyboard.release(k_select)
        else:
            global keyp
            m = message.content.lower()
            if m.startswith('a '):
                m = m.replace('a ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_a)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_a)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_a)
                        keyp = True
            elif m.startswith('b '):
                m = m.replace('b ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_b)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_b)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_b)
                        keyp = True
            elif m.startswith('x '):
                m = m.replace('x ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_x)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_x)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_x)
                        keyp = True
            elif m.startswith('y '):
                m = m.replace('y ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_y)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_y)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_y)
                        keyp = True
            elif m.startswith('u '):
                m = m.replace('u ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_up)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_up)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_up)
                        keyp = True
            elif m.startswith('d '):
                m = m.replace('d ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_down)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_down)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_down)
                        keyp = True
            elif m.startswith('l '):
                m = m.replace('l ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_left)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_left)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_left)
                        keyp = True
            elif m.startswith('r '):
                m = m.replace('r ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_right)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_right)
                            await asyncio.sleep(0.1)
                except:
                    if m == "hold":
                        keyboard.press(k_right)
                        keyp = True
            elif m.startswith('lb '):
                m = m.replace('lb ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_lb)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_lb)
                            await asyncio.sleep(0.1)
                except:
                    pass
            elif m.startswith('rb '):
                m = m.replace('rb ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_rb)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_rb)
                            await asyncio.sleep(0.1)
                except:
                    pass
            elif m.startswith('start '):
                m = m.replace('start ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_start)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_start)
                            await asyncio.sleep(0.1)
                except:
                    pass
            elif m.startswith('select '):
                m = m.replace('select ','')
                try:
                    if int(m) < 16:
                        for x in range(0,int(m)):
                            keyboard.press(k_select)
                            await asyncio.sleep(0.2)
                            keyboard.release(k_select)
                            await asyncio.sleep(0.1)
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

@bot.command()
async def calibrate(ctx,button:str=None,calkey:str=None):
    if ctx.author.id == myid:
        global k_up, k_down, k_left, k_right, k_a, k_b, k_x, k_y, k_lb, k_rb, k_start, k_select
        if not button:
            await ctx.send("Please specifiy a button to calibrate. You can calibrate to these buttons:\n"
            "UP\n"
            "DOWN\n"
            "LEFT\n"
            "RIGHT\n"
            "A\n"
            "B\n"
            "X\n"
            "Y\n"
            "LB (LEFT TRIGGER)\n"
            "RB (RIGHT TRIGGER)\n"
            "START\n"
            "SELECT\n")
            return
        if not calkey:
            await ctx.send(f"Please specifiy a key to calibrate `{button}` to.")
            return
        if len(calkey) != 1:
            await ctx.send("Please type a supported key on your keyboard.")
            return
        calkey = calkey.lower()
        button = button.lower()
        if button == "up" or button == "u":
            k_up = calkey
        elif button == "down" or button == "d":
            k_down = calkey
        elif button == "left" or button == "l":
            k_left = calkey
        elif button == "right" or button == "r":
            k_right = calkey
        elif button == "a":
            k_a = calkey
        elif button == "b":
            k_b = calkey
        elif button == "x":
            k_x = calkey
        elif button == "y":
            k_y = calkey
        elif button == "start":
            k_start = calkey
        elif button == "select":
            k_select = calkey
        elif button == "lb":
            k_lb = calkey
        elif button == "rb":
            k_rb = calkey
        else:
            await ctx.send("Undefined button. Please choose a supported button.")
            return
        await ctx.send(f"Successfully remapped button {button} to {calkey}!")

bot.run(token)
