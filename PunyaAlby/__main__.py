# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import importlib

from pyrogram import idle
from uvloop import install
from config import BOT_VER, CMD_HANDLER
from PunyaAlby import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from PunyaAlby.helpers.misc import create_botlog, git, heroku

MSG_ON = """
**ALBY-PYROBOT DIAKTIFKAN**๐
      (\๏ธต/) 
ใโซบ( โขแบโข)โซน 
โโโช โโโโโโโ
โ  **Userbot Version -** `{}`
โ  **Ketik** `{}alby` **untuk Mengecheck Bot**
โโโโโโโโโโ
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
    LOGGER("PunyaAlby").info(f"ALBY-PYROBOT v{BOT_VER} [๐ฅ BERHASIL DIAKTIFKAN! ๐ฅ]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    if bot1 and str(BOTLOG_CHATID).startswith("-100"):
        bot1.me = await bot1.get_me()
        chat = await bot1.get_chat(BOTLOG_CHATID)
        desc = "GROUP LOGS UNTUK ALBY-PYROBOT.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\nโจ Powered By ~ @ruangdiskusikami โจ"
        lolo = f"LOGS FOR {bot1.me.first_name}"
        if chat.description != desc:
            await bot1.set_chat_description(BOTLOG_CHATID, desc)
        if chat.title != lolo:
            await bot1.set_chat_title(BOTLOG_CHATID, lolo)
        await bot1.set_chat_photo(BOTLOG_CHATID, photo="PunyaAlby/helpers/pyroby.jpg")
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
