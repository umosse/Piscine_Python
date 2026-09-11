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


def to_morse(message: str) -> str:
    cypher = ''
    for char in message:
        if char.isalnum() or char.isspace():
            cypher += NESTED_MORSE[char.upper()]
        else:
            raise AssertionError("Error: wrong arguments")
    return cypher
