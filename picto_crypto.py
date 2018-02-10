import cv2
import numpy as np
import hashlib as hs
import random as rd
task = input("Are you encrypting(e) or decrypting(d)? put type 'e' for encrypting or 'd' for decrypting: ")
def encrypt():
    text = input('path to .txt file to encrypt: ')
    with open(text, 'r') as in_file:
        data = in_file.read()  # input('message to encrypt: ')
    print('data achieved')
    url = input('path to base image that data will be encrypted into: ')
    key_in = cv2.imread(url)  # this is the array that will be edited
    #######################################################################
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
        print('making the destroyed file for encryption set')
        for i in range(ext_len):
            print('working on row:', i)
            for j in range(len_2):
                for k in range(3):
                    orig_int = img[i][j][k]
                    seed_choice = rd.randrange(2)
                    img[i][j][k] = get_int(orig_int, seeds[seed_choice])

    seeds = [rd.randrange(255), rd.randrange(255), rd.randrange(255)]
    img = key_in
    ext_len = len(img)
    len_2 = len(img[0])
    file_name = "new_" + url
    destroy(img)
    cv2.imwrite(filename=file_name, img=img)
    # print(file_name + " has been writen!")
    #######################################################################
    url = file_name
    url = url.encode('utf-8')
    out_name = str(hs.md5(url).hexdigest()) + '.png'
    # print(type(key_in))
    print('key is set')

    def get_ascii(string):
        idx_st = []
        for i, ch in enumerate(string):
            idx_st.append(ord(ch))
        return tuple(idx_st)

    data = get_ascii(data)
    print('ascii achieved')
    data_len = len(data)

    def get_depths():  # this  function will return 3 depths that answers the question: How many  pixels  will get
        data_len_l = data_len  # local var to keep track how far i has to go
        depth1 = 1  # how many rows to include
        depth2 = 1  # how many columns to include
        depth2_0 = 0  # residual columns in last row
        depth3 = 0  # greatest possible val is 2 and this is the depth into the  3rd dimension needed
        while True:
            if len(key_in[0]) * 3 < data_len_l:  # how  many rows -1? # main loop set
                data_len_l = data_len_l - len(key_in[0]) * 3
                depth1 += 1
            if data_len_l > 3:  # how many columns to include in the for loop later
                data_len_l -= 3
                depth2 += 1
            elif 3 < data_len_l <= len(key_in):  # depth2_0 residual columns in last row
                depth2 += 1
                data_len_l -= 3
            if data_len_l <= 3:  # final loop for 3rd dimension depth
                if data_len_l == 3:
                    depth2_0 += 1
                    break
                else:
                    depth3 = data_len_l
                    break
        return depth1, depth2, depth2_0, depth3

    depth1, depth2, depth2_0, depth3 = get_depths()
    print('Depths achieved')
    # print(depth1, depth2, depth2_0, depth3)
    data_plc = 0
    def edit_picture(i, j, k, e):  # technically no glitch but this does not work if the pixel's value is less than the ord()
        ch_num = data[e]    # the ord() from the  data tuple
        pxl_num = key_in[i][j][k]
        pxl_num = pxl_num.astype(int)
        num = pxl_num - ch_num
        # print(pxl_num, ch_num, num)
        key_in[i][j][k] = num.astype(np.int8)
        # print('new val:', key_in[i][j][k])
        # print('edit_picture:', pxl_num, ch_num, num)

    for i in range(depth1):
        for j in range(depth2):
            # if j == depth2 - 1:  # this part is problematic
            #     for h in range(depth2_0):
            #         for k in range(3):
            #             # print('key in', key_in[i][j][k], 'ord: ', data[data_plc])
            #             edit_picture(i, h, k, data_plc)
            #             data_plc += 1
            #             # print('key out', key_in[i][j][k])
            # else:
            for k in range(3):
                # print('key in', key_in[i][j][k], type(key_in[i][j][k]), 'ord:', data[data_plc])
                edit_picture(i, j, k, data_plc)
                data_plc += 1
                # print('key out', key_in[i][j][k], type(key_in[i][j][k]))
    print('key_in ==> key_out [success]')
    cv2.imwrite(out_name, key_in)
    print('Done encrypting! Your encrypted file is', out_name)
    print("DO NOT CHANGE THE FILE'S NAME! WHEN DECRYPTING BOTH FILES MUST BE IN THE SAME DIRECTORY WITH THIS PROGRAM")
    # ^^^ all that for the encryption
# encrypt()
# ^^^ that works I think vvv is to decrypt the message
def decrypt():
    orig_url = input('original (unedited) image path:')  # this is partially hardcoded but yea if the files name where changed from the time of encryption it would not work
    url = orig_url.encode('utf-8')
    key_url = str(hs.md5(url).hexdigest()) + '.png'
    encrypted = cv2.imread(key_url)
    orig = cv2.imread(orig_url)
    st = open(str(hs.md5(url).hexdigest())+'.txt', 'w')
    for i in range(len(orig)):
        bv = False
        for j in range(len(orig[0])):
            for k in range(3):
                o_num = orig[i][j][k]
                o_num = o_num.astype(int)
                e_num = encrypted[i][j][k]
                e_num = e_num.astype(int)
                ch_num = o_num - e_num
                char = chr(ch_num)
                st.write(char)
                # print(o_num, e_num, ch_num, st)
                if ch_num == 0:
                    bv = True
                    break
            if bv:
                break
        if bv:
            break
    st.close()
    print("The decrypted data is in the file: ", str(hs.md5(url).hexdigest())+'.txt')

def __main__(t):
    if t == 'e':
        encrypt()
        exit('happy hacking!')
    elif t == 'd':
        decrypt()
        exit('happy hacking!')
    else:
        exit('Your not great with instructions try again.')
# ^^^ runs the  decrypt() and encrypt() and lets the user choose
#
__main__(task)
