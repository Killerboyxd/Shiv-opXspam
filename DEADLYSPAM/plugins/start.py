
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ff8228a476d1fc73ab8fe.jpg"


Deadly_Button = [
        [
        Button.url("🌼 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🌼", "https://t.me/do_dil_ek_jaan143"),
        Button.url("🌼 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🌼", "https://t.me/RONNY_KI_DUNIYA")
        ],
        [
        Button.url(" 😈 𝗢𝗪𝗡𝗘𝗥 😈 ", "https://t.me/ll_SABKA_BHAI_KILLER_ll"),
        Button.url(" 🐣 𝗙𝗘𝗘𝗟𝗜𝗡𝗚𝗦 🥂 ", "https://t.me/ll_SABKA_BHAI_KILLER_ll")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[🍷 𝗗𝗛𝗜𝗠𝗔𝗡 🍷](tg://user?id={5760312424})"
        DEADLY_ON = f"""
𝗛𝗘𝗬 {mention},
𝗧𝗛𝗜𝗦 𝗜𝗦 𝗦𝗛𝗜𝗩 𝗦𝗣𝗔𝗠𝗕𝗢𝗧 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬:- {creator}!

🥵 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥:- {myOwner}

⚙ 𝗖𝗢𝗗𝗘 𝗖𝗥𝗘𝗔𝗧𝗢𝗥:- {creator}

❤️‍🩹 𝗖𝗟𝗜𝗖𝗞 𝗕𝗘𝗟𝗢𝗪 𝗧𝗢 𝗔𝗖𝗖𝗘𝗦𝗦 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 , 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗔𝗡𝗗 𝗢𝗪𝗡𝗘𝗥!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
