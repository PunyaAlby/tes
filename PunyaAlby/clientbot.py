from pyrogram import Client as Bot
from PunyaAlby.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION1


client = Bot(STRING_SESSION1, API_ID, API_HASH, plugins=dict(root="PunyaAlby.modules"))
robot = Bot(":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN)
