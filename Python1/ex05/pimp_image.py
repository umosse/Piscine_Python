from load_image import ft_load
import cv2
import numpy as numpy


def ft_invert(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	Prints the image after inverting its colors.
	"""

	invert = img_array.copy()

	invert = 255 - invert
	
	print(invert)

	return invert


def ft_red(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	Prints the image after applying a red filter.
	"""

	red = img_array.copy()

	red[:, :, 1] *= 0
	red[:, :, 2] *= 0
	
	print(red)

	return red


def ft_green(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	Prints the image after applying a green filter.
	"""

	green = img_array.copy()

	green[:, :, 0] -= green[:, :, 0]
	green[:, :, 2] -= green[:, :, 2]
	
	print(green)

	return green

def ft_blue(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	Prints the image after applying a blue filter.
	"""

	blue = img_array.copy()

	blue[:, :, 0] = 0
	blue[:, :, 1] = 0

	print(blue)

	return blue


def ft_grey(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	Prints the image after applying a grey filter.
	"""

	grey = img_array.copy()

	grey = cv2.cvtColor(grey, cv2.COLOR_RGB2GRAY)

	print(grey)

	return grey


def	main():
	img_array = ft_load("landscape.jpg")


if __name__ == "__main__":
	main()