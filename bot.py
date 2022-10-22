import discord
from discord.ext import commands, tasks
import asyncio
import os
import sys
from discord.utils import get
from setup import *
from pynput.keyboard import Key, Controller

keyboard = Controller()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix,intents=intents)
typeStatusPlay = discord.ActivityType.playing
bot.remove_command("help")

def loadloadscrn():
    import pyscreenshot as ImageGrab
    import io
    global screengrab
    taskscreenshot.start()
    async def screengrab(channel):
        screen = ImageGrab.grab()
        arr = io.BytesIO()
        screen.save(arr, format='PNG')
        arr.seek(0)
        file = discord.File(arr,'game.png')
        await channel.send(file=file)

@tasks.loop(seconds=2)
async def taskscreenshot():
    if not loadscrn:
        taskscreenshot.stop()
        return
    if not loadscrnchannel:
        print(f"Please set a channel to send screenshots in with {prefix}setscreenshotchannel\n"
        "Thanks!")
        return
    servers = bot.guilds
    for server in servers:
        for channel in server.channels:
            if channel.id == loadscrnchannel:
                await screengrab(channel)
                return

@bot.event
async def on_message(message):
    # Okay, look, I wrote this long ago
    # I know how stupid it is
    # But I'm too lazy to make it look nice
    # So just bare with it, okay?
    # Sorry, and thanks
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
                        await asyncio.sleep(10)
                        keyboard.release(k_a)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_b)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_x)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_y)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_up)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_left)
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
                        await asyncio.sleep(10)
                        keyboard.release(k_right)
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
                    if m == "hold":
                        keyboard.press(k_lb)
                        await asyncio.sleep(10)
                        keyboard.release(k_lb)
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
                    if m == "hold":
                        keyboard.press(k_rb)
                        await asyncio.sleep(10)
                        keyboard.release(k_rb)
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
                    if m == "hold":
                        keyboard.press(k_start)
                        await asyncio.sleep(10)
                        keyboard.release(k_start)
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
                    if m == "hold":
                        keyboard.press(k_select)
                        await asyncio.sleep(10)
                        keyboard.release(k_select)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print(f'Present in {len(bot.guilds)} servers.')
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=typeStatusPlay, name=activity))
    got = False
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.id == textchannelid:
                got = True
    if not got:
        sys.exit("Please enter the text-channel ID in the setup.py file.\n"
        "If you already have, make certain the bot is in the same server as the text-channel.")
    if loadscrn:
        loadloadscrn()

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Report a bug", url="https://mi460.dev/bugs", colour=discord.Colour(0xe07314), description="**You are on the beta build**\n"
    "*Relays button input from a Discord text channel to a game*")

    embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}",icon_url=f"{bot.user.display_avatar.url}")

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
    embed.add_field(name="Stacking and holding buttons", value="You can stack button presses or hold them, as well. For example, you can press the A button 15 times (which is the max possible to stack) consecutively by typing `A 15`. You can hold the A button for 10 seconds by typing `A hold`. These functions work for every button.", inline=False)
    if ctx.author.id == myid:
        embed.add_field(name=f"{prefix}calibrate", value=f"This command is used to change what key a button will be. For example, `{prefix}calibrate A {k_a}` would change the A button to {k_a}. Of course, the A button is already {k_a}, but you get the point.", inline=False)
        embed.add_field(name=f"{prefix}load_screenshots", value=f"Requires two installations to run. It will display a screenshot every time a message in the text channel is sent.\n"
        f"If you want to set loading screenshots as a default, do it like this `{prefix}load_screenshots True`. The reverse also applies: `{prefix}load_screenshots False`", inline=False)
        embed.add_field(name=f"{prefix}setscreenshotchannel", value=f"Sets the default channel for screenshots to be sent.", inline=False)
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
async def load_screenshots(ctx,*,default = None):
    if ctx.author.id == myid:
        global loadscrn
        if loadscrn and not default:
            await ctx.send("This plugin is already loaded!\n"
            "If you are having trouble with it working, please make an issue on Github.\n"
            "https://github.com/MCMi460/Discord-Plays/issues/new")
            return
        if not default:
            c = "true"
        else:
            c = default.lower()
        with open ("setup.py","r") as read:
            contents = read.read()
            with open ("setup.py","w") as write:
                if c.startswith("true") or c.startswith("on") or c.startswith("yes"):
                    replace = contents.replace("loadscrn = False","loadscrn = True")
                    loadscrn = True
                    loadloadscrn()
                elif c.startswith("false") or c.startswith("off") or c.startswith("no"):
                    replace = contents.replace("loadscrn = True","loadscrn = False")
                    loadscrn = False
                write.write(replace)
        if contents == replace:
            await ctx.send("The plugin is already set to that.")
        else:
            await ctx.send("Sucessfully turned load_screenshots " + ("on" if loadscrn else "off"))

