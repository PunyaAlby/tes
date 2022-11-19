import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "1020199"))
API_HASH = getenv("API_HASH", "3672885f650c19ef18d53548bb641d5f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", ""))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", f"https://PunyaAlby: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@https://github.com/PunyaAlby/tepy")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
