import logics.search_image.constant as const
from random import shuffle
from urllib.request import urlopen


def html_get(name, type=const.mode):
    url = const.url[type].format(name)
    page = urlopen(url).read()
    return page

if __name__ == '__main__':
    print(len(html_get("bunny")))