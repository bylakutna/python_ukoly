a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
if a < b and a < c:
    min = a
elif b < a and b < c:
    min = b
else:
    min = c
if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c
if (a == min or a == max) and (b == min or b == max):
    print(min, c, max)
elif (b == min or b == max) and (c == min or c == max):
     print(min, a, max)
else:
    print(min, b, max)