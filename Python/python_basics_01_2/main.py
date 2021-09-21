def main():
    number = int(input("Podaj numer zadania: "))
    if number == 1:
        exercise_1()
    if number == 2:
        exercise_2()
    if number == 3:
        exercise_3()
    if number == 4:
        exercise_4()
    if number == 5:
        exercise_5()
    else:
        print("Podano niewłaściwy numer zadania!")


def exercise_1():
    name = "szymon"
    print("Witaj " + name.title() + ". Czy chcesz poznać pythona?")


def exercise_2():
    name = "szymon"
    print(name.upper())
    print(name.lower())
    print(name.title())


def exercise_3():
    name = "viktor e. frankl"
    print(" " + name.title() + " powiedział kiedyś:\n Pomiędzy bodźcem i reakcją jest"
                               " przestrzeń:\n w tej przestrzeni leży wolność i moc"
                               " wyboru naszej odpowiedzi.")


def exercise_4():
    name = "viktor e. frankl"
    message = "powiedział kiedyś:\n Pomiędzy bodźcem i reakcją jest przestrzeń:" \
              "\n w tej przestrzeni leży wolność i moc wyboru naszej odpowiedzi."
    print(name.title() + message)


def exercise_5():
    name = " viktor e. frankl"
    print((name.title()).strip())


main()
