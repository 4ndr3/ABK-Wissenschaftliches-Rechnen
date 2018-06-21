import math

Dateiname = '07Pendel-Runge-Kutta.dat'
Datei = open(Dateiname,'w')

def omegapunkt(phi,omega,t,g,l,q,F0,erz):
	return -g/l * math.sin(phi) - q * omega + F0 * math.sin(erz * t)    #?

#Variablen initialisieren
t = 0.
tmax = 60.
dt = .01

phi = .7853975  #Startwinkel
omega = 0       #Startwinkelgeschwindigkeit

q = .5          #?
F0 = 1.2        #?
erz = 2./3      #?

g = 9.81        #Erdbeschleunigung
l = g           #?

while t < tmax:
    phiquer = phi + (dt/2.) * omega                                     #?
    omegaquer = omega + (dt / 2.) * omegapunkt(phi,omega,t,g,l,q,F0,erz)  #?
    
    phi = phi + dt * omegaquer                                                  #?
    omega = omega + dt * omegapunkt(phiquer,omegaquer,t + dt / 2.,g,l,q,F0,erz)     #?
    
    Datei.write(str(t)+" "+str(phi)+" "+str(omega)+"\n")    #Schreibe Zeit, phi, omega in Datei
    t = t + dt

Datei.close()
print(Dateiname,"erzeugt.")