from os import environ, getenv
import re
import os
from typing import List

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6429532957"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://i.ibb.co/nshhg1Zp/photo-2025-02-27-10-15-04-7481728210955141136.jpg")
API_ID = int(getenv("API_ID", "28744454"))
API_HASH = str(getenv("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7733520743:AAG0HLnBXKQEqz9RC2v-MaSM88qi9UeVMJs"))
IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "EmitingStars_Botz").split())) # Add Multiple channel id
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://NewData:NewData@cluster0.bctax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
