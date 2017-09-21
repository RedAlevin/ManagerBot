import files.constant as const
import logics.search_image
import os
import logics.blur
import telebot


def if_my_message(message):
    message_id = message.from_user.id
    message_text = message.text
    """
    if message_id == const.admin_id:
        if message_text == "+":
            pass
        elif message_text == "-":
            pass
    else:
        pass
    """
    message_text = logics.search_image.ru_to_search(message_text)
    generate_img(message_text)



def generate_img(name):
    logics.search_image.download_img(name)
    dir = os.listdir(os.getcwd()+"/files/saves")
    for i in range(len(dir)):
        logics.blur.photo("files/saves/{}".format(dir[i]), "files/blur/{}.jpg".format(i))
        os.remove("files/saves/{}".format(dir[i]))
    print("Complited")


def push_img(bot):
    dir = os.listdir(os.getcwd() + "/files/blur")
    for i in range(len(dir)):
        with open("files/blur/{}".format(dir[i]), "rb") as img:
            bot.send_chat_action(const.admin_id, "upload_photo")
            bot.send_photo(const.admin_id, img)
            os.remove("files/blur/{}".format(dir[i]))
