import logics.search_image.constant as const
from random import shuffle
from urllib.request import urlopen, urlretrieve


def html_get(name, type=const.mode):
    url = const.url[type].format(name)
    page = str(urlopen(url).read())
    return type, page

def yandex_slise(page):
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


def image_get(folder, url_type, page, number=const.download_img):
    if url_type == "Yandex":
        list_img = yandex_slise(page)
        for i in range(30):
            try:
                format_img = list_img[i].split(".")[-1]
                download_img(list_img[i], "{}/bunny{}.{}".format(folder ,i, format_img))
            except:
                pass
    elif url_type == "Google":
        pass
    elif url_type == "Bing":
        pass


def download_img(url, name):
    urlretrieve(url, name)




if __name__ == '__main__':
    t, page = html_get("bunny")
