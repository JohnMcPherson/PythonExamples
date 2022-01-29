def create_alt_string_or_nothing(number_to_test, divisor, alt_string):
    if number_to_test % divisor == 0:
        return alt_string
    else:
        return ""


def number_to_fizz_buzz_string(number):
    fizz_buzz_string = create_alt_string_or_nothing(number, 3, "fizz") \
                       + create_alt_string_or_nothing(number, 5, "buzz")
    if fizz_buzz_string == "":
        return number
    else:
        return fizz_buzz_string


for number in range(1, 100):
    print(number_to_fizz_buzz_string(number))
