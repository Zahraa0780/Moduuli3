# Pyydä käyttäjältä sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna sukupuoli (M/N): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkista hemoglobiiniarvo ja anna arvio
if sukupuoli == "N":
    if 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on poikkeava.")
elif sukupuoli == "M":
    if 134 <= hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on poikkeava.")
else:
    print("Virheellinen sukupuoli.")
