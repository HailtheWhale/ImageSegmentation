'''
To Copy, Rename, and Paste the marked data and raw images 
From multiple folders into one 
'''

import shutil
import os 

path_base = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\Base_images'
path_destination = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined'

# Selecting Base Folder Data 
path_base_info = os.listdir(path_base)
# print(path_base_info)
path_base_info = path_base_info[4:8]

# Looping thru base folder data  
for data in range(0, len(path_base_info)):
    path_source = os.path.join(path_base,path_base_info[data]) + '\Data'
    # print(path_source)
    
    # Collects names of all data files 
    data_info = os.listdir(path_source)
    # print(data_info)
    
    # Storing name of the data folder being pulled from for later naming use 
    data_name = path_base_info[data]
    # print(data_name)
    
    # Looping thru data in data folder 
    for data_nested in data_info:
        # print(data_nested)
        # Source to copy from 
        path_source_data = os.path.join(path_source, data_nested)
        # Source to paste to 
        path_destination_data = os.path.join(path_destination, (data_name + '_' + data_nested))
        # print(path_destination_data)
        ## Uncomment when ready to run...
        #shutil.copy(path_source_data,path_destination_data)