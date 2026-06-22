import cv2


def ft_load(path: str) -> list:
	"""
	
	"""

	print(path)

	img = cv2.imread(path)

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	return img_rgb
