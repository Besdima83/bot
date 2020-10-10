import settings
import requests  # pip install requests
import json
from requests.exceptions import HTTPError


class TelegramBot:

    @staticmethod
    def get_new_messages_as_json(update_id):
        try:
            response = requests.get(url=settings.TELEGRAM_GET_NEW_MESSAGE_URL, params={'offset': update_id})
            return json.loads(response.text)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            return "error"
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            return "error"

    @staticmethod
    def post_message(chat_id, text):
        try:
            response = requests.post(url=settings.TELEGRAM_POST_MESSAGE_URL, params={'chat_id': chat_id, 'text': text})
            return json.loads(response.text)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            return "error"
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            return "error"
