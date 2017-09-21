import files.constant as const
import logics.search_image

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
    logics.search_image.download_img("bunnu")