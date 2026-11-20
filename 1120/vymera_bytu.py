# vypocet celkove vymery bytu v m2
print("Vypocet celkove vymery bytu v m2")
pocet_mistnosti = int(input("Zadej pocet mistnosti: "))
if pocet_mistnosti <= 0:
    print("Pocet mistnosti musi byt kladne cislo.")
    exit()
celkova_vymera = 0
while True:
    for i in range(pocet_mistnosti):
        delka = float(input(f"Zadej delku mistnosti {i+1}: "))
        sirka = float(input(f"Zadej sirku mistnosti {i+1}: "))
        if delka <= 0 or sirka <= 0:
            print("Delka a sirka musi byt kladne cislo.")
            exit()
        vymera = delka * sirka
        celkova_vymera += vymera
    print(f"Celkova vymera bytu je: {celkova_vymera} m2")
    input