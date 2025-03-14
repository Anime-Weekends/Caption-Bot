import os

class script(object):

    START_TXT = """<b>🍁 Hᴇʟʟᴏ {} !\n
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/EmitingStars_Botz'>Eᴍɪᴛɪɴɢ sᴛᴀʀs </a></b>
"""

    HELP_TXT = """<blockquote>❗ 𝗔𝗹𝗲𝗿𝘁 ❗</blockquote>
<blockquote expandable>• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

•> /set_cap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
•> /del_cap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ</blockquote>

<blockquote expandable>𝗙𝗢𝗥𝗠𝗔𝗧</blockquote>
<blockquote expandable>`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ Nᴀᴍᴇ
`{year}` = Yᴇᴀʀ Oғ Fɪʟᴇ
`{default_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ.

Eg:- `/set_cap
{file_name}

⚙️ Size » {file_size}</blockquote>
"""

    ABOUT_TXT = """<b><blockquote expandable>𝗔𝗕𝗢𝗨𝗧 𝗖𝗔𝗣𝗧𝗜𝗢𝗡 𝗙𝗢𝗡𝗧</blockquote>
<blockquote>➢ ʙᴏʟᴅ ᴛᴇxᴛ

☞ <b><code>{filename}</code></b>

➢ sᴘᴏɪʟᴇʀ ᴛᴇxᴛ

☞ <spoiler><code>{filename}</code></spoiler>

➢ ʙʟᴏᴄᴋǫᴜᴏᴛᴇ ᴛᴇxᴛ

☞ <blockquote>{filename}</blockquote>

➢ ʙʟᴏᴄᴋǫᴜᴏᴛᴇ ᴇxᴘᴀɴᴅᴇᴅ ᴛᴇxᴛ

☞ <blockquote expandable>{filename}</blockquote>

➢ ɪᴛᴀʟɪᴄ ᴛᴇxᴛ

☞ <i>{filename}</i>

➢ ᴜɴᴅᴇʀʟɪɴᴇ ᴛᴇxᴛ

☞ <u>{filename}</u>

➢ sᴛʀɪᴋᴇ ᴛᴇxᴛ

☞ <s>{filename}</s>

➢ ᴍᴏɴᴏ ᴛᴇxᴛ

☞ <code>{filename}</code>

➢ ʜʏᴘᴇʟɪɴᴋ ᴛᴇxᴛ

☞ <a href="https://t.me/Anime_Weekends">{filename}</a>

➢ ᴘʀᴇ ᴛᴇxᴛ

☞ <pre>
{file_name}
</pre></blockquote></b>"""
