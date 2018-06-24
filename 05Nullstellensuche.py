def Funktion(x):
	return 5 * x - x**2

def Ergebnis(final):
	print("Die Nullstelle ist gefunden. Das Ergebnis liegt bei: ",final)
	exit()

def Eingabe():
	print("Exemplarische Darstellung einer Nullstellensuche durch Intervallverschachtellung anhand der Funktion f = 5x - x^2. Geben Sie bitte die Grenzen des Intervalls an, in dem gesucht werden soll. (Vorsicht, (Funktion(oben)*Funktion(unten) muss negativ sein!)")
	print("Geben Sie nun bitte Anfang und Ende ein.")
	error = 1
	while error == 1:
		Intervallanfang = float(input("Intervallanfang:"))				#Intervall einlesen
		Intervallende = float(input("Intervallende:"))
		if (Funktion(Intervallanfang) * Funktion(Intervallende)) < 0:	#Testen ob f(oben)*f(unten) negativ; bedeutet zwischen den beiden Werten muss eine Nullstelle sein; das Programm funktioniert nicht wenn dazwischen keine Nullstelle liegt oder mehrere
			error = 0			#Wenn ja, Eingabeschleife unterbrechen, regulaere Suche beginnen
		elif Funktion(Intervallanfang) == 0:				#Wenn Nullstelle Anfangs- oder Endwert ausgeben und beenden
			print("Nullstelle Anfangswert.")
			Ergebnis(Intervallanfang)
		elif Funktion(Intervallende) == 0:
			print("Nullstelle ist Endwert.")
			Ergebnis(Intervallende)
		else:					#Sonst gilt f(oben)*f(unten) positiv, nicht erlaubt. Schleife von vorn
			print("Funktionswerte:", Funktion(Intervallanfang),Funktion(Intervallende))
			print("Das war wohl nichts - noch einmal.")

	print("Funktionswerte von Intervallanfang:", Funktion(Intervallanfang), "und Intervallende:",Funktion(Intervallende))
	return Intervallanfang , Intervallende


Anfang, Ende = Eingabe()
Fehler = abs(Anfang - Ende)
print("Fehler: ",Fehler)
epsilon = .00001

while Fehler > epsilon:
	Mittelwert = (Anfang + Ende) / 2.
	print("Mitte:",Mittelwert)
	if Funktion(Mittelwert) == 0:
		Ergebnis(Mittelwert)
	if (Funktion(Anfang) * Funktion(Mittelwert) < 0):	#Wenn pos. * neg. Wert (oder umgekehrt) neg. ist, dann liegt dasw. eine Nullstelle
		Ende = Mittelwert	# Der obere Teil des Intervalls wird weggeworfen,
	else:					# wenn anfang & mittel postiv ist, muss Nullstelle zwischen Mitte und Ende liegen
		Anfang = Mittelwert	
	Fehler = abs(Anfang - Ende)

print("Naeherungsergebnis")
Ergebnis(Anfang + Ende / 2.)
Ergebnis(Mittelwert)	#muesste eigentlich genauso gehen
