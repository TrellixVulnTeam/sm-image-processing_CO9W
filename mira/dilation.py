# -- File: dilation.py --
# Author: vzbf32
# Creation date: 2017-12-17 18:59
# Purpose: Implements greyscale dilation with a square structuring element of a size 5x5 pixels
# N.B. `ROI` means `region of interest`



# Necessary imports
# - `sys` for getting arguments when script is run from terminal
# - `numpy` for getting height and width of image
# - `cv2` for loading images as greyscale
# - `erosion` for eroding the image
import sys
import numpy as np
import cv2
import erosion



# Inverts an 8-bit greyscale image.
# Takes an image input, iterates through every pixel on the image and replaces each
# pixel value V with the number 255-V. 255 is the maximum value each pixel can take
# (if we are dealing in 8-bit images), so 255-V for each image will invert the
# greyscale image.
def invert(img):
	"""Inverts an image.
	
	:param img: The image to dilate.
	"""
	
	# Get the height and width of `img` using numpy
	height, width = np.shape(img)
	
	# Iterate through each individual pixel (first along the X axis, then the Y axis)
	for y in range(0, height):
		for x in range(0, width):
			
			# Replace the value V at each pixel with 255-V as this will invert the pixel
			img[x][y] = 255 - img[x][y]
	
	# Return the inverted image data
	return img


# Dilates an image specifically with a 5x5 kernel. We take image data parsed by cv2.
# Dilation is as simple as inverting the image, eroding it, and then inverting it again.
# To reduce code duplication, we simply import the `erosion` module and call `erosion.erode()`
# for the erosion. 
def dilate(img, save=1):
	"""Dilates an image.
	
	:param img: The image to dilate.
	:param save: Determines whether to save the image or return it.
	             1 is save, 0 is return.
	"""

	invertedImg = invert(img)
	erodedImg = erosion.erode(invertedImg, save=0)
	dilatedImg = invert(erodedImg)
	
	# Output or return the dilated image as appropriate
	if save == 1:
		# Write the image to the second argument string when the program is run
		cv2.imwrite(sys.argv[2], dilatedImg)
		print("Wrote dilated image to " + sys.argv[2])
	elif save == 0:
		# Return the image data to the function that called this function
		return dilatedImg
	else:
		# Somehow a save flag value of neither 0 nor 1 was set - return nothing and print an error
		print("Error - invalid save flag for dilation")
	
	
	
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
			dilate(img)
		else:
			print("Image '" + sys.argv[1] + "' was not successfully loaded.")