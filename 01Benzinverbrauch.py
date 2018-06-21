print("Aufgabe 1" )

print("gefahrene Strecke (Km):")
strecke = float(input())

print("verbrauchtes Benzin (l):")
benzin = float(input())

verbrauch = (benzin * 100.) / strecke
print("Es wurden im Mittel", verbrauch,"Liter auf 100Km verbraucht")