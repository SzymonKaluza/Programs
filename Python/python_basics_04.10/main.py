def main():
    exercise_01()


def exercise_01():
    digits = []
    for digit in range(0, 10):
        digits.append(digit)
    print(digits)
    print("pierwsze trzy elementy to:", digits[0:3])
    print("Trzy elementy w środku listy to:", digits[3:6])
    print("Ostatnie trzy elementy listy to:", digits[-3:])
    numbers = digits[:]
    for number in range(10, 1001):
        numbers.append(number)
    print("Cyfry to: ", digits)
    print("Liczby natomiast to: ", numbers)
    print("Popełniłeś błąd głuptasie !!!")
    print("Cyfry to nie liczby!!!")
    print("Cyfry to: ", digits)
    print("Liczby natomiast to: ", numbers[10:1001])


main()
