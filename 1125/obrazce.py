print("VÍTEJ V PROGRAMU PRO KRESLENÍ GEOMETRICKÝCH TVARŮ")
pokracovat = "ano"
vyska = 0
syrka = 0
obrazec = ""

while pokracovat == "ano":
    obrazec = input("Zadej tvar, který chceš nakreslit: ")
    if obrazec == "c":
        vyska = int(input("Zadej délku strany čtverce: "))
        pocitadlo = 0
        while pocitadlo < vyska:
            print("*" * vyska)
            pocitadlo += 1
    elif obrazec == "o":
        syrka = int(input("Zadej šířku obdélníku: "))
        vyska = int(input("Zadej výšku obdélníku: "))
        pocitadlo = 0
        while pocitadlo < vyska:
            print("*" * syrka)
            pocitadlo += 1
    elif obrazec == "tpl":
        vyska = int(input("Zadej základnu trojúhelníku: "))
        pocitadlo = 1
        while pocitadlo <= vyska:
            print("*" * pocitadlo)
            pocitadlo += 1
    elif obrazec == "tpp":
        vyska = int(input("Zadej základnu trojúhelníku: "))
        pocitadlo = 1
        while pocitadlo <= vyska:
            mezery = vyska - pocitadlo
            print(" " * mezery + "*" * pocitadlo)
            pocitadlo += 1
    elif obrazec == "tr":
        vyska = int(input("Zadej základnu trojúhelníku: "))
        if vyska % 2 == 0:
            pocitadlo = 2
            while pocitadlo <= vyska:
                mezery = (vyska - pocitadlo)//2
                print(" " * mezery + "*" * pocitadlo)
                pocitadlo += 2
        else:
            pocitadlo = 1
            while pocitadlo <= vyska:
                mezery = (vyska - pocitadlo)//2
                print(" " * mezery + "*" * pocitadlo)
                pocitadlo += 2
        while pocitadlo <= vyska:
            mezery = (vyska - pocitadlo)//2
            print(" " * mezery + "*" * pocitadlo)
            pocitadlo += 2
    else:
        print("Neplatný tvar. Zkus to znovu.")

    pokracovat = input("Chceš nakreslit další tvar? ")
    while pokracovat != "ano" and pokracovat != "ne":
        pokracovat = input("Neplatná volba. Zadej 'ano' nebo 'ne': ")