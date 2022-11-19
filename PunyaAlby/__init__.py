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
import time
from os import listdir, mkdir

import heroku3
from aiohttp import ClientSession
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from rich.console import Console
from rich.table import Table
import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict

from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client
from pytgcalls import GroupCallFactory

from config import (
    API_HASH,
    API_ID,
    BOTLOG_CHATID,
    DB_URL,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    SUDO_USERS,
)

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


if (
    not STRING_SESSION1
    and not STRING_SESSION2
    and not STRING_SESSION3
    and not STRING_SESSION4
    and not STRING_SESSION5
):
    LOGGER(__name__).error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    LOGGER(__name__).error("No API_ID Found! Exiting!")
    sys.exit()

if not API_HASH:
    LOGGER(__name__).error("No API_HASH Found! Exiting!")
    sys.exit()

if BOTLOG_CHATID:
    BOTLOG_CHATID = BOTLOG_CHATID
else:
    BOTLOG_CHATID = "me"

LOOP = asyncio.get_event_loop()

trl = Translator()

aiosession = ClientSession()

CMD_HELP = {}

scheduler = AsyncIOScheduler()

StartTime = time.time()

START_TIME = datetime.now()

TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}


### testing
from PunyaAlby.config import BOTLOG_CHATID, STRING_SESSION1, UPSTREAM_BRANCH, UPSTREAM_REPO
from PunyaAlby.clientbot import client, robot
from PunyaAlby.utils.times import time_to_seconds
from PunyaAlby.utils.tasks import install_requirements


loop = asyncio.get_event_loop()
console = Console()


### Heroku Shit
UPSTREAM_BRANCH = UPSTREAM_BRANCH
UPSTREAM_REPO = UPSTREAM_REPO

### Modules
MOD_LOAD = []
MOD_NOLOAD = []

### Boot Time
boottime = time.time()

### Clients
aiohttpsession = ClientSession()
robot = robot

### Config
BOTLOG_CHATID = BOTLOG_CHATID

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Assistant Info
ASSIDS = []
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""
random_assistant = []


async def initiate_bot():
    global ASSIDS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
    global Heroku_cli, Heroku_app
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "ALBY PYROBOT : Best Ever Userbot"
    )
    console.print(header)
    with console.status(
        "[magenta] ALBY PYROBOT Booting...",
    ) as status:
        console.print("┌ [red]Booting Up The Bot Clients...\n")
        await robot.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The User Client...")
        if STRING_SESSION1 != "None":
            random_assistant.append(1)
            console.print("├ [yellow]Booted User Client")
        
        console.print("└ [green]All Client Bots Booted Successfully!")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("\n┌ [red]Loading Clients Information...")
        getme = await robot.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        if STRING_SESSION1 != "None":
            getme = await client.get_me()
            ASSID = getme.id
            ASSIDS.append(ASSID)
            ASSNAME = (
                f"{getme.first_name} {getme.last_name}"
                if getme.last_name
                else getme.first_name
            )
            ASSUSERNAME = getme.username
            ASSMENTION = getme.mention
        console.print("└ [green]Loaded Clients Information!")
        try:
            repo = Repo()
        except GitCommandError:
            console.print("┌ [red] Checking Git Updates!")
            console.print("└ [red]Git Command Error\n")
            return
        except InvalidGitRepositoryError:
            console.print("┌ [red] Checking Git Updates!")
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(UPSTREAM_BRANCH, origin.refs[UPSTREAM_BRANCH])
            repo.heads[UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[UPSTREAM_BRANCH]
            )
            repo.heads[UPSTREAM_BRANCH].checkout(True)
            try:
                repo.create_remote("origin", UPSTREAM_REPO)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(UPSTREAM_BRANCH)
            try:
                nrs.pull(UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            await install_requirements(
                "pip3 install --no-cache-dir -r Installer"
            )
            console.print("└ [red]Git Client Update Completed\n")


loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
