import numpy as np						#numpy bib mit mathefunktionen und umbenennen in np
from scipy.integrate import odeint		#von scientific python bib nur Ordinary Differential Equation solver Funktion
import matplotlib.pyplot as plt			#von matplotlib nur die pyplot sublib und in plt umbennen
from matplotlib.patches import Circle	#von matplotlib.patches nur Kreisfunktion

L1, L2 = 1, 1				# Pendelarm-Laengen [m]
m1, m2 = 1, 1				# Massen [Kg]
g = 9.81					#Gravitationskonstante
r = .05						#Radius der Kugeln

def Ableitung(y,t,L1,L2,m1,m2):
	theta1, theta1punkt, theta2, theta2punkt = y

	cos = np.cos(theta1-theta2)
	sin = np.sin(theta1-theta2)
	theta1punktpunkt = (m2 * g * np.sin(theta2) - m2 * sin * (L1 * theta1punkt**2 * cos + L2 * theta2punkt**2) - (m1 + m2) * g * np.sin(theta1)) / L1 / (m1 + m2 * sin**2)

	theta2punktpunkt = ((m1 + m2) * (L1 * theta1punkt**2 * sin - g * np.sin(theta2) + g * np.sin(theta1) * cos) + m2 * L2 * theta2punkt**2 * sin * cos) / L2 / (m1 + m2 * sin**2)

	return theta1punkt, theta1punktpunkt, theta2punkt, theta2punktpunkt


def make_plot(i):											#Plotten und Abspeichern des Doppelpendels fuer Zeitpunkt i
	ax.plot([0,x1[i],x2[i]], [0, y1[i],y2[i]], lw=2,c='k')	#Die Arme
	c0 = Circle((0,0),r/2,fc='k',zorder=10)					#Kreise als Massen und Ankerpunkt
	c1 = Circle((x1[i],y1[i]),r,fc='b',ec='b',zorder=10)	
	c2 = Circle((x2[i],y2[i]),r,fc='r',ec='r',zorder=10)	
	ax.add_patch(c0)
	ax.add_patch(c1)
	ax.add_patch(c2)
	
	#Schwanz als nachlassende Linie
	ns = 20
	s = max_trail//ns
	for j in range(ns):
		imin = i - (ns - j) * s
		if imin < 0:
			continue
		imax = imin + s + 1
		alpha = (j / ns)**2				#quadratisches Abschwaechen
		ax.plot(x2[imin:imax],y2[imin:imax],c='r',solid_capstyle='butt',lw=2,alpha=alpha)
	
	#Bild auf Ankerpunkt fixieren und Achsen gleichsetzen
	ax.set_xlim(-L1-L2-r,L1+L2+r)
	ax.set_ylim(-L1-L2-r,L1+L2+r)
	ax.set_aspect('equal',adjustable='box')
	plt.axis('off')
	plt.savefig('frames/_img{:04d}.png'.format(i//di))
	plt.cla()

	
t_max = 20
dt = .01
t = np.arange(0, t_max+dt, dt)		#Zeitraum und Abstand der Zeitpunkte ergeben die Zeitmatrix [s]
y0 = [np.pi/2, 0, np.pi / 2, 0]		#Anfangsauslenkung und Winkelgeschwindigkeit [theta1, omega1, theta2, omega2]


y = odeint(Ableitung,y0,t,args=(L1,L2,m1,m2))	#Numerische Integration, Speicherung in y
theta1 = y[:,0]						#Winkelfunktionen aus dem Ergebnis der numerischen Integration gewinnen; Zahl hinter dem Komma ist die Spalte
theta2 = y[:,2]

#Umwandlung in kartesische Koordinaten
x1 =  L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)


#Ab hier nur noch Plotten
trail_secs = 1						#Schwanz von m2 fuer Sekunden
max_trail = int(trail_secs / dt)	#Ueberfuehrung in Vektor


fps = 10
di = int(1. / fps / dt)			# FEHLER in Python 2.x: for i in range(0, t.size, di): ValueError: range() step argument must not be zero. MIT 1. GEHT ES. oder mit Python 3.x geht es
fig , ax = plt.subplots()

for i in range(0, t.size, di):
	print(i//di,'/',t.size//di)
	make_plot(i)
