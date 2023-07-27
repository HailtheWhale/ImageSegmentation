# Deleting original files
        if os.path.exists(path_source_data_raw):
            os.remove(path_source_data_raw)
        else:
            print("The RAW data could not be found. Please check it")
        if os.path.exists(path_source_data_mask):
            os.remove(path_source_data_mask)
        else:
            print("The MASK data could not be found. Please check it")