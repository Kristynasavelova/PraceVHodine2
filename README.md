# Obsah
- [1.funkce]()
- [2.funkce]()
- [3.funkce]()
- [4.funkce]()
- [5.funkce]()
- [6.funkce]()
- [7.funkce]()
  
## 1. Funkce-pole
pole, kde je seznam předmětů:
predmety = ["Ucebni praxe", "Matematika", "Programovani", "Anglicky jazyk", "Český jazyk", "Pocitacove site", "Aplikacni software"]

## 2.Funkce-délka pole
DelkaPole = len(predmety)
print(DelkaPole)
-vypíše kolik je v seznamu předmětů

## 3.Funkce-For cyklus
for vypis in predmety:
    print(vypis)  
-vypíše všechny předměty v seznamu

## 4.Funkce-append
DalsiPredmet = str(input("zadejte jeden předmět,který v seznamu ještě není: "))
predmety.append(DalsiPredmet)
-připíše to, co zadá uživatel na konec seznamu

## 5.Funkce-remove
if "Český jazyk" in predmety:
  predmety.remove("Český jazyk")
else:
   print("předmět Český jakzyk není v seznamu")
-odstraní danou věc ze seznamu

## 6.Funkce-sort
predmety.sort()
print(predmety)
-seřadí předměty od A do Z a vypíše seznam

## 7.Funkce-reverse
predmety.reverse()
print(predmety)
-vypíše seznam obráceně



