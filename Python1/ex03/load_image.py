import cv2


def ft_load(path: str) -> list:
	"""
	Loads an image and returns an array with its format and pixels in RGB format.
	"""

	print(path)

	img = cv2.imread(path)

	height, width, channel = img.shape
	print('The shape of image is:', (height, width, channel))

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	return img_rgb
