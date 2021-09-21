def main():
    exercise_1()
    exercise_2()
    exercise_3()


def exercise_1():
    names = ['dominika', 'dawid', 'kuba', 'maciej', ]
    print(names[0].title())
    print(names[1].title())
    print(names[2].title())
    print(names[3].title())


def exercise_2():
    names = ['dominika', 'dawid', 'kuba', 'maciej', ]
    print("Witaj " + names[0].title() + " w szkole pythona")
    print("Witaj " + names[1].title() + " w szkole pythona")
    print("Witaj " + names[2].title() + " w szkole pythona")
    print("Witaj " + names[3].title() + " w szkole pythona")


def exercise_3():
    vehicles = ['motor', 'bicycle', 'tram', 'car', 'bus', ]
    print("Najczęściej poruszam się za pomocą pojazdu który nazywa się : "
          "" + vehicles[-1] + ".\nJednak czasami zdarza mi się jeździć za pomocą: " + vehicles[1]
          + ".\nNigdy jednak nie korzystam z : " + vehicles[0] + ", " + vehicles[2] + ", " + vehicles[3] + "!")


main()
