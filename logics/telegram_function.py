import files.constant as const
import logics.search_image
import os
import logics.blur
import time


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
    print(message_text)
    message_text = logics.search_image.ru_to_search(message_text)
    generate_img(message_text, message_id)


def generate_img(name, id):

    try:
        os.mkdir("files/saves/{}".format(id))
    except:
        pass

    try:
        os.mkdir("files/blur/{}".format(id))
    except:
        pass

    logics.search_image.download_img(name, id)

    dir = os.listdir(os.getcwd()+"/files/saves/{}/".format(id))
    for i in range(len(dir)):
        if len(dir[i]) < 7:
            logics.blur.photo_one("files/saves/{}/{}".format(id, dir[i]), "files/blur/{}/{}{}.jpg".format(id, i, "{}"))
        os.remove("files/saves/{}/{}".format(id, dir[i]))
    os.rmdir("files/saves/{}".format(id))


def push_all(bot, message):
    message_id = message.from_user.id


    dir = os.listdir(os.getcwd() + "/files/blur/{}".format(message_id))

    bot.send_message(message_id, "Uploading {} image".format(len(dir)))
    time.sleep(2)
    for i in range(len(dir)):
        with open("files/blur/{}/{}".format(message_id, dir[i]), "rb") as img:
            bot.send_chat_action(message_id, "upload_photo")
            time.sleep(1)
            bot.send_photo(message_id, img)
            os.remove("files/blur/{}/{}".format(message_id, dir[i]))
    os.rmdir("files/blur/{}".format(message_id))