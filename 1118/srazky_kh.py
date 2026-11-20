import urllib.request
url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"
odpoved = urllib.request.urlopen(url)
celkem_srazky = 0
pocet_dni = 0
radek = odpoved.readline()
while bool(radek):
    text_radku = radek.decode("utf-8")
    denni_srazky = float(text_radku)
    if denni_srazky >= 0:
        celkem_srazky += denni_srazky
        pocet_dni += 1
    radek = odpoved.readline()
odpoved.close()
print(f"Celkem srážky: {celkem_srazky} mm za {pocet_dni} dní.")