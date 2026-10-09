# vyhodnocení kolize

# box
x1 = 2
x2 = 6
y1 = 1.5
y2 = 7


xb = float(input("Zadej x souřadnici panáčka"))
yb = float(input("Zadej y souřsdnici panáčka"))

#vyhodnocování
if xb > x1 and xb < x2 and yb > y1 and yb < y2:
    print("bod x =" + str(xb) + "bod y =" + str(yb) + "tyto body kolizují s boxem")
elif xb >= x1 and xb <= x2 and yb >= y1 and yb <= y2:
    print("bod x =" + str(xb) + "bod y =" + str(yb) + "tyto body jsou na kraji boxu")
else:
    print("bod x =" + str(xb) + "bod y =" + str(yb) + "tyto body jsou mimo box")