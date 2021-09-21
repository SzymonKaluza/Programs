def main():
    exercise_01()


def exercise_01():
    skaluza = {'imię' : 'szymon',
               'nazwisko' : 'kaluza',
               'miejscowość' : 'daleko',
               }
    doles = {'imię' : 'Dawid',
             'nazwisko' : 'oles',
             'miejscowość' : 'czestochowa'
    }
    jbitner = {'imie' : 'jakub',
               'nazwisko' : 'bitner',
               'miejscowość' : 'czestochowa'
    }
    dictionary = {
        'skaluza' : skaluza,
        'doles' : doles,
        'jbitner' : jbitner,
    }
    for key, value  in dictionary.items():
        for data in value.items():
            print(data)


main()
