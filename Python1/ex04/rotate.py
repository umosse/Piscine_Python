from load_image import ft_load
import cv2
import numpy as numpy


def ft_transpose(img: numpy.ndarray) -> numpy.ndarray:
	"""
	
	"""

	rows = img.shape[0]
	columns = img.shape[1]
	channels = img.shape[2]

	transposed = numpy.zeros((columns, rows, channels), dtype=img.dtype)

	for r in range(rows):
		for c in range(columns):
			transposed[c][r] = img[r][c]
	
	return(transposed)

def ft_rotate(img_array: numpy.ndarray) -> numpy.ndarray:
	"""
	
	"""

	height, width = img_array.shape[:2]
	center_y = height // 2
	center_x = width // 2

	start_y = center_y - 200
	end_y = center_y + 200
	start_x = center_x - 100
	end_x = center_x + 300

	cropped_img = img_array[start_y:end_y, start_x:end_x]

	zoomed_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2GRAY)
	zoomed_img = zoomed_img[:, :, numpy.newaxis]

	z_height, z_width, z_channel = zoomed_img.shape
	print('The shape of image is:', (z_height, z_width, z_channel))
	print(zoomed_img)

	rotated_img = ft_transpose(zoomed_img)
	r_height, r_width, r_channel = rotated_img.shape
	print('New shape after transpose:', (r_height, r_width))

	return rotated_img


def	main():
	img_array = ft_load("animal.jpeg")
	rotated = ft_rotate(img_array)
	print(rotated)

	cv2.imshow("", rotated)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()