@bot.command()
async def setscreenshotchannel(ctx):
    if ctx.author.id == myid and loadscrn == True:
        global loadscrnchannel
        with open ("setup.py","r") as read:
            contents = read.read()
            with open ("setup.py","w") as write:
                replace = contents.replace(f"loadscrnchannel = {loadscrnchannel}",f"loadscrnchannel = {ctx.channel.id}")
                if replace != contents:
                    loadscrnchannel = ctx.channel.id
                    await ctx.send(f"Screenshot channel set to <#{ctx.channel.id}>!")
                    write.write(replace)
                else:
                    await ctx.send(f"No changes have been made.")
                    write.write(contents)

@bot.command()
async def calibrate(ctx,button:str=None,calkey:str=None):
    if ctx.author.id == myid:
        global k_up, k_down, k_left, k_right, k_a, k_b, k_x, k_y, k_lb, k_rb, k_start, k_select
        if not button:
            await ctx.send(f"Please specifiy a button to calibrate. You can calibrate to these buttons:\n"
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
        with open ("setup.py","r") as remap:
            contents = remap.read()
            with open ("setup.py","w") as remapwrite:
                if button == "up" or button == "u":
                    replace = contents.replace(f"k_up = '{k_up}", f"k_up = '{calkey}")
                    k_up = calkey
                elif button == "down" or button == "d":
                    replace = contents.replace(f"k_down = '{k_down}", f"k_down = '{calkey}")
                    k_down = calkey
                elif button == "left" or button == "l":
                    replace = contents.replace(f"k_left = '{k_left}", f"k_left = '{calkey}")
                    k_left = calkey
                elif button == "right" or button == "r":
                    replace = contents.replace(f"k_right = '{k_right}", f"k_right = '{calkey}")
                    k_right = calkey
                elif button == "a":
                    replace = contents.replace(f"k_a = '{k_a}", f"k_a = '{calkey}")
                    k_a = calkey
                elif button == "b":
                    replace = contents.replace(f"k_b = '{k_b}", f"k_b = '{calkey}")
                    k_b = calkey
                elif button == "x":
                    replace = contents.replace(f"k_x = '{k_x}", f"k_x = '{calkey}")
                    k_x = calkey
                elif button == "y":
                    replace = contents.replace(f"k_y = '{k_y}", f"k_y = '{calkey}")
                    k_y = calkey
                elif button == "start":
                    replace = contents.replace(f"k_start = '{k_start}", f"k_start = '{calkey}")
                    k_start = calkey
                elif button == "select":
                    replace = contents.replace(f"k_select = '{k_select}", f"k_select = '{calkey}")
                    k_select = calkey
                elif button == "lb":
                    replace = contents.replace(f"k_lb = '{k_lb}", f"k_lb = '{calkey}")
                    k_lb = calkey
                elif button == "rb":
                    replace = contents.replace(f"k_rb = '{k_rb}", f"k_rb = '{calkey}")
                    k_rb = calkey
                else:
                    await ctx.send("Undefined button. Please choose a supported button.")
                    return
                if contents == replace:
                    await ctx.send("No changes were made.")
                    remapwrite.write(contents)
                    return
                remapwrite.write(replace)
                await ctx.send(f"Successfully remapped button {button} to {calkey}!")

bot.run(token)
