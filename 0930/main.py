# ************************************************
# kalkulačka spropitného
# 30. 9. 2026
# ************************************************


print("KALKULAČKA SPROPITNÉHO")                  # tisk nadpisu
celkova_cena = float(input("Zadej celkovou cenu: "))
#celkova_cena = float(celkova_cena)               # převod na číslo
spropitne = int(input("Zadej spropitné v procentech: "))  # zadání spropitného
pocet_lidi = int(input("Zadej počet lidí: "))          # zadání počtu lidí

celkova_cena = celkova_cena + celkova_cena * spropitne / 100  # výpočet ceny s spropitným
print(celkova_cena)

cena_na_osobu = round(celkova_cena / pocet_lidi + 0,5)  # výpočet ceny na osobu
print("Každý zaplatí:", cena_na_osobu)