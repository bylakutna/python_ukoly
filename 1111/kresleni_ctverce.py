#KRESLENÍ ČTVERCE HVĚZDIČKAMA
x = 0
while True:
    otazka = input("Chceš vykreslit čtverec? ")
    if otazka == "ano":
        x = int(input("Jaká má být jeho strana? "))
        for i in range(x):
            print("*" * x)
    elif otazka == "ne":
        print("DĚKUJI ZA POUŽITÍ PROGRAMU")
        break
    else:
        print("Zkus to znovu, zadej pouze: ano/ne")