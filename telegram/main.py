import telebot
import telegram.constant as const

bot = telebot.TeleBot(const.bot_token)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message)


bot.polling(0)