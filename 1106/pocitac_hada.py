print("zahrajeme jsi hru a já se pokusím uhodnout tvoje číslo v rozsahu 1-100." \
" Ty mi budeš říkat jestli je muj tip v větší, m menší nebo s správně.")
dolni = 1
horni = 100
tip = 0
pokus = 0
uhodni = 0
while uhodni != "s":
    pokus += 1
    if pokus > 7:
        print("Bohužel jsem neuhodl tajné číslo")
        break
    tip = int((dolni + horni) // 2)
    print(f"pokus: {pokus} Můj tip je: {tip}")
    uhodni = input("Zadej jestli je můj tip v větší, menší nebo s správně: ")
    elif uhodni == "v":
        dolni = (tip + 1)
    elif uhodni == "m":
        horni = (tip - 1)
    elif uhodni == "s":
        print(f"Gratulujeme! Uhodl jsem číslo {tip} na {pokus}. pokus.")
