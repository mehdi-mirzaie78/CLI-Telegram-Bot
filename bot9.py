"""
Author: Mehdi Mirzaie
Session 9 - Forward messages of a specific channel by its username
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client, filters
from config.settings import NAME, API_ID, API_HASH, PROXY
from pyrogram.types import Message

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)
# Your channel's username without '@'
CHANNEL_USERNAME = ...


# Function for filtering channel messages based on its username
async def channel_filter_username(_, __, m: Message):
    return bool(m.chat.username == CHANNEL_USERNAME)


# Custom filter to get messages of specified channel
channel_username = filters.create(channel_filter_username)


@app.on_message(filters.channel & channel_username)
async def forward_messages(client, msg: Message):
    print(" message received ".center(100, '-'))
    await msg.forward('me')
    print(" message forwarded to saved messages ".center(100, '-'))


if __name__ == "__main__":
    app.run()
