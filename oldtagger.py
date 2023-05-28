import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events, Button
from telethon.tl.custom import Button
import random # pip install random
from random import randint
import configparser
from asyncio import sleep
from telethon import events
from Config import Config 
# Pyrogram----------------------------------------------------------------------------------------------------
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)



logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = ["5134595693"]
LOG_QRUP = -1001913078116



#-#-#-# Pyrogram Başlanğıc #-#-#-#
rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@rehim.on_message(filters.command("infoid") & filters.user(SUDO_USERS))
async def get_id(client, message):
    try:

        if (not message.reply_to_message) and (message.chat):
            await message.reply(f"İstdifadəçi {message.from_user.first_name}'idisi <code>{message.from_user.id }</code>.\nChat id: <code>{message.chat.id}</code>.") 

        elif not message.reply_to_message:
            await message.reply(f"İstdifadəçi {message.from_user.first_name}'ID <code>{message.from_user.id }</code>.") 

        elif message.reply_to_message.forward_from_chat:
            await message.reply(f"Yönləndirilmiş Kanal {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title} İdisi <code>{message.reply_to_message.forward_from_chat.id}</code>.") 

        elif message.reply_to_message.forward_from:
            await message.reply(f"Yönləndirilmiş İstdifadəçi, {message.reply_to_message.forward_from.first_name} İdisi <code>{message.reply_to_message.forward_from.id   }</code>.")

        elif message.reply_to_message.forward_sender_name:
            await message.reply("Üzr istəyirik, məxfilik parametrlərinə görə yönləndirilmiş istifadəçi ID-sini əldə edə bilməzsiniz")

        else:
            await message.reply(f"İstdifadəçi {message.reply_to_message.from_user.first_name}'İdisi <code>{message.reply_to_message.from_user.id}</code>.")   

    except Exception:
            await message.reply("ID-ni əldə edərkən xəta baş verdi.")



# ---------------------  TELETHON TEAMABASOF#

@abasov.on(events.NewMessage(incoming=True, from_users=SUDO_USERS, pattern="^[./!]depo ?(.*)|^[./!]yolla ?(.*)"))
async def kopya(event):
    await event.delete()
    mesaj = await event.get_reply_message()
    if not mesaj:
        await event.reply("Bir şeyə yanıt verdə 🤦‍♂️")
        return
    await mesaj.reply("⚡️ **Bu mesajı log qrupuna atdım**")
    await event.abasov.send_message(LOG_QRUP, mesaj)





############## DEĞİŞKENLER ##############



abasov = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)




#edalet_22 terefinden elave edildi
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  



print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
rehim.start()
abasov.run_until_disconnected()
