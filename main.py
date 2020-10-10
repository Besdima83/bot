from telegram.telegrambot import TelegramBot
import time
# Точка входа
if __name__ == '__main__':
    update_id = 0
    count = 0
    while 1 < 2: # Бесконечный цыкл
        new_messages_as_json = TelegramBot.get_new_messages_as_json(update_id + 1)
        if new_messages_as_json != "error":
            if "result" in new_messages_as_json:
                results = new_messages_as_json["result"]
                if len(results) > 0:
                    for result in results:
                        text = ""
                        chat_id = 0
                        chat_user_name = ""

                        if "update_id" in result:
                            update_id = max(update_id, result["update_id"])

                        if "message" in result:
                            message = result["message"]

                            if "text" in message:
                                text = message["text"]

                            if "chat" in message:
                                chat = message["chat"]
                                if "id" in chat:
                                    chat_id = chat["id"]
                                if "first_name" in chat:
                                    chat_user_name = chat["first_name"]
                        m = 1
                        for i in range(m):
                            count += 1
                            print(f"Сообщение от {chat_user_name}: \"{text}\", чат ID: {chat_id}")
                            post_message_as_json = TelegramBot.post_message(chat_id, f"Ответочка{count}")
                            print(post_message_as_json)
                            if post_message_as_json != "error":
                                if "ok" in post_message_as_json:
                                    if post_message_as_json["ok"]:
                                        print(f"Ответочка ушла -> {chat_user_name}")
                                    else:
                                        print("Oops... Ответочка не ушла")
                                else:
                                    print("...")  # Новых сообщений нет
                            else:
                                print("Oops... Ответочка не ушла")
        else:
            print("Oops...")

        time.sleep(1)
