def main():
    guests = ['stephen covey', 'robert cialdini', 'nicolo machiavelli', ]
    exercise_1(guests[0])
    exercise_1(guests[1])
    exercise_1(guests[2])
    guests.append(exercise_2(guests.pop()))
    print(guests)




def exercise_1(guest):
    print("szanowny panie " + guest.title() +
          "\nZapraszam Pana na uroczystą kolację w dniu 15.08.2021 o godzinie 21:00\n")


def exercise_2(guest):
    print("Z przykrością zawiadamiamy że Pan" + guest.title() +
          " nie mógł przybyć z powodu nieoczekiwanej śmierci")
    score = 'mark zukerberg'
    return score


main()
