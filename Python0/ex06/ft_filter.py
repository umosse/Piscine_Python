def ft_filter(function, iterable):
	"""Apply a function to an iterable and return the items which return true."""
	if function:
		return (item for item in iterable if function(item))
	return (item for item in iterable if item)
