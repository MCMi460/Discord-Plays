# Discord Plays Bot

*Allows the remote control of a game from a text-channel in Discord*

## Warning!

This bot allows control of the keyboard of your computer while it is running to allow Discord users to play a game you stream to a voice-channel. Please be cautious of what power you give strangers over your computer.

If, at any time, you feel unsafe of running this program on your computer but still would like to use it, please download a Virtual Machine and run it there.

---
## How to use

Step 1:

Make an [application][discord_dev] and copy the token of your bot to your clipboard. Then, [download master.zip][master] and unzip.

Step 2:

Install Python, [discord.py][discordpy], and [pynput][pynput] (as stated in the requirements section) with a package manager like [pip][pip], then update the [setup.py][settings] with your token you copied as well as your prefix of choice and (optional) user ID.

Step 3:

Invite the bot to a server of your choice and copy the ID of a text-channel you'd like the bot to accept inputs from. You can get this by right enabling developer mode and right clicking the text-channel's name. You'll see a button that says "Copy ID". Copy that channel's ID and add it to [setup.py][settings] where it says "textchannelid".

Step 4:

Open a command-line, go to the directory with the `bot.py`, and run `python3 bot.py` (`python bot.py` for Windows users). Enjoy~!

---
### This program is a WIP

The bot is in its beta at the moment, as there are many better ways to code it that would allow better user-input, safer environments, etc. At the moment, please be be patient for new updates. Feel free to use the code as-is, however. Thank you.

\[⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\] 99% Complete

---
## Requirements:

-[Python 3.9][python]
<br>-[discord.py][discordpy]
<br>-[pynput][pynput]

*(All requirements used visible in [bot.py][bot])*

---
If you have any issues, [contact me here][support].

You don't have to give credit to me. That's not what Github is for (in my opinion).

<a href="https://mi460.dev/github"><img src="https://img.shields.io/static/v1?label=MCMi460&amp;message=Github&amp;color=c331d4"></a>
<a href="https://mi460.dev/discord"><img src="https://discordapp.com/api/guilds/699728181841887363/embed.png"></a>

[settings]: https://github.com/MCMi460/Discord-Plays/blob/main/setup.py
[master]: https://github.com/MCMi460/Discord-Plays/archive/main.zip
[python]: https://www.python.org/downloads/
[discordpy]: https://github.com/Rapptz/discord.py/blob/master/README.rst
[bot]: https://github.com/MCMi460/Discord-Plays/blob/main/bot.py
[support]: https://mi460.dev/bugs
[pynput]: https://pypi.org/project/pynput/
[discord_dev]: https://discord.com/developers/applications
[pip]: https://pypi.org/project/pip/

<!--- You found an easter egg! Here's a cookie UwU :totallyrealcookie.png: -->
