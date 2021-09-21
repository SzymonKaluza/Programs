# 14.08.2021
def main():
    number = int(input("Podaj numer zadania: "))
    if number == 1:
        exercise_1()
    if number == 2:
        exercise_2()


def exercise_1():
    print("5 + 3 = ", 5 + 3)
    print("10 - 2 = ", 10 - 2)
    print("24 : 3 = ", 24/3)
    print("2 * 4 = ", 2*4)


def exercise_2():
    number = 9
    print("Moja ulubiona liczba to: " + str(number))


main()
