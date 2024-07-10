from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ 𝗥𝗘𝗣𝗢 𝗟𝗘𝗡𝗘 𝗞𝗘 𝗟𝗜𝗬𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗝𝗢𝗜𝗡 𝗞𝗔𝗥𝗢
𝗔𝗨𝗥 𝗗𝗜𝗦𝗖𝗨𝗦𝗦𝗜𝗢𝗡 𝗚𝗥𝗢𝗨𝗣 𝗠𝗘 𝗥𝗘𝗣𝗢 𝗧𝗬𝗣𝗘 𝗞𝗔𝗥𝗢 
𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 👉🏻 @Stylish_Bio_Dp_0 ✰
 
 ►  𝗜𝗙 𝗔𝗡𝗬 𝗣𝗥𝗢𝗕𝗟𝗘𝗠 𝗢𝗥 𝗤𝗨𝗘𝗥𝗬 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗧𝗢 𝗠𝗬 𝗢𝗪𝗡𝗘𝗥 👉🏻 @Niksonfire
**"""




@app.on_message(filters.command("Nick"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘LP⚡", url="https://t.me/Stylish_Bio_Dp_0"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥🥀", url="https://t.me/niksonfire"),
          ],
               

           
            ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/dda08a0a6f2e8282f8332.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("Nick", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/Niksonfire")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""THANKS | [𝖦𝖱𝖮𝖴𝖯](https://t.me/Stylish_Bio_Dp_0)
| THANKS FOR USING ME ⚡ |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


