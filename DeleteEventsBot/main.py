from pyrogram import Client, filters


# Delete Service Messages
@Client.on_message(filters.group & filters.service)
async def delete_events(bot, msg):
    try:
        chat_member = await bot.get_chat_member(msg.chat.id, "self")
    except Exception:  # Like kicked, etc.
        return
    if chat_member.status == "administrator":
        if chat_member.can_delete_messages:
            await msg.delete()
        else:
            await msg.reply(
                "I'm surely admin, but I don't have 'Delete Messages' permission !!!"
            )
    else:
        await msg.reply(
            "I'm not admin, so I can't delete messages. \n\nMake me admin or kick me outta here."
        )
