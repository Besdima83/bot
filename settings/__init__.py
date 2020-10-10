from settings.hidesettings import TELEGRAM_BOT_TOKEN

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/"
TELEGRAM_GET_NEW_MESSAGE_URL = f"{TELEGRAM_API_URL}getUpdates"
TELEGRAM_POST_MESSAGE_URL = f"{TELEGRAM_API_URL}sendMessage"
