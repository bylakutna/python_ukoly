#KONTROLA PRVOČÍSLA
import math
print("kontrola prvočísla")
cislo = int(input("Zadej přirozené číslo: "))
y = 3
je_prvocislo = True
if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False

while y < math.sqrt(cislo):
    if cislo % y == 0:
        je_prvocislo = False
        break
    y += 2

if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslo")
else:
    print(f"Číslo {cislo} není prvočíslo")