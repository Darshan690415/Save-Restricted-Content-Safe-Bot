# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25352517"))
API_HASH = getenv("API_HASH", "2b7e6cf7752c3af91f958d67793a3e0b")
BOT_TOKEN = getenv("BOT_TOKEN", "7726613356:AAHOgz4KscbBr0uwiTbtx7CbPnYqI5txOmw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7360968885").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://darshanmalkiya5:45674567uU@@cluster0.dhqmz6n.mongodb.net/")
LOG_GROUP = getenv("LOG_GROUP", "-4522794360")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002374676510"))
