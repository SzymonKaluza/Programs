def main():
    exercise_1()


def exercise_1():
    dictionary = {
        'pętla' : 'Powtarzająca się czynność wykonywana przez program',
        'iteracja' : 'przesunięcie uwagi przez kolejne elemty zbioru',
        'Zagnierzdżenie' : 'Umieszczenie struktury w innej strukturze',
        'pycharm' : 'Oprogramowanie firmy jetbrain umożliwiające tworzenie oraz kompilację oprogramowania',
        'kompilacja' : 'Zmiana kodu na zrozumiały dla użądzenia',
    }
    for key, value in dictionary.items():
        print(key + " : " + value)

main()