import files.constant as const
import logics.search_image
import os
import logics.blur


def if_my_message(message):
    message_id = message.from_user.id
    message_text = message.text

    if message_id == const.admin_id:
        if message_text == "+":
            pass
        elif message_text == "-":
            pass
    else:
        pass


def generate_img(name):
    logics.search_image.download_img(name)
    dir = os.listdir(os.getcwd()+"/files/saves")
    for i in range(len(dir)):
        logics.blur.photo("files/saves/{}".format(dir[i]), "files/blur/{}.jpg".format(i))
        os.remove("files/saves/{}".format(dir[i]))
    print("Complited")
