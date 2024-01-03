from pyrogram import *
from config import API_ID, API_HASH


 

@Bot.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        Bot = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "TheFunkyFox"})
        await Bot.start()
        await msg.reply(f"Your Client Has Been Successfully ✅ !\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")







