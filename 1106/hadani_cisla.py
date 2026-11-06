import random
tc = random.randint(1,20)
tip = 0
pokus = 0

while tip != tc:
    pokus += 1
    tip = int(input(f"pokus: {pokus} Zadej svůj tip: "))
    if pokus < 5 and tip > 20 or pokus < 5 and tip < 1:
        print("Zadej číslo v rozsahu 1-20. pokus se ti nepočítá")
        pokus -= 1
    elif pokus < 5 and tip == tc:
        print(f"Gratulujeme! Uhodl jsi číslo {tc} na {pokus}. pokus.")
    elif pokus < 5 and tip > tc:
        print("tip je vetší než tajné číslo")
    elif pokus < 5 and tip < tc:
        print("tip je menší než tajné číslo")
    else:
        print("Bohužel jsi neuhodl tajné číslo")
        tip = tc