% To create the datastores needed in the Deep Network Designer 

% Creating Training Data Data store for Deep Network Designer
% Directory to folder containing raw images
imageDir = 'C:\Users\dmg20\Research\Computer_Vision\images\U_Net_Images\video_1\Raw_Imgs';
% Creating image object containing raw images; An array of image directories and subfolder directories
imds = imageDatastore(imageDir);
% Directory to folder containiing grayscale masks 
labelDir = 'C:\Users\dmg20\Research\Computer_Vision\images\U_Net_Images\video_1\Labelled_Imgs_Gray';
% Defined classes will be learning for. Defined during image labeling 
classNames = ["blade","background","blade_defect_sunburn","blade_edge"];
% Pixel value for the corresponding class.
labelIDs   = [0,64,128,192];
% Pixel Data store of mask data
%%%%%% ???? MANY <Undefined> Pixels. 
pxds = pixelLabelDatastore(labelDir,classNames,labelIDs);
trainingData = combine(imds,pxds);

% Creating Validation Data Data store for Deep Network Designer
% Directory to folder containing test images
imageDir_test = 'C:\Users\dmg20\Research\Computer_Vision\images\U_Net_Images\video_1\Test_Imgs';
% Creating image object containing test images; An array of image directories and subfolder directories
imds_test = imageDatastore(imageDir_test);
% Directory to folder containiing grayscale masks 
labelDir = 'C:\Users\dmg20\Research\Computer_Vision\images\U_Net_Images\video_1\Test_Labels';
% Defined classes will be learning for. Defined during image labeling 
classNames = ["blade","background","blade_defect_sunburn","blade_edge"];
% Pixel value for the corresponding class.
labelIDs   = [0,64,128,192];
% Pixel Data store of mask data
%%%%%% ???? MANY <Undefined> Pixels. Blur the image to get rid of ????
pxds_test = pixelLabelDatastore(labelDir,classNames,labelIDs);
validationDate = combine(imds_test,pxds_test);