import math

Dateiname = '11Sonne-Erde-Mond.dat'
Datei = open(Dateiname,'w')

#Variablen initialisieren
t = 0.
t_max = 5.
dt = .0001

betam = 1								#Falls der Mond heute mal schwerer ist, kann man etwas anderes als 1 waehlen

Gm_Erde = 3. * 10**(-6)					# Gravitationskonstante G * m_Erde / ( 4 pi^2)
Gm_Mond = 3.69 * 10**(-8) * betam		# Gravitationskonstante G * m_Mond / ( 4 pi^2)


#Simulation initialisieren
Erde_s_x = 1.							#x-Startposition der Erde (s steht fuer Strecke, nicht fuer Start)
Erde_s_y = 0.							#y-Startposition der Erde

Erde_v_x = 0.							#Tangetialgeschwindigkeit der Erde in x zum Startzeitpunkt in [rad/a]
Erde_v_y = 2. * math.pi					#Tangetialgeschwindigkeit der Erde in y zum Startzeitpunkt in [rad/a]

Erde_s_x_alt = Erde_s_x - dt * Erde_v_x	#x-Pos. der Erde im vorherigen Zeitschritt
Erde_s_y_alt = Erde_s_y - dt * Erde_v_y	#y-Pos. der Erde im vorherigen Zeitschritt


Mond_s_x = Erde_s_x						#Mond ist auf der selben x-Startpos. wie die Erde
Mond_s_y = Erde_s_y - .002569			#Mond ist um minus seinen Radius in y verschoben

Mond_v_x = Erde_v_x + .23138			#Tangetialgeschwindigkeit des Mondes in x ist die der Erde plus Eigengeschwindigkeit 
Mond_v_y = Erde_v_y						#Tangetialgeschwindigkeit des Mondes in y ist die der Erde

Mond_s_x_alt = Mond_s_x - dt * Mond_v_x	#x-Pos. des Mondes im vorherigen Zeitschritt
Mond_s_y_alt = Mond_s_y - dt * Mond_v_y	#y-Pos. des Mondes im vorherigen Zeitschritt


#Abkuerzungen
pi24 = 4 * math.pi**2					#4*pi^2


while t < t_max:
	r_Erde_Mond = math.sqrt((Erde_s_x - Mond_s_x)**2 + (Erde_s_y - Mond_s_y)**2)
	r_Sonne_Erde = math.sqrt(Erde_s_x**2 + Erde_s_y**2)
	r_Sonne_Mond = math.sqrt(Mond_s_x**2 + Mond_s_y**2)
	
	#Beschleunigungen ACHTUNG: -pi24 AUSGEKLAMMERT WEIL die Gm-Konstanten DAS EINGERECHNET HABEN. != AUFBGABENSTELLUNG)
	Erde_a_x = - pi24 * (Erde_s_x / r_Sonne_Erde**3 + Gm_Mond * (Erde_s_x - Mond_s_x) / r_Erde_Mond**3)	#x-zweipunkt 
	Erde_a_y = - pi24 * (Erde_s_y / r_Sonne_Erde**3 + Gm_Mond * (Erde_s_y - Mond_s_y) / r_Erde_Mond**3)	#y-zweipunkt 
	Erde_s_x_neu = 2 * Erde_s_x - Erde_s_x_alt + dt**2 * Erde_a_x
	Erde_s_y_neu = 2 * Erde_s_y - Erde_s_y_alt + dt**2 * Erde_a_y
	
	Mond_a_x = - pi24 * (Mond_s_x / r_Sonne_Mond**3 + Gm_Erde * (Mond_s_x - Erde_s_x) / r_Erde_Mond**3)	#x-zweipunkt
	Mond_a_y = - pi24 * (Mond_s_y / r_Sonne_Mond**3 + Gm_Erde * (Mond_s_y - Erde_s_y) / r_Erde_Mond**3)	#y-zweipunkt
	Mond_s_x_neu = 2 * Mond_s_x - Mond_s_x_alt + dt**2 * Mond_a_x
	Mond_s_y_neu = 2 * Mond_s_y - Mond_s_y_alt + dt**2 * Mond_a_y

	Datei.write(str(t)+" "+str(Erde_s_x)+" "+str(Erde_s_y)+" "+str(Mond_s_x)+" "+str(Mond_s_y)+" "+str(Erde_s_x - Mond_s_x)+" "+str(Erde_s_y - Mond_s_y)+"\n")

	#aktuelle Position wird die alte
	Erde_s_x_alt = Erde_s_x
	Erde_s_y_alt = Erde_s_y	
	Mond_s_x_alt = Mond_s_x
	Mond_s_y_alt = Mond_s_y
	
	#neue Position wird die akutelle
	Erde_s_x = Erde_s_x_neu
	Erde_s_y = Erde_s_y_neu
	Mond_s_x = Mond_s_x_neu
	Mond_s_y = Mond_s_y_neu
	
	t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")
