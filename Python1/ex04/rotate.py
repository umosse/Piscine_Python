from load_image import ft_load
import cv2
import numpy as numpy


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
	return zoomed_img


loaded_img = ft_load("animal.jpeg")

zoomed = ft_rotate(loaded_img)
print(zoomed)

cv2.imshow("", zoomed)
cv2.waitKey(0)
cv2.destroyAllWindows()

def	main():
	img_array = ft_load("animal.jpeg")
	ft_rotate(img_array)

if __name__ == "__main__":
	main()