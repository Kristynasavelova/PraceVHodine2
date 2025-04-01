predmety = ["Ucebni praxe", "Matematika", "Programovani", "Anglicky jazyk", "Cesky jazyk", "Pocitacove site", "Aplikacni software"]

DelkaPole = len(predmety)
print(DelkaPole)

for vypis in predmety:
    print(vypis)

DalsiPredmet = str(input("zadejte jeden předmět,který v seznamu ještě není: "))
pridani = predmety.append(DalsiPredmet)

Odstranenni = predmety.remove("Cesky jazyk")

serazeni = predmety.sort

obracenePoradi = predmety.reverse
print(obracenePoradi)