# Pyydä käyttäjältä vuosiluku
vuosi = int(input("Anna vuosiluku: "))

# Tarkista, onko vuosi karkausvuosi
if (vuosi % 4 == 0 and vuosi % 100 != 0) or vuosi % 400 == 0:
    print(vuosi, "on karkausvuosi.")
else:
    print(vuosi, "ei ole karkausvuosi.")
