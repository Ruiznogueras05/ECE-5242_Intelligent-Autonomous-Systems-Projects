import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from roipoly import RoiPoly

##IMPORTANT TO CHANGE##
imageFolderPath = '/Users/GilbertoE.Ruiz/IntelAutoSys/Project1/Proj1TrainImages'
imageFolder = os.listdir(imageFolderPath)


##IMPORTANT TO CHANGE##
segmentedConeFolderPath = '/Users/GilbertoE.Ruiz/IntelAutoSys/Project1/SegmentedConeImages'
output_folder = os.path.join(segmentedConeFolderPath)


##IMPORTANT TO CHANGE##
segmentedFolderPath = '/Users/GilbertoE.Ruiz/IntelAutoSys/Project1/SegmentedImages'
output_folder2 = os.path.join(segmentedFolderPath)


for i, imageFile in enumerate(imageFolder):
    # Getting the image path 
    imagePath = os.path.join(imageFolderPath, imageFile)

    image = cv2.imread(imagePath)

    # Plotting the image for the user to draw the first ROI (cone object)
    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Draw a rectangle inside a cone, then press q")

    # Red rectangle object to get ROI of cone
    roi = RoiPoly(color='r', fig=plt.gcf())
    mask = roi.get_mask(current_image=image[:, :, 0])

    ys, xs = np.where(mask)
    x_min, x_max, y_min, y_max = np.min(xs), np.max(xs), np.min(ys), np.max(ys)

    # Image thats been applied with the mask
    segmentedConeImage = image[y_min:y_max, x_min:x_max]

    segmented_image_path = os.path.join(segmentedConeFolderPath, f"segmented_cone_{i + 1}.png")
    cv2.imwrite(segmented_image_path, segmentedConeImage)


    #Plotting the image again for the user to draw the second ROI (non cone object)
    plt.figure(figsize=(10,8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Draw a rectangle of a non cone object, then press q")

    roi2 = RoiPoly(color='b', fig=plt.gcf())
    mask2 = roi2.get_mask(current_image=image[:, :, 0])

    ys2, xs2 = np.where(mask2)
    x_min2, x_max2, y_min2, y_max2 = np.min(xs2), np.max(xs2), np.min(ys2), np.max(ys2)

    # Image thats been applied with the mask
    segmentedImage = image[y_min2:y_max2, x_min2:x_max2]

    segmented_image_path2 = os.path.join(segmentedFolderPath, f"segmented_{i + 1}.png")
    cv2.imwrite(segmented_image_path2, segmentedImage)

