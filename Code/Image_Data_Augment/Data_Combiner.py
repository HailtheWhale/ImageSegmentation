'''
To Copy, Rename, and Paste the marked data and raw images 
From multiple folders into one 
'''

import shutil
import os 

path_base = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\Base_images'
path_destination = 'C:\\Users\\dmg20\\Research\\Computer_Vision\\images\\U_Net_Images\\combined'

path_base_info = os.listdir(path_base)
path_base_info = path_base_info[2:6]
# print(path_base_info[2:6])

for data in range(0, len(path_base_info)):
    path_source = os.path.join(path_base,path_base_info[data]) + '\Data'
    # print(path_source)
    data_info = os.listdir(path_source)
    # print(data_info)
    data_name = path_base_info[data]
    # print(data_name)
    for data_nested in data_info:
        # print(data_nested)
        path_source_data = os.path.join(path_source, data_nested)
        path_destination_data = os.path.join(path_destination, (data_name + '_' + data_nested))
        # print(path_destination_data)
        
        shutil.copy(path_source_data,path_destination_data)