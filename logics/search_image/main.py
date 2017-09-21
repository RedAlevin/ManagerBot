
keys = ["cat", "dog", "bunny"]
"""
from urllib.request import urlopen
url = "https://www.google.ru/search?q={}&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X.html"

for i in range(len(keys)):
    a = keys[i]
    urlK = url.format(a)
    html = urlopen(url)
    with open("{}.html".format(i), "wb") as fh:
        fh.write(html.read())

print("COMPLITE")


from urllib.request import urlopen
for i in range(len(keys)):
    page = urlopen('https://yandex.ru/images/search?text={}'.format(keys[i]))

    with open("{}.html".format(keys[i]), "wb") as fh:
        fh.write(page.read())
"""


with open("bunny.html", 'r') as html:
    print(len(html.readline()))