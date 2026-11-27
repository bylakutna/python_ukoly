def cifra_na_znak(hodnota):
    hodnota = int(hodnota)
    if hodnota >= 0 and hodnota <= 9:
        return str(hodnota)
    elif hodnota >= 10 and hodnota <= 15:
        if hodnota == 10:
            return "A"
        elif hodnota == 11:
            return "B"
        elif hodnota == 12:
            return "C"
        elif hodnota == 13:
            return "D"
        elif hodnota == 14:
            return "E"
        elif hodnota == 15:
            return "F"
    else:
        print ("neco se pokazilo. Hodnota je mimo rozsah 0-15")
        return None
def preved_soustavu(cislo, zaklad):
    prevedene_cislo = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        cislo //= zaklad
        prevedene_cislo = cifra_na_znak(zbytek) + prevedene_cislo
    return prevedene_cislo

print(preved_soustavu(10, 2))
print(preved_soustavu(25, 8))
print(preved_soustavu(255, 16))

