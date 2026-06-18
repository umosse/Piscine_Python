import numpy as numpy

def slice_me(family: list, start: int, end: int) -> list:
	"""
	
	"""

	if type(family) is not list:
		print("Error: Not a list")
		exit(1)


	family_array = numpy.array(family)

	if numpy.issubdtype(family_array.dtype, numpy.number) is False:
		print("Error: Wrong list type")
		exit(1)

	family_first = family_array.shape[0]
	family_second = family_array.shape[1]

	new_family_array = family_array[start:end]
	new_family_first = new_family_array.shape[0]
	new_family_second = new_family_array.shape[1]

	print("My shape is :", (family_first, family_second))
	print("My new shape is :", (new_family_first, new_family_second))

	return(new_family_array)



def	main():
	slice_me()

if __name__ == "__main__":
	main()
