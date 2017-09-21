import telebot
import files.constant as const
import logics.telegram_function as function

bot = telebot.TeleBot(const.bot_token)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    function.generate_img()


bot.polling(0)