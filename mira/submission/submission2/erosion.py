# -- File: erosion.py --
# Author: vzbf32
# Creation date: 2017-12-17 18:05
# Purpose: Implements greyscale erosion with a square structuring element of a size 5x5 pixels
# N.B. `ROI` means `region of interest`



# Necessary imports
# - `sys` for getting arguments when script is run from terminal
# - `numpy` for getting height and width of image
# - `cv2` for loading images as greyscale
import sys
import numpy as np
import cv2



# Erodes an image specifically with a 5x5 kernel. We take image data parsed by cv2.
# We iterate through every pixel and make a list of the values surrounding that pixel 
# in a 5x5 block. For example, if we are centred around the pixel with value 104 in
# the following diagram, we will create a list 
# 
# [100, 120, 100, 140, 150, 90, 100, 100, 101, 99, 95, 97, 104, 102, 95, 84, 90, 99, 
#   97, 90, 89, 91, 99, 96, 103]
# 
# and we will set the corresponding pixel to the minimum value of this list (in our
# case, 84) in the new image.
# 
#  100 120 100 140 150
#   90 100 100 101  99
#   95  97 104 102  95
#   84  90  99  97  90
#   89  91  99  96 103
#
# Near the edge of the image, we may find that the kernel extends to pixels that do
# not exist. In this case, we check that we are reading from a pixel that is on the
# image and if we are not, we simply skip that pixel and move onto the next one in
# the kernel.
def erode(img, save=1):
    """Erodes an image.

    :param img: The image to erode.
    :param save: Determines whether to save the image or return it.
                 1 is save, 0 is return.
    """
    # Copy the data from `img` to `erodedImg`, which is the 'working' image
    erodedImg = img.copy()

    # Get the height and width of `img` using numpy
    height, width = np.shape(img)

    # Iterate through each individual pixel (first along the X axis, then the Y axis)
    for y in range(0, height):
        for x in range(0, width):

            # Create an empty array that we use for the values of each pixel in the ROI
            ROIvalues = []

            # Iterate through the 5x5 ROI centred around the current pixel
            # Remember that `range(a,b)` includes `a` and excludes `b`
            for yROI in range(y-2, y+3):
                for xROI in range(x-2, x+3):

                    # If out of bounds, just leave the value out of the list
                    if yROI <= -1 or yROI >= height or xROI <= -1 or xROI >= width:
                        continue
                    else:
                        # Append the value of each pixel in the 5x5 ROI to `ROIvalues`
                        ROIvalues.append(img[xROI][yROI])

            # Set the value of that pixel to the minimum value of all the pixel values in the ROI
            erodedImg[x][y] = min(ROIvalues)

    # Output or return the eroded image as appropriate
    if save == 1:
        # Write the image to the second argument string when the program is run
        cv2.imwrite(sys.argv[2], erodedImg)
        print("Wrote eroded image to " + sys.argv[2])
    elif save == 0:
        # Return the image data to the function that called this function
        return erodedImg
    else:
        # Somehow a save flag value of neither 0 nor 1 was set - return nothing and print an error
        print("Error - invalid save flag for erosion")



# If we run the script by itself rather than as an imported module
if __name__ == "__main__":
    # Check the user specified a filename for input
    if len(sys.argv) <= 1:
        print("Not enough arguments - no input image specified")
    elif len(sys.argv) == 2:
        print("Not enough arguments - no output image specified")
    else:
        # Read the image as greyscale using cv2
        img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        if not img is None:
            erode(img)
        else:
            print("Image '" + sys.argv[1] + "' was not successfully loaded.")