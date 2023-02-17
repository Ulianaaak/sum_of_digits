some_digit = 13
def sum_of_digits(some_number):
    try:
        number_of_digit = len(str(some_number))
        result = 0
        for digit in range(number_of_digit):
            result += int(str(some_digit)[digit])
        return result
    except ValueError:
        return "Че, самый умный?"

print(sum_of_digits(some_digit))
#some_digit = 13 => 4
#some_digit = 17478 => 27
#some_digit = {"ключ"} => Че, самый умный?