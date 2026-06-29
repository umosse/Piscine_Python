from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import cv2


array = ft_load("landscape.jpg")

inverted = ft_invert(array)
inverted = cv2.cvtColor(inverted, cv2.COLOR_RGB2BGR)
red = ft_red(array)
red = cv2.cvtColor(red, cv2.COLOR_RGB2BGR)
green = ft_green(array)
green = cv2.cvtColor(green, cv2.COLOR_RGB2BGR)
blue = ft_blue(array)
blue = cv2.cvtColor(blue, cv2.COLOR_RGB2BGR)
grey = ft_grey(array)
grey = cv2.cvtColor(grey, cv2.COLOR_RGB2BGR)

print(ft_invert.__doc__)

cv2.imshow("", inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
