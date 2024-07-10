from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬", url=f"https://t.me/Stylish_Bio_Dp_0"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗞𝗜𝗗𝗡𝗔𝗣 𝗠𝗘 🫣",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="👉🏻𝗢𝗪𝗡𝗘𝗥🥀", url=f"https://t.me/Niksonfire"),
            InlineKeyboardButton(text="⚡𝗨𝗣𝗗𝗔𝗧𝗘𝗦⚡", url=f"https://t.me/Stylish_Bio_Dp_0"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons
