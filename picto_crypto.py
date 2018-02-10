import cv2
import numpy as np
import hashlib as hs
# import random as rd

def encrypt():
    with open('test.txt', 'r') as in_file:
        data = in_file.read()  # input('message to encrypt: ')
    print('data achieved')
    url = 'black_baby.jpg'
    key_in = cv2.imread(url)  # this is the array that will be edited
    url = url.encode('utf-8')
    out_name = str(hs.md5(url).hexdigest()) + '.png'
    # print(type(key_in))
    print('key in set')

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
        print(pxl_num, ch_num, num)
        key_in[i][j][k] = num.astype(np.int8)
        print('new val:', key_in[i][j][k])
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
    print('Done encrypting')


# encrypt()
# ^^^ that works I think vvv is to decrypt the message
orig_url = 'black_baby.jpg'     # this is partially hardcoded but yea if the files name where changed from the time of encryption it would not work
url = orig_url.encode('utf-8')
key_url = str(hs.md5(url).hexdigest()) + '.png'
encrypted = cv2.imread(key_url)
orig = cv2.imread(orig_url)
# print('orig____ \n', orig, 'encrypted____\n', encrypted)
def decrypt():
    st = ''
    for i in range(len(orig)):
        bv = False
        for j in range(len(orig[0])):
            for k in range(3):
                o_num = orig[i][j][k]
                e_num = encrypted[i][j][k]
                ch_num = o_num - e_num
                char = chr(ch_num)
                st = st + char
                # print(o_num, e_num, ch_num, st)
                if ch_num == 0:
                    bv = True
                    return st
            if bv:
                return st
        if bv:
            return st


string = decrypt()

print(string)
