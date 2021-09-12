from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/phoenix_empire")],
        [InlineKeyboardButton(
            "ʀᴇᴘᴏʀᴛ ʙᴜɢs ", url="https://t.me/heyaaman")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
