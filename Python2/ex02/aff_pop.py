from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

def suffixes(value):
	"""
	Handle the 'M' and 'k' after the numbers
	"""

	value = str(value).strip()

	if value.endswith("M"):
		return float(value[:-1]) * 1000000
	elif value.endswith("k"):
		return float(value[:-1]) * 1000

	return float(value)


def	format_millions(val, pos):
	"""
	Format axis numbers to accomodate the 'M'
	"""
	return f"{val:g}M"



def	aff(data_set: pd.DataFrame):
	"""
	Displays the country information of the campus.
	"""

	country = "France"

	country_row = data_set[data_set["country"] == country]
	years = country_row.columns[1:252].astype(int)
	values = country_row.iloc[0, 1:252].map(suffixes)

	country2 = "Belgium"

	country_row2 = data_set[data_set["country"] == country2]
	values2 = country_row2.iloc[0, 1:252].map(suffixes)

	plt.plot(years, values/1000000, label=country, color="green")
	plt.plot(years, values2/1000000, label=country2, color="blue")

	plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
	
	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.title("Population Projections")
	plt.legend(loc="lower right")

	plt.show()


def	main():
	data_set = load("population_total.csv")
	aff(data_set)


if __name__ == "__main__":
	main()