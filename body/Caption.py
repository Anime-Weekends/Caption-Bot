from pyrogram import *
from info import *
import asyncio
from Script import script
from .database import *
import re
from pyrogram.errors import FloodWait
from pyrogram.types import *
import asyncio
import random
from pyrogram.types import InputMediaPhoto
from pyrogram.enums import ParseMode

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    welcome_text = "<i><blockquote>Wᴇʟᴄᴏᴍᴇ, ʙᴀʙʏ… ɪ’ᴠᴇ ʙᴇᴇɴ ᴄʀᴀᴠɪɴɢ ʏᴏᴜʀ ᴘʀᴇsᴇɴᴄᴇ ғᴇᴇʟs ᴘᴇʀғᴇᴄᴛ ɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ’ʀᴇ ʜᴇʀᴇ.</blockquote></i>"
    stickers = [
        "CAACAgUAAxkBAAEOXBhoCoKZ76jevKX-Vc5v5SZhCeQAAXMAAh4KAALJrhlVZygbxFWWTLw2BA"
    ]

    msg = await message.reply_text(welcome_text)
    await asyncio.sleep(0.1)
    await msg.edit_text("<b><i><pre>Sᴛᴀʀᴛɪɴɢ...</pre></i></b>")
    await asyncio.sleep(0.1)
    await msg.delete()

    await message.reply_sticker(random.choice(stickers))

    user_id = int(message.from_user.id)
    await insert(user_id)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⤬ Kɪᴅɴᴀᴘᴘ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ⤬", url="https://t.me/Auto_Caption_Elite_Bot?startchannel=true")
            ], [
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Fᴏɴᴛ", callback_data="about")
            ], [
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ", url="https://t.me/EmitingStars_Botz"),
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+HZuPVe0l-F1mM2Jl")
            ]
        ]
    )

    await message.reply_photo(
        photo=SILICON_PIC,
        caption=f"<b><blockquote>♥️ Hᴇʟʟᴏ {message.from_user.mention} !</blockquote>\n"
                f"<blockquote>ɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. "
                f"Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>\n"
                f"<blockquote>Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ » <a href='https://t.me/EmitingStars_Botz'>Eᴍɪᴛɪɴɢ sᴛᴀʀs</a></blockquote></b>",
        reply_markup=keyboard
    )
    
# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["total_users"]))
async def all_db_users_here(client,message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    await silicon.edit(f"Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`")

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        silicon = await message.reply_text("Geting All ids from database..\n Please wait")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
        await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await silicon.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "Usᴀɢᴇ: **/set_cap 𝑌𝑜𝑢𝑟 𝑐𝑎𝑝𝑡𝑖𝑜𝑛 𝑈𝑠𝑒 <code>{file_name}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑁𝑎𝑚𝑒.\n\n𝑈𝑠𝑒<code>{file_size}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑆𝑖𝑧𝑒/n/n✓ 𝑀𝑎𝑦 𝐵𝑒 𝑁𝑜𝑤 𝑌𝑜𝑢 𝑎𝑟𝑒 𝑐𝑙𝑒𝑎𝑟 💫**"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Your New Caption: {caption}")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is: {caption}")
        
# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ... Dᴇʟᴇᴛᴇᴅ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Nᴏᴡ I ᴀᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ </i></b>")
    except Exception as e:
        e_val = await msg.replay(f"ERR I GOT: {e}")
        await asyncio.sleep(5)
        await e_val.delete()
        return

def extract_language(default_caption):
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Kannada|Hin)\b'#Contribute More Language If You Have
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    if not languages:
        return "Hindi-English"
    return ", ".join(sorted(languages, key=str.lower))

def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

@Client.on_message(filters.channel)
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = DEF_CAP.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return

# Size conversion function
def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  # Changed the condition to stop at the last unit
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

# ========================================                               
#             𝗦𝗧𝗔𝗥𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗    
#                                        
#            === PrinceRexy ===                                          
# ========================================

from pyrogram.types import InputMediaPhoto

@Client.on_callback_query(filters.regex(r'^start'))
async def start(bot, query):
    await query.message.edit_media(
        media=InputMediaPhoto(
            media="https://i.ibb.co/nshhg1Zp/photo-2025-02-27-10-15-04-7481728210955141136.jpg",  # Replace with your own image
            caption=script.START_TXT.format(query.from_user.mention),
            parse_mode=ParseMode.HTML
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⤬ Kɪᴅɴᴀᴘᴘ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ⤬", url="http://t.me/Auto_Caption_Elite_Bot?startchannel=true")],
                [InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                 InlineKeyboardButton("Fᴏɴᴛ", callback_data="about")],
                [InlineKeyboardButton("Uᴘᴅᴀᴛᴇ", url="https://t.me/EmitingStars_Botz"),
                 InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+HZuPVe0l-F1mM2Jl")]
            ]
        )
    )


@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    await query.message.edit_media(
        media=InputMediaPhoto(
            media="https://i.ibb.co/nM1fxK31/photo-2025-04-29-17-47-11-7498793142519332880.jpg",
            caption=script.HELP_TXT,
            parse_mode=ParseMode.HTML
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Fᴏɴᴛ', callback_data='about')],
                [InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')]
            ]
        )
    )


@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_media(
        media=InputMediaPhoto(
            media="https://i.ibb.co/nM1fxK31/photo-2025-04-29-17-47-11-7498793142519332880.jpg",  # Replace with your own image
            caption=script.ABOUT_TXT,
            parse_mode=ParseMode.HTML
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='help')],
                [InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')]
            ]
        )
    )
