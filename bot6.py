"""
Author: Mehdi Mirzaie
Session 6 - Joining to a public group & Get users & Add members to channel
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)

CHAT_ID = ...        # Group CHAT ID that you want to join and get its users


class Utils:
    CHAT_ID = CHAT_ID

    def __init__(self, bot: Client):
        self.bot = bot

    async def join_group(self, chat_id: str) -> None:
        await self.bot.join_chat(chat_id=chat_id)

    async def get_members(self, chat_id: str) -> list:
        messages = self.bot.get_chat_history(chat_id=chat_id, limit=10)
        users = [msg.from_user.id async for msg in messages]
        return users

    async def add_users(self, user_ids: list, chat_id: str = None) -> None:
        if chat_id is None:
            chat_id = self.CHAT_ID
        await self.bot.add_chat_members(chat_id, user_ids)

    @staticmethod
    def is_username_valid(username: str) -> bool:
        return True if username.startswith('@') else False


# utils instance to handle useful methods
utils = Utils(app)


@app.on_message(filters.text and filters.chat('me'))
async def add_members(client, msg: Message):
    group_chat_id = msg.text
    if utils.is_username_valid(group_chat_id):
        await utils.join_group(group_chat_id)
        users = await utils.get_members(group_chat_id)
        await utils.add_users(users)
    else:
        await msg.reply('Error Processing your message. Invalid link. Send your link like this `@sample`')


if __name__ == '__main__':
    print(' bot6 started... '.center(100, '*'))
    app.run()
