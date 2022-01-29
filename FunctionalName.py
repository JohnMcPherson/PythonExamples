def combinedName(first, last) :
    return first + last

def hello():
    firstName = input("Enter your firstName: ")
    surname = input("Enter you surname: ")
    return combinedName(firstName, surname)

print(hello())