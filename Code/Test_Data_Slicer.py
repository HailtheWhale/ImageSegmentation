'''
To Random select data from dataset for the test dataset  
'''

import shutil
import os 
import random 

path_raw_source = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined_10_21_22\\Raw_Imgs'
path_masks_source = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined_10_21_22\\Labelled_Imgs_Gray'
path_raw_destination = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined_10_21_22\\Test_Imgs'
path_masks_destination = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined_10_21_22\\Test_labels' 

# Setting Slice Threshold 
data_length = len(os.listdir(path_raw_source))
slice_percent = data_length*0.20
# print(int(slice_percent))

# Getting data lists 
path_raw_data = os.listdir(path_raw_source)
path_masks_data = os.listdir(path_masks_source)

# Setting counter
i = 1

# Run code flag 
run_code = True 

# Making sure the data lines up
for file in range(0,data_length):
    if path_raw_data[file] != path_masks_data[file]:
        print("Data does NOT line up")
        run_code = False 
        break 
    
if run_code == True:
    # looping till Slice Threshold 
    while i <= int(slice_percent):
        # Getting rand index from data list 
        test_index = random.randint(0,len(os.listdir(path_raw_source))-1)
        # Getting indexed file 
        data_raw = path_raw_data[test_index]
        data_mask = path_masks_data[test_index]
        # Sources to copy from 
        path_source_data_raw = os.path.join(path_raw_source, data_raw)
        path_source_data_mask = os.path.join(path_masks_source, data_mask)
        # Sources to paste to 
        path_destination_data_raw = os.path.join(path_raw_destination, data_raw)
        path_destination_data_mask = os.path.join(path_masks_destination, data_mask)
        if os.path.exists(path_source_data_raw) and os.path.exists(path_source_data_mask):
            # Copying files 
            shutil.copy(path_source_data_raw,path_destination_data_raw)
            shutil.copy(path_source_data_mask,path_destination_data_mask)
            # Deleting original files
            os.remove(path_source_data_raw)
            os.remove(path_source_data_mask)
            i+=1
        else:
            print("The data could not be found. Trying again.")

# print(len(os.listdir(path_raw_destination)))