from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADKAIAAmQgIVd2e584kTrkUgI")
    await message.reply_text(
        f"""Hai 👋🏻, I am Sujandra 🎵

I can play music in your group's voice call. Developed by [Hendra](https://t.me/IamYourEnemy).

Add me to your group and play music freely!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 Panduan singkat", url="https://telegra.ph/aaksnsn-06-06")
                  ],[
                    InlineKeyboardButton(
                        "Group Chat", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel Bucin", url="t.me/randfeels"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 Donasi", url="https://t.me/IamYourEnemy"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Sujandra Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Channel 🌻", url="https://t.me/AkuUserBot")
                ]
            ]
        )
   )


