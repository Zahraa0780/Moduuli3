# Pyydä käyttäjältä kuhan pituus senttimetreinä
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Tarkista, onko kuha alamittainen
alamittainen_raja = 37
if kuhan_pituus < alamittainen_raja:
    puuttuvat_sentit = alamittainen_raja - kuhan_pituus
    print("Kuha on alamittainen. Laske kuha takaisin järveen ja puuttuu", puuttuvat_sentit, "senttiä alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallittu pituus.")
