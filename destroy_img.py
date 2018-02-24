# Raphael Gonzalez
import cv2
import random as rd

def get_int(orig, seed):
    new_int = orig
    if orig > seed:
        new_int = orig - seed + 70
        return new_int
    elif seed > orig:
        new_int = seed - orig - 80
        return new_int
    else:
        return seed - 20

def destroy(img):
    for i in range(ext_len):
        for j in range(len_2):
            for k in range(3):
                orig_int = img[i][j][k]
                seed_choice = rd.randrange(2)
                img[i][j][k] = get_int(orig_int, seeds[seed_choice])

url = str(input('path to image you want to destroy: '))
seeds = [rd.randrange(255), rd.randrange(255), rd.randrange(255)]
print('new_'+url, "is being written...")
img = cv2.imread(url)
ext_len = len(img)
len_2 = len(img[0])
file_name = "new_" + url
destroy(img)
cv2.imwrite(file_name, img)
print(file_name + " has been writen!")
