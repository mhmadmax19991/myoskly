import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Music Krizy")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "M_X_FF")
ALIVE_NAME = getenv("ALIVE_NAME", "Music Krizy")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "M_X_FFF")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rq_ok")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/ac76cf32f59bca56ac299.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rone1233/Music_Rony")
IMG_1 = getenv("IMG_1", "https://telegra.ph//file/ac76cf32f59bca56ac299.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/ac76cf32f59bca56ac299.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/ac76cf32f59bca56ac299.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph//file/ac76cf32f59bca56ac299.jpg")
