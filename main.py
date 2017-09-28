import telebot
import files.constant as const
import logics.telegram_function as function

bot = telebot.TeleBot(const.bot_token)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.from_user.id, "I searching image!")
    print(message.text)

    bot.send_message(message.from_user.id, "Searching - completed.\n I generating image!")
    function.generate_img(message.text, message.from_user.id)

    bot.send_message(message.from_user.id, "Generating - completed.\n I pushing image!")
    function.push_all(bot, message)
    print("Push")

bot.polling(0)