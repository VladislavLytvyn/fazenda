import environ
from pathlib import Path

import telebot


BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

BOT_TOKEN = env.str("BOT_TOKEN")
URL_SEND_MESSAGE = env.str("URL_SEND_MESSAGE")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Я бот, який буде надсилати вам повідомлення.")


bot.infinity_polling()
