import files.constant as const
from random import shuffle
from urllib.request import urlopen, urlretrieve


def html_get(name, type=const.mode):
    url = const.url[type].format(name)
    page = str(urlopen(url).read())
    return page


def yandex_slice(page):
    url_img = []
    while page:
        k = page.find(const.serch["Yandex"])
        page = page[k + len(const.serch["Yandex"]):]
        c_page = page.split("&amp;")

        # format url
        try:
            url_o_img = c_page[1][8:]
            url_o_img = url_o_img.replace("%3A", ":")
            url_o_img = url_o_img.replace("%2F", "/")

            url_img.append(url_o_img)
        except:
            pass
    return url_img


def google_slice(page):
    pass


def bing_slice(page):
    pass


def image_get(folder, url_type, page):
    if url_type == "Yandex":
        list_img = yandex_slice(page)[:30]
        shuffle(list_img)
        for i in range(const.download_img):
            try:
                format_img = list_img[i].split(".")[-1]
                file_name = "{}/{}.{}".format(folder, i, format_img)
                urlretrieve(list_img[i], file_name)
            except:
                pass
    elif url_type == "Google":
        pass
    elif url_type == "Bing":
        pass


def download_img(name, mode=const.mode):
    page = html_get(name, mode)
    image_get(const.folder, mode, page)



def ru_to_search(message):

    message = message.lower()

    message = message.replace(" ", "%20")

    ru_alp = "ёйцукенгшщзхъфывапролджэячсмитьбю"
    sea_alp = ["%D1%91",  # ё
               "%D0%B9",  # й
               "%D1%86",  # ц
               "%D1%83",  # у
               "%D0%BA",  # к
               "%D0%B5",  # е
               "%D0%BD",  # н
               "%D0%B3",  # г
               "%D1%88",  # ш
               "%D1%89",  # щ
               "%D0%B7",  # з
               "%D1%85",  # х
               "%D1%8A",  # ъ
               "%D1%84",  # ф
               "%D1%8B",  # ы
               "%D0%B2",  # в
               "%D0%B0",  # а
               "%D0%BF",  # п
               "%D1%80",  # р
               "%D0%BE",  # о
               "%D0%BB",  # л
               "%D0%B4",  # д
               "%D0%B6",  # ж
               "%D1%8D",  # э
               "%D1%8F",  # я
               "%D1%87",  # ч
               "%D1%81",  # с
               "%D0%BC",  # м
               "%D0%B8",  # и
               "%D1%82",  # т
               "%D1%8C",  # ь
               "%D0%B1",  # б
               "%D1%8E",  # ю
               ]
    for i in range(len(ru_alp)):
        message = message.replace(ru_alp[i], sea_alp[i])

    return message

