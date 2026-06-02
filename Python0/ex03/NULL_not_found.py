def NULL_not_found(object: any) -> int:
	if (object is None or object == 0 or object == "" or object != object):
		if (object is None):
			print("Nothing:", object, type(object))
		elif (type(object) is int):
			print("Zero:", object, type(object))
		elif (type(object) is float):
			print("Cheese:", object, type(object))
		elif (type(object) is bool):
			print("Fake:", object, type(object))
		elif (type(object) is str):
			print("Empty:", object, type(object))
	else:
		print("Type not found")
		return 1
	return 0