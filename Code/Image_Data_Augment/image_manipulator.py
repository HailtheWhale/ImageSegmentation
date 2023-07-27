'''
Changes the threshold values of the truthy masks made
by Labelme
'''

import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2

# Directory containing all of the image mask data (.npy files)
# Directory was copied pasted. 
img_mask_data_dir = "C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\marked_images\\video_1_VOC\\SegmentationClass"
# img_mask_dir = "C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\marked_images\\video_1_VOC\\SegmentationClassPNG"

# Files in directory 
img_mask_data_list = os.listdir(img_mask_data_dir)
# print(img_mask_data_list)

for img in range(0,len(img_mask_data_list)):
    img_mask_data = os.path.join(img_mask_data_dir, img_mask_data_list[img])
    print("img is:", img_mask_data_list[img])

    # Loading data 
    img_mask_data = np.load(img_mask_data)

    # Counting pixel labels 
    # zero_cnt = 0
    # one_cnt = 0
    # two_cnt = 0
    # three_cnt = 0

    # Getting image dimensions 
    # Files in directory 
    # img_mask_list = os.listdir(img_mask_dir)
    # print(img_mask_data_list)
    # img_data = os.path.join(img_mask_dir, img_mask_list[0])
    # print(img_mask_data)

    # pic = Image.open(img_data)
    # pic_arr = np.asarray(pic)
    # print("The shape of the img is:", pic_arr.shape)

    # Creating blank mask to copy
    blank_img = np.zeros((480,640))
    # print(blank_img.shape)


    # Looping to count:
    for row in range(0,img_mask_data.shape[0]):
        for col in range(0,img_mask_data.shape[1]):
            if img_mask_data[row][col] == 0:
                # zero_cnt+=1
                blank_img[row][col] = 0
            elif img_mask_data[row][col] == 1:
                # one_cnt+=1
                blank_img[row][col] = 64
            elif img_mask_data[row][col] == 2:
                # two_cnt+=1
                blank_img[row][col] = 128
            else:
                # three_cnt +=1 
                blank_img[row][col] = 192

    save_path = "C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\video_1\\Labelled_Imgs_Gray\\" + str(img_mask_data_list[img][0:9]) + ".jpg"
    #print(save_path)
    cv2.imwrite(save_path, blank_img)

    # Printing Info 
    # print("### Mask Img Data Points ###")
    # print("\nData summary:\n", img_mask_data)
    # print("\nData shape:\n", img_mask_data.shape)
    # print("label 0 pixel count:",zero_cnt)
    # print("label 1 pixel count:",one_cnt)
    # print("label 2 pixel count:",two_cnt)
    # print("label 3 pixel count:",three_cnt)

