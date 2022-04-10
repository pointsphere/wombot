"""Bot configuration variables."""
from os import environ, getenv, path

#import pytz
#from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(BASE_DIR, ".env"))

# General config
ENVIRONMENT = getenv("ENVIRONMENT")
#TIMEZONE_US_EASTERN = pytz.timezone("America/New_York")

# Chatango credentials
CHATANGO_USERS = {
    "wombot": {
        "USERNAME": getenv("CHATANGO_BOT_USERNAME"),
        "PASSWORD": getenv("CHATANGO_BOT_PASSWORD"),
        
    },
}

# Known Chatango bot usernames
CHATANGO_BOTS = [
    "wombot",
    
]

# Chatango rooms
#CHATANGO_TEST_ROOM = getenv("CHATANGO_TEST_ROOM")
#CHATANGO_TEST_ROOM = getenv("CHATANGO_TEST_ROOM")

# Chatango users with additional features
CHATANGO_SPECIAL_USERS = getenv("CHATANGO_SPECIAL_USERS")
if CHATANGO_SPECIAL_USERS:
    CHATANGO_SPECIAL_USERS = CHATANGO_SPECIAL_USERS.split(",")
