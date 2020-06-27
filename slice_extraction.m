%% single slice extraction from multiple brain MR images

clear all
clc

image_folder = 'C:\Users\lenovo\Desktop\New folder\CN_GM';
filenames = dir(fullfile(image_folder, '*.nii'));
total_images = numel(filenames);

for i = 1:total_images
    f = fullfile(image_folder, filenames(i).name);
    img = niftiread(f);
    img_size = size(img);
    slice = img(:,:,img_size(3)/2);
    imwrite(slice, fullfile(image_folder, strcat('CN_GM_', num2str(i), '.jpeg')));
end
