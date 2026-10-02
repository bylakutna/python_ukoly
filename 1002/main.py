x = -5

# príkaz větvení
#if x >= 0:
#    print(f"{x} je kladné číslo nebo nula")
#else:
#    print(f"{x} je záporné číslo")
#    x = -x
#print(f"Absolutní hodnota: {x}")
#print(f"Absolutní hodnota: {abs(x)}")

# druhá varianta
if x > 0:
    print(f"{x} je kladné číslo")
elif x == 0:
    print(f"{x} je nula")
elif x < 0:
    print(f"{x} je záporné číslo")
print(f"Absolutní hodnota: {abs(x)}")