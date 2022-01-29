inputString = "Here is my string"

def characterPrinter(input) :
    for character in input:
        print(character)

characterPrinter(inputString)
print()
print()
characterPrinter(reversed(inputString))