import math

Dateiname = '07Pendel-Runge-Kutta.dat'
Datei = open(Dateiname,'w')

def omegapunkt(phi,omega,t,g,l,q,F0,erz):
	return - g / l * math.sin(phi) - q * omega + F0 * math.sin(erz * t)    
	"""Bewegungsgleichung omegapunkt = phipunktpunkt
	1. Term: g/l = omega^2 = Eigenfrequenz^2; Erdbeschleunigung wirkt pos. beim nach unten schwingen und daempfend beim nach oben schwingen
	2. Term: q * omega ist die Daempfung des Pendels
	3. Term: Antreibende Kraft (erzwungene Schwingung) F0 wirkt beschleunigend"""

#Variablen initialisieren
t = 0.
t_max = 60.
dt = .01

phi = .7853975	#Startwinkel
omega = 0		#Startwinkelgeschwindigkeit

q = .5			#Qualitaetskonstante = Kehrwert der Daempfung = omega / gamma bei Santra
F0 = 1.2		#Kraft der erzwungenen Schwingung
erz = 2./3		#Kreisfrequenz der erzwungenen Schwingung

g = 9.81		#Erdbeschleunigung
l = g			#Laenge des Pendels; ist aus ueberhaupt gar keinem Grund gleich g

while t < t_max:
    phiquer = phi + (dt/2.) * omega                                     #?
    omegaquer = omega + (dt / 2.) * omegapunkt(phi,omega,t,g,l,q,F0,erz)  #?
    
    phi = phi + dt * omegaquer                                                  #?
    omega = omega + dt * omegapunkt(phiquer,omegaquer,t + dt / 2.,g,l,q,F0,erz)     #?
    
    Datei.write(str(t)+" "+str(phi)+" "+str(omega)+"\n")    #Schreibe Zeit, phi, omega in Datei
    t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")