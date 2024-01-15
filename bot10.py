"""
Author: Mehdi Mirzaie
Session 10 - Forward messages of specific channel by its username. upload download using saved messages
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client, filters
from pyrogram.types import Message, Document
from config.settings import NAME, API_ID, API_HASH, PROXY
from uuid import uuid4

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)

CHANNEL_USERNAME = ...


def is_username(text: str):
    return text.startswith('@')


def generate_file_name(document: Document):
    return f"{uuid4().hex}.{document.file_name.split('.')[-1]}"


def filter_channel(channel_username: str):
    channel_username = channel_username.replace('@', '')

    async def function(_, __, m: Message):
        return bool(m.chat.username == channel_username)

    return filters.create(function)


@app.on_message(filters.channel & filter_channel(CHANNEL_USERNAME))
async def forward_to_saved_messages(client, msg: Message):
    print(" message received ".center(100, '-'))
    await msg.forward('me', )
    print(" message forwarded to saved messages ".center(100, '-'))


@app.on_message(filters.chat('me') & filters.document)
async def upload_file(client, msg: Message):
    file_name = generate_file_name(msg.document)
    await app.download_media(msg, file_name)
    print(" Document has been downloaded ".center(100, '-'))
    response = f'''
Your file has been uploaded successfully.
Here is your download link https://site.com/{file_name}'''
    await msg.reply(response)
    print(" Upload verification has been sent ".center(100, '-'))


@app.on_message(filters.chat('me') & filters.text)
async def join_chat(client, msg: Message):
    if is_username(msg.text):
        try:
            await app.join_chat(msg.text)
            await msg.reply(" Joined successfully! ")
            print(f" Joined {msg.text} ".center(100, '-'))

        except Exception as e:
            await msg.reply(" Something went wrong! ")
            print(f" Could not join to {msg.text} ".center(100, '-'))
            print(e)


if __name__ == "__main__":
    app.run()
