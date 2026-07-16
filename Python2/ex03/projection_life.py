from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter


def	aff(data_set: pd.DataFrame, data_set_2: pd.DataFrame):
	"""
	Displays the the life expectancy of a country relative to its gdp.
	"""

	life_exp = []
	income = []

	for index, row in data_set.iterrows():
		country = row['country']
		life_exp.append(data_set.loc[data_set['country'] == country, '1900'].values[0])
		income.append(data_set_2.loc[data_set_2['country'] == country, '1900'].values[0])


	plt.scatter(income, life_exp)

	plt.xlabel("Gross domestic product")
	plt.ylabel("Life expectancy")
	plt.title('1900')

	plt.show()


def	main():
	data_set = load("life_expectancy_years.csv")
	data_set_2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	aff(data_set, data_set_2)


if __name__ == "__main__":
	main()