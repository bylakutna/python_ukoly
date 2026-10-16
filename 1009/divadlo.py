# vstupenka do divadla

pocet_osob = int(input("Zadejte počet osob: "))
cenaz = 500

if pocet_osob >= 4:
    cena = cenaz * 0.75
elif pocet_osob <= 3:
    vek = int(input("Zadejte svůj věk: "))
    if vek > 65:
        cena = cenaz * 0.8
    elif vek < 26:
        student = str(input("Jste student? (ano/ne): "))
        if student == "ano":
          cena = cenaz * 0.7
        else:
            cena = cenaz
    else:
        cena = cenaz
else:
    cena = cenaz

print(f"Cena vstupenky pro jednoho je: {cena} Kč")
if pocet_osob > 1:
    celkova_cena = cena * pocet_osob
    print(f"Celková cena pro {pocet_osob} osoby/ů je: {celkova_cena} Kč")

