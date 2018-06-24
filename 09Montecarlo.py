#Integration der Funktion f per Monte Carlo Methode
import math
import random
random.seed()

def f(x):
	return math.sin(x)	#beliebige funktion als f definieren


#Variablen initialisieren
x_min = 0				# intervall [0,2pi] definieren 
x_max = 2. * math.pi
Schritte = 1000000		#1M Schritte
y_min = f(x_min)		
y_max = y_min			#weil die Sinus-Funktion 2pi-periodisch ist, ist y_min = f(x_min) = y_max = f(x_max), funktioniert nur wen def f() eine 2pi-periodische Funktion definiert

for i in range(Schritte):
	x = x_min + (x_max - x_min) * float(i) / Schritte	#aktueller x-Wert des Schrittes i ist das x-Intervall geteilt durch die Anzahl der Schritte mal dem akutellen schritt
	y = f(x)											
	if y < y_min:										# Das tatsaechliche Funktions-y_min wird gefunden
		y_min = y
	if y > y_max:										# Das tatsaechliche Funktions-y_max wird gefunden
		y_max = y


#Monte Carlo
Rechteck = (x_max - x_min) * (y_max - y_min)		# Rechteckflaeche um die Funktion
Schritte2 = 1000000									# 1M Punkte
Treffer = 0

for j in range(Schritte2):
	x = x_min + (x_max - x_min) * random.random()	# zu x wird ein zufaelliger aus dem Intervall von x addiert.
	y = y_min + (y_max - y_min) * random.random()	# zu y wird ein zufaelliger aus dem Intervall von y addiert.
	if math.fabs(y) <= math.fabs(f(x)):				# Wenn der Absolutwert von y kleiner dem absoluten Funktionswert an der Stelle x ist...
		if 0 < y <= f(x):
			Treffer += 1 									# Flaeche ueber der x-Achse wird als positive Flaeche gewertet
		if f(x) <= y < 0:
			Treffer += 1									# Flaeche unter der x-Achse AUCH ALS POSITIVE Flaeche gewertet

Flaeche = Rechteck * float(Treffer) / Schritte2		# ist scheinbar so
print('Treffer:',Treffer)
print(" Nummerische Integration = ", Flaeche)		#Sollte int(sin(x),0,pi) ~= 4 rauskommen, wenn man die Flaeche unter der x-Achse positiv wertet. Sonst sollte ~= 0 raus kommen

