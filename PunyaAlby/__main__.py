# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de


from uvloop import install
import time
import logging
import importlib
import random
import sys
import traceback
import threading
import asyncio

import pyrogram
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from PunyaAlby import app, log, Command, isCi
from PunyaAlby.modules import ALL_PLUGINS
from config import BOT_VER, CMD_HANDLER
from PunyaAlby import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from PunyaAlby.helpers.misc import create_botlog, git, heroku

MSG_ON = """
**ALBY-PYROBOT DIAKTIFKAN**📍
      (\︵/) 
　⫺( •ᆺ•)⫹ 
┏━∪ ━━━━━━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alby` **untuk Mengecheck Bot**
┗━━━━━━━━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ruangdiskusikami")
            await bot.join_chat("ruangprojects")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("PunyaAlby").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("PunyaAlby").info(f"ALBY-PYROBOT v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    if bot1 and str(BOTLOG_CHATID).startswith("-100"):
        bot1.me = await bot1.get_me()
        chat = await bot1.get_chat(BOTLOG_CHATID)
        desc = "GROUP LOGS UNTUK ALBY-PYROBOT.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ @ruangdiskusikami ✨"
        lolo = f"LOGS FOR {bot1.me.first_name}"
        if chat.description != desc:
            await bot1.set_chat_description(BOTLOG_CHATID, desc)
        if chat.title != lolo:
            await bot1.set_chat_title(BOTLOG_CHATID, lolo)
        await bot1.set_chat_photo(BOTLOG_CHATID, photo="PunyaAlby/helpers/pyroby.jpg")
    await idle()
    await aiosession.close()

BOT_RUNTIME = 0
HELP_COMMANDS = {}


loop = asyncio.get_event_loop()

async def get_runtime():
	return BOT_RUNTIME

async def start_bot():
	await app.start()
	for module in ALL_PLUGINS:
		imported_module = importlib.import_module("PunyaAlby.modules." + module)
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			imported_module.__MODULE__ = imported_module.__MODULE__
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			if not imported_module.__MODULE__.lower() in HELP_COMMANDS:
				HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
			else:
				raise Exception("Can't have two modules with the same name! Please change one")
		if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
			HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
	log.info("-----------------------")
	log.info("Plugins loaded: " + str(ALL_PLUGINS))
	log.info("-----------------------")
	log.info("Bot run successfully!")

	if isCi:
		log.info("Test is passed!")
	else:
		await idle()

if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    install()
    git()
    heroku()
    BOT_RUNTIME = int(time.time())
    LOOP.run_until_complete(main())
    loop.run_until_complete(start_bot())
