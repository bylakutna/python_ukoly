# D E N N Í    P O Z D R A V


time = float(input("Zadejte čas v hodinách: "))
if time < 0:
    print("Čas nemůže být záporný")
elif time >= 24:
    print("zadejte čas v rozmezí 0 - 23 hodin")
elif time < 5:
    print("Dobrou noc")
elif time < 10:
    print("Dobré ráno")
elif time < 12:
    print("Dobré dopoledne")
elif time == 12:
    print("Dobré poledne")
elif time < 16:
    print("Dobré odpoledne")
elif time < 22:
    print("Dobrý večer")
elif time >=22:
    print("Dobrou noc")