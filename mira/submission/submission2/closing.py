# -- File: closing.py --
# Author: vzbf32
# Creation date: 2017-12-17 18:59
# Purpose: Using the erosion and dilation implementations, implement a greyscale closing with
#          a square structuring element of a size 5x5 pixels



# Necessary imports
# - `sys` for getting arguments when script is run from terminal
# - `numpy` for getting height and width of image
# - `cv2` for loading images as greyscale
# - `erosion` for eroding the image
# - `dilation` for dilating the image
import sys
import cv2
import erosion
import dilation



# Closes an image by dilating the image and then eroding it.
# We call dilation.dilate() and erosion.erode() with the save flag set to 0; this way the functions
# will return the dilated/eroded image data rather than saving it to a file.
def close(img):
    """Opens an image by eroding it and then dilating it.

    :param img: The image to open.
    """

    dilatedImg = dilation.dilate(img, save=0)
    closedImg = erosion.erode(dilatedImg, save=0)

    # Output the closed image as appropriate
    # Write the image to the second argument string when the program is run
    cv2.imwrite(sys.argv[2], closedImg)
    print("Wrote closed image to " + sys.argv[2])



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
            close(img)
        else:
            print("Image '" + sys.argv[1] + "' was not successfully loaded.")