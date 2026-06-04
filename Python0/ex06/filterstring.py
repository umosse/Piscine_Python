import sys
from ft_filter import ft_filter


def main():
	"""
	Program accepts exactly 2 arguments
		1: a string of words
		2: an int
		It returns a list of words longer than the int
	"""
	args = sys.argv
	if len(args) > 3:
		# raise AssertionError("Too many arguments")
		print("AssertionError: Wrong arguments")
		sys.exit(1)
	if len(args) < 3:
		print("AssertionError: Wrong arguments")
		sys.exit(1)
	if type(args[1]) is not str:
		print("AssertionError: Wrong arguments (not str)")
		sys.exit(1)
	if not args[1].isalpha():
		for char in args[1]:
			if char != " " and not char.isalpha():
				print("AssertionError: Wrong arguments (wrong str)")
				sys.exit(1)
	try:
		intarg = int(sys.argv[2])
	except:
		print("AssertionError: Wrong arguments (not int)")
		sys.exit(1)
	wordlist = ft_filter(lambda word: len(word) > intarg, args[1].split())
	print(list(wordlist))



if __name__ == "__main__":
	main()