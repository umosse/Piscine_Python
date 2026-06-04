import sys


def main():
	"""Display the sum of the upper-case, lower case and puctuation
	characters as well as digits and spaces in a single string argument."""
	args = sys.argv
	if len(args) > 2:
		# raise AssertionError("Too many arguments")
		print("AssertionError: Too many arguments")
		sys.exit(1)
	if len(args) < 2:
		print("Please provide an argument")
		sys.exit(1)

	upper_case = 0
	lower_case = 0
	punctuation = 0
	digits = 0
	spaces = 0

	text = args[1]
	print("The text contains", len(text), "characters:")

	for char in text:
		if char == " " or char == "\n":
			spaces += 1
		elif char.isdigit():
			digits += 1
		elif char.isupper():
			upper_case += 1
		elif char.islower():
			lower_case += 1
		else:
			punctuation += 1
	if upper_case > 0:
		print(upper_case, "upper letters")
	if lower_case > 0:
		print(lower_case, "lower letters")
	if punctuation > 0:
		print(punctuation, "punctuation marks")
	if spaces > 0:
		print(spaces, "spaces")
	if digits > 0:
		print(digits, "digits")


if __name__ == "__main__":
	main()
