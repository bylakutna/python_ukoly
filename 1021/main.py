a = int(input("Zadej číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
min = a
max = a
if b < min:
    min = b
elif b > max:
    max = b
if c < min:
    min = c
elif c > max:
    max = c
print(f"minimum: {min}, maximum: {max}")