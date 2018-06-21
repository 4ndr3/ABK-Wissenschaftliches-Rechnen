import math
import random

def f(x):
	return math.sin(x)	#beliebige funktion als f definieren


#Variablen initialisieren
x_min = 0				# intervall [0,2pi] definieren 
x_max = 2. * math.pi
Schritte = 1000000		#1M Schritte
y_min = f(x_min)		#Es wird angenommen y_min sei f(x_min). Is Quatsch, wird in der for-Schleife tatsaechlich berechnet. Koennte auch auf jeden anderen Wert gesetzt werden.
y_max = y_min			#y_max Wert wird auch auf y_min gesetzt. Auch Quatsch.

for i in range(Schritte):
	x = x_min + (x_max - x_min) * float(i) / Schritte	#aktuelles x des Schrittes i ist das x-Intervall geteilt durch die Anzahl der Schritte mal dem akutellen schritt
	y = f(x)											# y ist einfach = f(x)
	if y < y_min:										# Das tatsaechliche y_min wird gefunden
		y_min = y
	if y > y_max:										# Das tatsaechliche y_max wird gefunden
		y_max = y


#Monte Carlo
Rechteck = (x_max - x_min) * (y_max - y_min)		# Rechteckflaeche wird definiert
Schritte2 = 1000000									# 1M Punkte
Mitte = 0											# Mitte definieren

for j in range(Schritte2):
	x = x_min + (x_max - x_min) * random.random()	# zu x wird ein zufaelliger aus dem Intervall von x addiert.
	y = y_min + (y_max - y_min) * random.random()	# zu y wird ein zufaelliger aus dem Intervall von y addiert.
	if 0 < y <= f(x):
		Mitte+=1 									# Flaeche ueber der x-Achse ist positiv. Wozu?
	if f(x) < y <= 0:
		Mitte-=1									# Flaeche unter der x-Achse ist negativ. Wozu?

Flaeche = Rechteck * float(Mitte) / Schritte2		#?
print('Mitte:',Mitte)
print(" Nummerische Integration = ", Flaeche)

