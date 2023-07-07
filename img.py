from random import randint, shuffle
import random
import numpy as np
from PIL import Image
import cv2

array1 = np.zeros([500, 500, 4], dtype=np.uint8)
array2 = np.zeros([500, 500, 4], dtype=np.uint8)
array3 = np.zeros([500, 500, 4], dtype=np.uint8)

def genrate_ar(array, blend=False):
    start = 0
    if blend:
        start = 1
    for row in range(start, len(array)):
        for col in range(start, len(array[0])):
            cel_top = []
            cel_left = []
            if row != 0:
                cel_top = array[row-1][col]
            if col != 0:
                cel_left = array[row][col-1]
            rgb = []
            if len(cel_top) != 0 and len(cel_left) != 0:
                if randint(2, 2) % 2 == 0:
                    cel_left[3] = randint(150, 255)
                    rgb = cel_left
                else:
                    cel_top[3] = randint(150, 255)
                    rgb = cel_top
            else:
                rgb_rand = []
                for a in range(0, 4):
                    rgb_rand.append(randint(50, 255))
                if len(rgb) == 0:
                    rgb = rgb_rand
                else:
                    for i in range(0, 4):
                        add_temp = rgb[i] - rgb_rand[1]
                        if add_temp < 0:
                            add_temp = rgb[i] + rgb_rand[1]
                        rgb[i] = add_temp

            array[row][col] = rgb
    return array





def img_line(nb_line = 1, orientation = "horizontal"):
    if nb_line < 1:
        nb_line = 1
    if nb_line > 500:
        nb_line = 500

    array = np.zeros([500, 500, 4], dtype=np.uint8)
    global array2
    array2 = []
    line = int(500/nb_line)
    it = line
    for row in range(0, len(array)):
        for col in range(0, len(array[0])):
            if row == 0 and col == 0:
                for i in range(0, 3):
                        array[row][col][i]= randint(50, 255)
                array[row][col][3] = randint(150, 255)
            elif row == 0:
                cel_left = array[row][col-1]
                cel_left[3] = randint(150, 255)
                array[row][col] = cel_left
            else:
                if line + it > 500:
                    cel_top = array[row-1][col]
                    cel_top[3] = randint(150, 255)
                    array[row][col] = cel_top
                else:
                    if row == line and col == 0:
                        for i in range(0, 3):
                            array[row][col][i] = randint(10, 255)
                        array[row][col][3] = randint(150, 255)
                    elif row == line:
                        cel_left = array[row][col-1]
                        cel_left[3] = randint(150, 255)
                        array[row][col] = cel_left
                    else:
                        cel_top = array[row-1][col]
                        cel_top[3] = randint(150, 255)
                        array[row][col] = cel_top
        if row == line:
            line += it
    if orientation == "vertical":
        return np.rollaxis(array)
    else:
        return array


def img_uni():
    array = np.zeros([500, 500, 4], dtype=np.uint8)
    global array2
    array2 = []
    for j in range(0, 2):
        for row in range(0, len(array)):
            for col in range(0, len(array[0])):
                if row == 0 and col == 0:
                    for i in range(0, 4):
                            array[row][col][i]= randint(10, 255)
                    array[row][col][3]= randint(150, 255)
                elif row == 0:
                    cel_left = array[row][col-1]
                    cel_left[3] = randint(150, 255)
                    array[row][col] = cel_left
                else:
                    cel_top = array[row-1][col]
                    cel_top[3] = randint(150, 255)
                    array[row][col] = cel_top
        if j == 0:
            array2 = array
    return cv2.addWeighted(array,0.5,array2,0.5,0.9)


def shuffle_ls(array):
    ls = list(array)
    for el in ls:
        random.shuffle(el)
    random.shuffle(ls)
    return ls


def img_test(array):
    # Point de départ
    x, y = (randint(0, len(array[0]) - 1), randint(0, len(array) - 1))
    pos = (x, y)

    # Quel figure ?
    figure = randint(0, 3)
    if figure == 0:
        pass
    elif figure == 1:
        pass
    elif figure == 2:
        pass
    elif figure == 3:
        pass

    # Quel grandeur ?
    

    


array1 = genrate_ar(array1)
array2 = genrate_ar(array2)

print("Finish the generate...")

# img = Image.fromarray(array1)
# img.save('rgb_arr1_origin.png')

img = Image.fromarray(array2)
img.save('rgb_arr2.png')

#np.random.shuffle(array1)
#img = Image.fromarray(img_line(np.zeros([500, 500, 4], dtype=np.uint8)))
#img.save('rgb_arr1_blend.png')



# CV2
img = Image.fromarray(genrate_ar(img_line(5), blend=False))
img.save('blend_rgb.png')



# choisis un point dans le tableau (x,y) = (row,col)
# il décide d'une forme: cercle carré rectangle triangle
# il choisis une taille et vois si il a la place sinon adapte