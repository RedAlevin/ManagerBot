import files.constant as const
from random import shuffle
from urllib.request import urlopen, urlretrieve


def html_get(name, type=const.mode):
    url = const.url[type].format(name)
    page = str(urlopen(url).read())
    with open("html.html", 'w') as html:
        html.write(page)
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
        list_img = yandex_slice(page)
        print(list_img)
        shuffle(list_img)
        for i in range(const.download_img):
            try:
                format_img = list_img[i].split(".")[-1]
                file_name = "{}/{}.{}".format(folder, i, format_img)
                download_img(list_img[i], file_name)
            except:
                pass
    elif url_type == "Google":
        pass
    elif url_type == "Bing":
        pass


def dow_img(url, name):
    urlretrieve(url, name)


def download_img(name):
    page = html_get(name)
    print(len(page))
    image_get(const.folder, "Yandex", page)
