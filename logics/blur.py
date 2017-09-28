import PIL.Image as image
import PIL.ImageFilter
import files.constant as const


def smart_slice(img):
    # if the image is square --> all norm
    # else centered and take a square from the center
    size_img = img.size

    if size_img[0] == size_img[1]:
        img_ret = [img]
    elif size_img[0] > size_img[1]:

        border = (size_img[0] - size_img[1]) // 2

        img_ret = [img.crop((border, 0, border + size_img[1], size_img[1])),
                   #img.crop((0, 0, size_img[1], size_img[1])),
                   #img.crop((size_img[0] - size_img[1], 0, size_img[0], size_img[1]))
                   ]
    elif size_img[0] < size_img[1]:

        border = (size_img[1] - size_img[0]) // 2

        img_ret = [img.crop((0, border, size_img[0], border + size_img[0])),
                   #img.crop((0, 0, size_img[0], size_img[0])),
                   #img.crop((0, size_img[1] - size_img[0], size_img[0], size_img[1]))
                   ]
    return img_ret


def front_img(img, add=const.add_to_size):

    size1 = const.big_size + add

    # background
    img = img.resize((size1, size1))
    img = blurring(img)

    return img


def blurring(img):

    n = const.blurring

    # blur n iteration
    for i in range(n):
        img = img.filter(PIL.ImageFilter.BLUR)
    return img


def photo_one(name, new_name):

    border = const.border
    mode = const.default_mode
    size1 = const.small_size
    size2 = const.big_size
    front_border = const.add_to_size // 2
    color_border = const.color_bolder
    mark = const.mark


    img_inp_p = image.open(name)
    img_inp_p.convert("RGBA")

    img_inp = smart_slice(img_inp_p)

    for i in range(len(img_inp)):
        img = img_inp[i]
        img = img.resize((size1, size1))
        imgBlur = front_img(img)
        imgBlur = imgBlur.crop((front_border, front_border,
                                front_border + size2, front_border + size2))
        if mode == 2:
            border_img = image.new("RGBA",
                                   (size1 + border * 2, size1 + border * 2),
                                   color_border)
            imgBlur.paste(border_img, ((size2 - size1 - border * 2) // 2,
                                          (size2 - size1 - border * 2) // 2))
        imgBlur.paste(img, ((size2-size1) // 2,
                                      (size2 - size1) // 2))

        if mark:
            w_m = image.open(const.mark_name)

            w_m = w_m.resize((180, 60))
            imgBlur.paste(w_m, const.mark_position[2])

        imgBlur.save(new_name.format(i))


def photo_two(name1, name2, new_name):

    border = const.border
    mode = const.default_mode
    size1 = const.small_size
    size2 = const.big_size
    front_border = const.add_to_size // 2
    color_border = const.color_bolder
    mark = const.mark


    img_inp_p1 = image.open(name1)
    img_inp_p1.convert("RGBA")
    img_inp1 = smart_slice(img_inp_p1)

    img_inp_p2 = image.open(name2)
    img_inp_p2.convert("RGBA")
    img_inp2 = smart_slice(img_inp_p2)

    img = img_inp1[0]
    img = img.resize((size1, size1))

    imgBlur = front_img(img_inp2[0])
    imgBlur = imgBlur.crop((front_border, front_border,
                            front_border + size2, front_border + size2))

    if mode == 2:
        border_img = image.new("RGB",
                               (size1 + border * 2, size1 + border * 2),
                               color_border)
        imgBlur.paste(border_img, ((size2 - size1 - border * 2) // 2,
                                   (size2 - size1 - border * 2) // 2))
    imgBlur.paste(img, ((size2 - size1) // 2,
                        (size2 - size1) // 2))

    if mark:
        w_m = image.open(const.mark_name)

        w_m = w_m.resize((180, 60))
        imgBlur.paste(w_m, const.mark_position[2])

    imgBlur.save(new_name)


def photo_thee(name1, name2, name3, new_name):

    border = const.border
    mode = const.default_mode3
    size1 = const.XS_size
    size2 = const.big_size
    front_border = const.add_to_size3 // 2
    nd = const.border3
    color_background = const.color_background
    color_border = const.color_bolder
    mark = const.mark


    img_inp_p1 = image.open(name1)
    img_inp_p1.convert("RGBA")
    img_inp1 = smart_slice(img_inp_p1)

    img_inp_p2 = image.open(name2)
    img_inp_p2.convert("RGBA")
    img_inp2 = smart_slice(img_inp_p2)

    img_inp_p3 = image.open(name3)
    img_inp_p3.convert("RGBA")
    img_inp3 = smart_slice(img_inp_p3)

    img = img_inp1[0]
    img = img.resize((size1, size1))

    imgBlur = front_img(img_inp2[0], front_border * 2)
    imgBlur2 = front_img(img_inp3[0], front_border * 2)

    imgBlur = imgBlur.crop((front_border, front_border,
                            front_border + size1, front_border + size1))
    imgBlur2 = imgBlur2.crop((front_border, front_border,
                            front_border + size1, front_border + size1))
    background = image.new("RGB", (size2, size2), color_background)
    nd_border = (size2 - (size1 + 2 * nd)) // 2

    if mode == 1:
        background.paste(imgBlur2, (nd_border + 2 * nd,
                                    nd_border))
        background.paste(imgBlur, (nd_border + nd,
                                   nd_border + nd))
        background.paste(img, (nd_border,
                               nd_border + 2 * nd))
    elif mode == 2:
        border_img = image.new("RGB",
                               (size1 + border * 2, size1 + border * 2),
                               color_border)
        background.paste(border_img, (nd_border + 2 * nd - border,
                                   nd_border - border ))
        background.paste(border_img, (nd_border + nd - border,
                                   nd_border + nd - border))
        background.paste(border_img, (nd_border - border,
                                   nd_border + 2 * nd - border))


        background.paste(imgBlur2, (nd_border + 2 * nd,
                                    nd_border))
        background.paste(imgBlur, (nd_border + nd,
                                   nd_border + nd))
        background.paste(img, (nd_border,
                               nd_border + 2 * nd))

    elif mode == 3:
        border_img = image.new("RGB",
                               (size1 + border * 2, size1 + border * 2),
                               color_border)
        background.paste(border_img, (nd_border + 2 * nd - border,
                                      nd_border - border))
        background.paste(imgBlur2, (nd_border + 2 * nd,
                                    nd_border))

        background.paste(border_img, (nd_border + nd - border,
                                      nd_border + nd - border))
        background.paste(imgBlur, (nd_border + nd,
                                   nd_border + nd))

        background.paste(border_img, (nd_border - border,
                                      nd_border + 2 * nd - border))
        background.paste(img, (nd_border,
                               nd_border + 2 * nd))

    if mark:
        w_m = image.open(const.mark_name)

        w_m = w_m.resize((180, 60))
        background.paste(w_m, const.mark_position[2])

    background.save(new_name)