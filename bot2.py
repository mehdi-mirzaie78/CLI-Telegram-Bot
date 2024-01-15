"""
Author: Mehdi Mirzaie
Session 1: Introduction Sending Messages and Files
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client
from pyrogram.types import Message
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)


@app.on_message()
async def test(client: Client, msg: Message):
    user_text = msg.text
    user_chat_id = msg.chat.id
    if user_text == 'سلام':
        await msg.reply('سلام چطوری؟')
    elif user_text == 'عکس':
        await msg.reply_photo('img/python.jpg', caption='Wallpaper')
    elif user_text == 'خوبی':
        await msg.reply('ممنون خوبم تو خوبی؟')
    else:
        await msg.reply('WTF?🤣')


app.run()
