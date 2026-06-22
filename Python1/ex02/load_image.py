import cv2
import numpy as numpy

def ft_load(path: str) -> list:
	"""
	
	"""

	print(path)

	img = cv2.imread(path)

	height, width, channel = img.shape
	print('The shape of image is :', (height, width, channel))

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	result = []

	for y in range(height):
		for x in range(width):
			r, g, b = img_rgb[y, x]
			result.append([r, g, b])
	
	result_array = numpy.array([result])

	return result_array

def	main():
	ft_load()

if __name__ == "__main__":
	main()
