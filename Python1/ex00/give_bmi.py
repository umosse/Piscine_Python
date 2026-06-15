import numpy as numpy


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""

	"""
	height_array = numpy.array(height)
	weight_array = numpy.array(weight)

	if height_array.size != weight_array.size:
		print("Error: Wrong list size")
		exit(1)

	bmi_array = numpy.array(weight_array / (height_array ** 2))

	return(bmi_array)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""

	"""
	bmi_array = numpy.array(bmi)
	bmi_limit = bmi_array < limit

	return(bmi_limit)



def	main():
	give_bmi()
	apply_limit()


if __name__ == "__main__":
	main()
