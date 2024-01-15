"""
Author: Mehdi Mirzaie
Session 7 - In saved messages, forward a message to groups that you are joined when you reply on that message
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client, filters
from pyrogram.types import Message, Dialog
from pyrogram.enums.chat_type import ChatType
from typing import AsyncGenerator
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, api_id=API_ID, api_hash=API_HASH, proxy=PROXY)


def validate_telegram_link(link: str) -> str:
    return link.replace('https://t.me/', '@')


async def get_super_groups(cli: Client, _limit: int = 0) -> AsyncGenerator[Dialog, None]:
    async for dialog in cli.get_dialogs(_limit):
        if dialog.chat.type == ChatType.SUPERGROUP:
            yield dialog


@app.on_message(filters.text and filters.chat('me'))
async def send_banner(client, msg: Message):
    chat_id = validate_telegram_link(msg.text)

    try:
        await app.join_chat(chat_id) if chat_id.startswith('@') else ...
    except Exception as e:
        await app.send_message('me', 'Something went wrong.')
        print(e)

    if msg.reply_to_message_id and msg.text.lower() == 'send':
        async for dialog in get_super_groups(app):
            print(dialog.chat.title)
            # forwards that message you replied on
            # await app.forward_messages(dialog.chat.id, 'me', msg.reply_to_message_id)


if __name__ == '__main__':
    app.run()
