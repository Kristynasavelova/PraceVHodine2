predmety = ["Ucebni praxe", "Matematika", "Programovani", "Anglicky jazyk", "Český jazyk", "Pocitacove site", "Aplikacni software"]

DelkaPole = len(predmety)
print(DelkaPole)

for vypis in predmety:
    print(vypis)  

DalsiPredmet = str(input("zadejte jeden předmět,který v seznamu ještě není: "))
predmety.append(DalsiPredmet)

if "Český jazyk" in predmety:
  predmety.remove("Český jazyk")
else:
   print("předmět Český jakzyk není v seznamu")

predmety.sort()
print(predmety)
predmety.reverse()
print(predmety)
