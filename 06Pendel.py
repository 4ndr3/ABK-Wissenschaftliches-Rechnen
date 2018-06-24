import math

Dateiname = '06Pendel.dat'
Datei = open(Dateiname,'w')        #Datei zum schreiben oeffnen

#Variablen initialisieren
t = 0.
t_max = 20.
dt = .01

while t < t_max:
	Datei.write(str(t)+" "+str(math.cos(t))+" "+str(math.sin(t))+"\n")  #Schreibe Zeit, phi=cos(t), omega=sin(t) in Datei; Wenn Pendel losgelassen wird verhaelt sich der Winkel wie Cosinus zum Startzeitpunkt = 1 = voll ausgelenkt, waehrend die Winkelgeschwindigkeit sich wie der sinus verhaelt zum Startzeitpunkt t=0 ist sie gleich 0
	t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")