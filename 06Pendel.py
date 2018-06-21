import math

Dateiname = '06Pendel.dat'
Datei = open(Dateiname,'w')        #Datei zum schreiben oeffnen

#Variablen initialisieren
t = 0.
t_max = 20.
dt = .01

while t < t_max:
	Datei.write(str(t)+" "+str(math.cos(t))+" "+str(math.sin(t))+"\n")  #Schreibe Zeit, phi=cos(t), omega=sin(t) in Datei
	t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")