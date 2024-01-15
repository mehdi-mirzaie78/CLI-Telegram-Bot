"""
Author: Mehdi Mirzaie
Session 3 - Filters & Download
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import text, photo, document, \
    sticker, me, channel, private, group
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)


# @app.on_message(filters=sticker)
# async def wait_to_send(client, msg: Message):
#     first_name = msg.chat.first_name
#     user_text = msg.text
#     user_chat_id = msg.chat.id
#     await msg.reply(f"You sent a sticker {first_name}.")

@app.on_message()
async def test_download(client, msg: Message):
    user = msg.chat.first_name
    await app.download_media(msg)
    await app.send_message(
        msg.chat.id,
        f"""
Dear {user}, your file has been uploaded successfully.
Here is your download link: 
http://site.com/downloads/{msg.document.file_name}
""")


app.run()
