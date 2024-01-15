"""
Author: Mehdi Mirzaie
Session 4 - Using raw functions to update the app info with invoke method
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

from pyrogram import Client
from pyrogram.raw.functions.channels import InviteToChannel
from pyrogram.raw.functions.account import UpdateProfile
from typing import List, Optional
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)
channel_id = ...    # Your channel ID
users = [...]       # List of username's that you want to add


async def invite_to_channel(_channel: str, _users: list):
    async with app:
        channel = await app.resolve_peer(_channel)
        users_to_add = [await app.resolve_peer(u) for u in _users]
        await app.invoke(InviteToChannel(channel=channel, users=users_to_add))


async def add_to_channel(_channel_id: str | int, _user_ids: List[str | int]) -> None:
    async with app:
        await app.add_chat_members(_channel_id, _user_ids)


async def update_info(first_name: str = None, last_name: str = None, bio: Optional = None):
    kwargs_to_update = {key: value for key, value in locals().items() if value is not None}
    async with app:
        await app.update_profile(**kwargs_to_update)


async def update_profile(first_name: str = None, last_name: str = None, about: Optional = None):
    kwargs = {key: value for key, value in locals().items() if value is not None}
    async with app:
        await app.invoke(UpdateProfile(**kwargs))


app.run(invite_to_channel(_channel=channel_id, _users=users))

# We have a lot of functionality thanks to pyrogram so you can use these functions like
# channels: DeleteHistory, DeleteChannel, LeaveChannel, JoinChannel
# account: CheckUsername
