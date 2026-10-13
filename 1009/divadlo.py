# vstupenka do divadla

vek = int(input("Zadejte svůj věk: "))
student = str(input("Jste student? (ano/ne): "))
pocet_osob = int(input("Zadejte počet osob: "))
cenaz = 500

if pocet_osob > 3:
    cena = cenaz * 0.75
elif vek < 26 and student == "ano":
    cena = cenaz * 0.7
elif vek > 65:
    cena = cenaz * 0.8
else:
    cena = cenaz

print(f"Cena vstupenky pro jednoho je: {cena} Kč")
if pocet_osob > 1:
    celkova_cena = cena * pocet_osob
    print(f"Celková cena pro {pocet_osob} osoby/ů je: {celkova_cena} Kč")

