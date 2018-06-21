import random
random.seed()

Zahl1 = random.randint(1,10)
Zahl2 = random.randint(1,10)
Ergebnis = Zahl1 + Zahl2

print("Die Aufgabe:",Zahl1,"+",Zahl2)
print("Bitte eine Zahl eingeben:")
Eingabe = int(input())

if Eingabe == Ergebnis:
	print(Eingabe,"ist richtig")
elif Eingabe < 0 or Eingabe > 100:
	print (Eingabe,"ist ganz falsch")
elif Ergebnis - 1 <= Eingabe <= Ergebnis + 1:
	print(Eingabe,"ist ganz nahe dran")
else:
	print(Eingabe,"ist falsch")
	
print("Ergebnis:",Ergebnis)