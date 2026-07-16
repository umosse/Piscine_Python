import pandas as pd


def load(path: str) -> pd.DataFrame:
	"""
	Takes a path as argument and returns a data set after writing its dimensions.
	"""

	try:
		data_set = pd.read_csv(path)

		dimensions = data_set.shape
		print('Loading dataset of dimensions', dimensions)

		return data_set
	
	except (FileNotFoundError, pd.errors.ParserError, pd.errors.EmptyDataError) as err:
		print("Error loading file at", path, err)
		return None
	except Exception as err:
		print("An unexpected error occured", err)
		return None
