from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def	aff(data_set: pd.DataFrame):
	"""
	Displays the country information of the campus.
	"""

	country = "France"

	country_row = data_set[data_set["country"] == country]
	years = country_row.columns[1:].astype(int)
	values = country_row.iloc[0, 1:].astype(float)

	plt.plot(years, values)
	
	plt.xlabel("Year")
	plt.ylabel("Life expectancy")
	plt.title(f"{country} Life expectancy Projections")

	plt.show()


def	main():
	data_set = load("life_expectancy_years.csv")
	aff(data_set)


if __name__ == "__main__":
	main()