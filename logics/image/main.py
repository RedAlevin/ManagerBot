import numpy as np
import PIL.Image as image
import PIL.ImageFilter


def smart_slise(img_array):
    # if the image is square --> all norm
    # else centered and take a square from the center
    size_img = len(img_array), len(img_array[0])

    if size_img[0] == size_img[1]:
        img_arr2 = np.array(img_array, dtype=np.float32)
    elif size_img[0] > size_img[1]:
        new_ar_f = []
        for i in range(size_img[1]):
            new_ar_l = []
            for i2 in range(size_img[1]):
                new_ar_l.append(img_array[(size_img[0] - size_img[1])//2 + i][i2])
            new_ar_f.append(new_ar_l)
        img_arr2 = np.array(new_ar_f, dtype=np.float32)

    elif size_img[0] < size_img[1]:
        new_ar_f = []
        for i in range(size_img[0]):
            new_ar_l = []
            for i2 in range(size_img[0]):
                new_ar_l.append(img_array[i][i2 + (size_img[1] - size_img[0]) // 2])
            new_ar_f.append(new_ar_l)
        img_arr2 = np.array(new_ar_f, dtype=np.float32)

    return img_arr2


def open_img_in_array(name_img):
    # open image --> RGB --> array
    img = image.open(name_img)
    img = img.convert("RGB")
    size_img = list(img.size)
    if size_img[1]%2 == 1:
        size_img[1] += 1
    if size_img[0]%2 == 1:
        size_img[0] += 1
    img = img.resize(size_img)
    img_ar = np.array(img, dtype=np.float32)
    return img_ar


def convert_array_to_img(array, w, h):
    # array --> image
    img = image.new("RGB", [h, w])
    for i in range(h):
        for i1 in range(w):
            img.putpixel((i, i1), tuple(array[i1][i]))

    return img


def front_img(img, num, num2):
    # background
    img = img.resize((num2, num2))
    img = bluring(img, num)

    return img


def plate_img_1(img1, img2):
    #img1 - smaller img
    #img2 - bigger img
    img_ar1 = np.array(img1, dtype=np.float32)
    img_ar2 = np.array(img2, dtype=np.float32)

    sd = (len(img_ar2) - len(img_ar1)) // 2

    for i in range(len(img_ar1)):
        for i2 in range(len(img_ar1)):
                img_ar2[i+sd][i2+sd] = img_ar1[i][i2]
    return img_ar2


def plate_img_2(img1, img2, border=2):
    #img1 - smaller img
    #img2 - bigger img
    img_ar1 = np.array(img1, dtype=np.float32)
    img_ar2 = np.array(img2, dtype=np.float32)

    sd = (len(img_ar2) - len(img_ar1)) // 2

    for i in range(len(img_ar1) + 2*border):
        for i2 in range(len(img_ar1) + 2*border):
                img_ar2[i+sd-border][i2+sd-border] = [0, 0, 0]
    for i in range(len(img_ar1)):
        for i2 in range(len(img_ar1)):
                img_ar2[i+sd][i2+sd] = img_ar1[i][i2]
    return img_ar2


def plate_img_3(img1, img2, img3, border=80, sizeWhite=640):
    #img1 - first img
    #img2 - second img
    #img3 - third img

    white_space = image.new("RGB",(sizeWhite, sizeWhite), "white")
    white_ar = np.array(white_space, dtype=np.float32)

    img_ar1 = np.array(img1, dtype=np.float32)
    img_ar2 = np.array(img2, dtype=np.float32)
    img_ar3 = np.array(img3, dtype=np.float32)

    sd = (sizeWhite - (len(img_ar1)+2*border)) // 2

    for i in range(len(img_ar1)):
        for i2 in range(len(img_ar1)):
            white_ar[i+sd][i2+sd+2*border] = img_ar3[i][i2]
    for i in range(len(img_ar1)):
        for i2 in range(len(img_ar1)):
            white_ar[i+sd+border][i2+sd+border] = img_ar2[i][i2]
    for i in range(len(img_ar1)):
        for i2 in range(len(img_ar1)):
            white_ar[i+sd+2*border][i2+sd] = img_ar1[i][i2]
    return white_ar

def bluring(img, n=2):
    # blur n iteration
    for i in range(n):
        img = img.filter(PIL.ImageFilter.BLUR)
    return img


def img_slise(img, size=10, size2=10):
    # cutting image
    img_ar = np.array(img, dtype=np.float32)
    new_img = image.new("RGB",[len(img_ar)-2*size,len(img_ar)-2*size2])
    for i in range(len(img_ar)-2*size):
        for i2 in range(len(img_ar)-2*size2):
            new_img.putpixel((i, i2), tuple(img_ar[i2+size2][i+size]))
    return new_img


def photo(name, name2=None, name3=None, border=2, mode=1, bluring_con=12, size1=520, size2=640, size3=400):
    # finish function

    img_inp_p = open_img_in_array(name)
    img_inp = smart_slise(img_inp_p)
    img = convert_array_to_img(img_inp, len(img_inp), len(img_inp[0]))
    img = img.resize((size1, size1))

    if mode==1:
        imgBlur = front_img(img, bluring_con, size2+160)
        imgBlur = img_slise(imgBlur, 80, 80)
        img_ar_new = plate_img_1(img, imgBlur)
    elif mode==2:
        imgBlur = front_img(img, bluring_con, size2 + 160)
        imgBlur = img_slise(imgBlur, 80, 80)
        img_ar_new = plate_img_2(img, imgBlur, border)
    elif mode==3:
        img_inp_p2 = open_img_in_array(name2)
        img_inp2 = smart_slise(img_inp_p2)
        img2 = convert_array_to_img(img_inp2, len(img_inp2), len(img_inp2[0]))
        img2 = img2.resize((size1, size1))

        img_inp_p3 = open_img_in_array(name3)
        img_inp3 = smart_slise(img_inp_p3)
        img3 = convert_array_to_img(img_inp3, len(img_inp3), len(img_inp3[0]))
        img3 = img3.resize((size1, size1))

        imgBlur2 = front_img(img2, bluring_con, size2+20)
        imgBlur2 = img_slise(imgBlur2, 10, 10)

        imgBlur3 = front_img(img3, 2 * bluring_con, size2 + 20)
        imgBlur3 = img_slise(imgBlur3, 10, 10)

        img = img.resize((size3, size3))
        imgBlur2 = imgBlur2.resize((size3, size3))
        imgBlur3 = imgBlur3.resize((size3, size3))

        img_ar_new = plate_img_3(img, imgBlur2, imgBlur3, sizeWhite=size2)
    elif mode ==4:

        img_inp_p2 = open_img_in_array(name2)
        img_inp2 = smart_slise(img_inp_p2)
        img2 = convert_array_to_img(img_inp2, len(img_inp2), len(img_inp2[0]))
        img2 = img2.resize((size1, size1))


        imgBlur2 = front_img(img2, bluring_con, size2+160)
        imgBlur2 = img_slise(imgBlur2, 80, 80)
        img_ar_new = plate_img_1(img, imgBlur2)
    elif mode ==5:

        img_inp_p2 = open_img_in_array(name2)
        img_inp2 = smart_slise(img_inp_p2)
        img2 = convert_array_to_img(img_inp2, len(img_inp2), len(img_inp2[0]))
        img2 = img2.resize((size1, size1))


        imgBlur2 = front_img(img2, bluring_con, size2+160)
        imgBlur2 = img_slise(imgBlur2, 80, 80)
        img_ar_new = plate_img_2(img, imgBlur2)


    img_new = convert_array_to_img(img_ar_new, size2, size2)

    return img_new
