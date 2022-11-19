# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from rich.console import Console
from rich.table import Table

import importlib

from pyrogram import idle
from uvloop import install
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

###
from PunyaAlby.config import BOTLOG_CHATID, STRING_SESSION1
from PunyaAlby import client, robot, ASSID, ASSNAME, BOT_ID, BOT_NAME
from PunyaAlby.helpers.filters import command
from PunyaAlby.helpers.decorators import errors
from PunyaAlby.modules import ALL_MODULES
from PunyaAlby.utils.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}

async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "PunyaAlby.modules." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green] 🔥 ALBY PYROBOT Started ✨\n"
    )
    try:
        await robot.send_message(
            BOTLOG_CHATID,
            "<b> 🔥 ALBY PYROBOT is Here ✨</b>",
        )
    except Exception as e:
        print(
            "\nBot. Has Failed To Access The Log Group, Be Sure You Have Added Your Bot To Your Log Channel And Promoted As Admin❗"
        )
        console.print(f"\n[red] Stopping Bot")
        return
    a = await robot.get_chat_member(BOTLOG_CHATID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot As Admin in Logger Group")
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}")
    console.print(f"├[green] ID :- {BOT_ID}")
    if STRING_SESSION1 != "None":
        try:
            await client.send_message(
                BOTLOG_CHATID, 
                MSG_ON,
            )
        except Exception as e:
            print(
                "\nUserBot Account Has Failed To Access The Log Group.❗"
            )
            console.print(f"\n[red] Stopping Bot")
            return
        try:
            await client.join_chat("ruangdiskusikami")
            await client.join_chat("ruangprojects")
        except:
            pass
        console.print(f"├[red] UserBot Started as {ASSNAME}")
        console.print(f"├[green] ID :- {ASSID}")
        console.print(f"└[red] ✅ ALBY-PYROBOT Complete 💯 ...")
        await idle()
        console.print(f"\n[red] Userbot Stopped")


home_text_pm = f"""**ʜᴇʟʟᴏ ,
ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.
I Aᴍ ᴀʟʙʏ ᴘʏʀᴏʙᴏᴛ, Aɴ Aᴅᴠᴀɴᴄᴇᴅ UsᴇʀBᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.**"""


@robot.on_message(command(["start"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ ᴀʟʙʏ ᴘʏʀᴏʙᴏᴛ » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ.
┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD› : [ᴀʟʙʏ](https://t.me/Punya_Alby)
┣★ Uᴘᴅᴀᴛᴇs ›› : [Uᴘᴅᴀᴛᴇs](https://t.me/ruangprojects)
┣★ Sᴜᴘᴘᴏʀᴛ » : [Dɪsᴄᴜs](https://t.me/ruangdiskusikami)
┗━━━━━━━━━━━━━━━━━━━┛
💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ
Yᴏᴜʀ Oᴡɴ » Gᴇɴɪᴜs Usᴇʀ Bᴏᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Dᴇᴘʟᴏʏ Aʟʙʏ Pʏʀᴏʙᴏᴛ ✨", url=f"https://github.com/PunyaAlby/ALBY-PYROBOT")
                ]
                
           ]
        ),
    )
    
    
    
@client.on_message(command(["help"]))
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await robot.send_message(BOTLOG_CHATID, text, reply_markup=keyboard)




async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...
💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
""".format(
            first_name=name
        ),
        keyboard,
    )

@client.on_callback_query(filters.regex("close"))
async def close(_, CallbackQuery):
    await CallbackQuery.message.delete()

@client.on_callback_query(filters.regex("aditya"))
async def aditya(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@client.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...
💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :** ", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ ʙᴀᴄᴋ", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 ᴄʟᴏsᴇ", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await robot.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)

if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
    loop.run_until_complete(initiate_bot())
