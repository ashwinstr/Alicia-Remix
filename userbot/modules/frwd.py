"""Enable Seen Counter in any message,
to know how many users have seen your message
Syntax: .frwd as reply to any message"""
from ..utils import admin_cmd
from userbot.events import register


@register(incoming=True, outgoing=True, disable_edited=True)
async def _(event):
    if event.fwd_from:
        return
    if PRIVATE_CHANNEL_BOT_API_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_CHANNEL_BOT_API_ID` for this plugin to work"
        )
        return
    try:
        e = await event.client.get_entity(int(PRIVATE_CHANNEL_BOT_API_ID))
    except Exception as e:
        LOGS.warn(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await event.client.forward_messages(e, re_message, silent=True)
        await event.client.forward_messages(event.chat_id, fwd_message)
        await event.delete()