import files.constant as const
import logics.search_image
import time

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


def generate_img():
    time.sleep(1)
    logics.search_image.download_img("fuck")