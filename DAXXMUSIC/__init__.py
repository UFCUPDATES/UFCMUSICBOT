from UFCMUSIC.core.bot import ritik
from UFCMUSIC.core.dir import dirr
from UFCMUSIC.core.git import git
from UFCMUSIC.core.userbot import Userbot
from UFCMUSIC.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ritik()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
