"""
Author: Mehdi Mirzaie
Session 1: Introduction Sending Messages and Files
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client
from config.settings import NAME, API_ID, API_HASH, PROXY
from typing import Coroutine

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)


# ======================= Sending Message ======================
# 1. Using bot.start() & bot.stop()
# bot.start()
# bot.send_message("me", "Hello, What's up?")
# bot.stop()

# 2. Using with
# with bot:
#     bot.send_message("@Mehdi_Mirzaieee", "Hello again!")
# bot.run()


# 3. Using async functionality
# async def send():
#     async with bot:
#         await bot.send_message("@Mehdi_Mirzaieee", "سلام مارک")
#
# bot.run(send())

# ======================= Sending document ======================

class Sender:
    def __init__(self, telegram_bot: Client):
        self.bot = telegram_bot

    async def send_video(self, chat_id, video, caption, **kwargs):
        async with self.bot:
            await self.bot.send_video(chat_id=chat_id, video=video, caption=caption, **kwargs)

    async def send_document(self, chat_id, document, caption, **kwargs):
        async with self.bot:
            await self.bot.send_document(chat_id=chat_id, document=document, caption=caption, **kwargs)

    async def send_photo(self, chat_id, photo, caption, **kwargs):
        async with self.bot:
            await self.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, **kwargs)

    async def send_audio(self, chat_id, audio, caption, **kwargs):
        async with self.bot:
            await self.bot.send_audio(chat_id=chat_id, audio=audio, caption=caption, **kwargs)

    def run(self, coroutine: Coroutine):
        print("Bot is running ...")
        self.bot.run(coroutine)


if __name__ == "__main__":
    sender = Sender(bot)

    sender.run(
        sender.send_document(chat_id='me', document='images/python.jpg', caption='Beautiful wallpaper')
    )
# @bot.on_message()
# async def hello(client, message):
#     """This form replies on each message that is sent and sends a message"""
#     await message.reply_text(f"Hi {message.from_user.mention}. How are you today?")
