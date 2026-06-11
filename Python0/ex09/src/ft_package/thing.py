import sys


def main():
	args = sys.argv
	if len(args) != 2:
		print("AssertionError: Wrong number of arguments")
		sys.exit(1)
	NESTED_MORSE = {'A': '.- ', 'B': '-... ',
					'C': '-.-. ', 'D': '-.. ', 'E': '. ',
					'F': '..-. ', 'G': '--. ', 'H': '.... ',
					'I': '.. ', 'J': '.--- ', 'K': '-.- ',
					'L': '.-.. ', 'M': '-- ', 'N': '-. ',
					'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
					'R': '.-. ', 'S': '... ', 'T': '- ',
					'U': '..- ', 'V': '...- ', 'W': '.-- ',
					'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
					'1': '.---- ', '2': '..--- ', '3': '...-- ',
					'4': '....- ', '5': '..... ', '6': '-.... ',
					'7': '--... ', '8': '---.. ', '9': '----. ',
					'0': '----- ', ' ': '/ '}
	message = args[1]
	cypher = ''
	for char in message:
		if char.isalnum() or char == ' ':
			cypher += NESTED_MORSE[char.upper()]
		else:
			print("AssertionError: Wrong arguments")
			sys.exit(1)
	print(cypher)


if __name__ == "__main__":
	main()
