import numpy as np					#numpy bib mit mathefunktionen
from scipy.integrate import odeint	#scipy bib mit Ordinary Differential Equation solver Funktion
import matplotlib.pyplot as plt		#plot bib

def pendel(y,t,b,c):
	phi, omega = y				#array y in zwei variablen spalten
	return [omega, -b * omega - c * np.sin(phi)]	# Differentialgleichung, die geloest wird als Array mit [omega, omegapunkt]

#phipunktpunkt(t) + b * phipunkt(t) + c * sin(phi) = 0
#omegapunkt(t) + b * omega(t) + c * sin(phi) = 0

#Definiere Variablen
b = .25 							#Daempfung
c = 5								#Pendellänge?
y0 = [np.pi-.1,0]					#Array mit Startwerten [phi, phipunkt=omega]
t = np.linspace(0,10,101)			#Zeit array mint 101 gleigrossen Werten zwischen 0 und 10

solution = odeint(pendel,y0,t,args=(b,c))	#Loesung der Differentialgleichung des Pendels mit den Startwerten

plt.plot(t,solution[:,0],'b',label='phi(t)')
plt.plot(t,solution[:,1],'g',label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()