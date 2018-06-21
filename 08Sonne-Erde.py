import math

Dateiname = '08Sonne-Erde.dat'
Datei = open(Dateiname,'w')				#Ausgabedatei zum schreiben oeffnen

#Variablen initialisieren
t = 0.
t_max = 100.
dt = .001

Erde_s_x = 1							#x-Startposition der Erde
Erde_s_y = 0							#y-Startposition der Erde
Erde_v_x = 0							#x-Startgeschwindigkeit der Erde
Erde_v_y = 2. * math.pi					#y-Startgeschwindigkeit der Erde
Erde_s_x_alt = Erde_s_x - dt * Erde_v_x	#x-Pos. der Erde im vorherigen Zeitschritt
Erde_s_y_alt = Erde_s_y - dt * Erde_v_y	#y-Pos. der Erde im vorherigen Zeitschritt

#Abkuerzungen
pi24 = 4. * math.pi**2					#4*pi^2

while t < t_max:
	r_Sonne_Erde = math.sqrt(Erde_s_x**2 + Erde_s_y**2)

	Erde_a_x = -pi24 * Erde_s_x / r_Sonne_Erde**3
	Erde_a_y = -pi24 * Erde_s_y / r_Sonne_Erde**3
	Erde_s_x_neu = 2. * Erde_s_x - Erde_s_x_alt + dt**2 * Erde_a_x
	Erde_s_y_neu = 2. * Erde_s_y - Erde_s_y_alt + dt**2 * Erde_a_y


	Datei.write(str(t)+" "+str(Erde_s_x)+" "+str(Erde_s_y)+"\n")
	
	#aktuelle Position wird die alte
	Erde_s_x_alt = Erde_s_x	
	Erde_s_y_alt = Erde_s_y
	
	#neue Position wird die akutelle
	Erde_s_x = Erde_s_x_neu
	Erde_s_y = Erde_s_y_neu
	
	t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")