import environ
from pathlib import Path

import telebot
from telebot.types import BotCommand


BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

BOT_TOKEN = env.str("BOT_TOKEN")
URL_SEND_MESSAGE = env.str("URL_SEND_MESSAGE")

bot = telebot.TeleBot(BOT_TOKEN)


def setup_bot_commands(bot):
    bot_commands = [
        BotCommand("/date", "Перегляд вільних дат"),
        BotCommand("/location", "Показати локацію Fazenda"),
        BotCommand("/links", "Показати посилання на соц. мережі"),
        BotCommand("/help", "Показати список команд"),

    ]
    bot.set_my_commands(bot_commands)


@bot.message_handler(commands=['help'])
def help_command(message):
    commands = [
        "/date - Перегляд вільних дат для бронювання",
        "/location - Показати локацію Fazenda",
        "/links - Показати посилання на соц. мережі",
        "/help - Показати список команд",
    ]
    bot.reply_to(message, "Доступні команди:\n" + "\n".join(commands))


@bot.message_handler(commands=['date'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Тут ти зможеш подивитись час доступний до бронювання Фазенди:\n"
        "https://skladok.store/kalendar-mahnit-yibanyi-kalendar-rozmir-a3-29kh42-sm/\n"
        "*посилання на gmail календар*"
    )


@bot.message_handler(commands=['location'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Як доїхати:\n"
        "*посилання на маршрут*\n"
        "Місце для відпочинку: с. Деремезна, Київська обл\n"
        "maps.app.goo.gl/p6jptwfyoX1H9Myt6"
    )


@bot.message_handler(commands=['links'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Instagram Fazenda:\nhttps://www.instagram.com/fazenda_residence/\n"
        "Створення Fazenda:\nhttps://www.youtube.com/watch?v=CQQ_QGXrJkc&list=PL0XAVu0yP0SZyZ5Vhygh87rK7h_qAZeMG\n"
        "Instagram Марини:\nhttps://www.instagram.com/maryna.lytvyn/"
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Будь ласка, використайте команду /help для перегляду доступних команд.')


setup_bot_commands(bot)
bot.infinity_polling()
