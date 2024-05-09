from pyrogram import Client
from bot.config import Telegram

StreamBot = Client(
    name='bot',
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    bot_token=Telegram.BOT_TOKEN,
    sleep_threshold=Telegram.SLEEP_THRESHOLD,
)
UserBot = Client(
    name='user',
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    session_string=Telegram.SESSION_STRING,
    sleep_threshold=Telegram.SLEEP_THRESHOLD,
    no_updates=True,
    in_memory=True,
)


multi_clients = {}
work_loads = {}