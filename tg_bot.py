import telebot
import requests

bot = telebot.TeleBot('sosi')


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.from_user.id
    username = message.from_user.username

    site_user_id = message.text.split(" ")[1] if (len(message.text.split(" ")) > 1) else None

    if site_user_id is None:
        bot.send_message(chat_id, "Команда не валидна. Перейди по ссылке "
                                  "из личного кабинета learn-together.xyz, "
                                  "чтобы задать username своего телеграмма")

    handle_add_nickname(site_user_id, username, chat_id)


def handle_add_nickname(user_id, telegram_name, chat_id):
    url = "https://learn-together.xyz/api/user/addTelegramData"
    data = {
        "UserId": user_id,
        "TelegramName": telegram_name,
        "TelegramChatId": chat_id
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        bot.send_message(chat_id, f"Ваш id {user_id}")
        bot.send_message(chat_id, f"Офигеть, ты же тот самый "
                                  f"{telegram_name}??? "
                                  f"Добавил твой ник)")
    else:
        bot.send_message(chat_id, f"Ошибка! Повторно перейди по ссылке из "
                                  f"личного кабинета")


bot.polling(none_stop=True, interval=1)
