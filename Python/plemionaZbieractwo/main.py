pikinier = 25
Topornik = 0.4 * pikinier
lekki = 3.2 * pikinier
ambitni = 90 * pikinier
ambitni2 = 90 * Topornik
ambitni3 = 90 * lekki
cierpliwi = 36 * pikinier
cierpliwi2 = 36 * Topornik
cierpliwi3 = 36 * lekki
zawodowi = 18 * pikinier
zawodowi2 = 18 * Topornik
zawodowi3 = 90 * lekki
specjaliści = 12 * pikinier
specjaliściM = 12 * Topornik
specjaliścil = 12 * lekki
liczbaPik = int(input("Podaj liczbę pikinierów: "))
liczbaTopor = int(input("Podaj liczbę mieczników: "))
liczbalekki = int(input("Podaj liczbę lekkich kawalerzystów: "))
wszystkoP = (liczbaPik * pikinier) / (ambitni + cierpliwi + zawodowi + specjaliści)
wszystkoM = (liczbaTopor * Topornik) / (ambitni2 + cierpliwi2 + zawodowi2 + specjaliściM)
wszystkoL = (liczbalekki * lekki) / (ambitni3 + cierpliwi3 + zawodowi3 + specjaliścil)
wynikAmbitniP = (wszystkoP * ambitni) / pikinier
wynikAmbitniM = (wszystkoM * ambitni2) / Topornik
wynikAmbitnil = (wszystkoL * ambitni3) / lekki
wynikCierpliwiP = (wszystkoP * cierpliwi) / pikinier
wynikCierpliwiM = (wszystkoM * cierpliwi2) / Topornik
wynikCierpliwiL = (wszystkoL * cierpliwi3) / lekki
wynikZawodowiP = (wszystkoP * zawodowi) / pikinier
wynikZawodowiM = (wszystkoM * zawodowi2) / Topornik
wynikZawodowiL = (wszystkoL * zawodowi3) / lekki
wynikSpecjaliściP = (wszystkoP * specjaliści) / pikinier
wynikSpecjaliściM = (wszystkoM * specjaliściM) / Topornik
wynikSpecjaliściL = (wszystkoL * specjaliścil) / lekki
print("Podziel to na następujące części:")
print("Dla ambitnych:\n\tPiknierów: ", wynikAmbitniP, "\n\tToporników: ", wynikAmbitniM)
print("\tKawalerzystów: ", wynikAmbitnil)
print("Dla cierpliwych:\n\tPiknierów: ", wynikCierpliwiP, "\n\tToporników: ", wynikCierpliwiM)
print("\tKawalerzystów: ", wynikCierpliwiL)
print("Dla zawodowych: \n\tPikinierów: ", wynikZawodowiP, "\n\tToporników: ", wynikZawodowiM)
print("\tKawalerzystów: ", wynikZawodowiL)
print("Dla specjalistów: \n\tPikinierów: ", wynikSpecjaliściP, "\n\tToporników: ", wynikSpecjaliściM)
print("\tKawalerzystów: ", wynikSpecjaliściL)
