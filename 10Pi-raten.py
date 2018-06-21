import math
import random
random.seed()

i =  0
Versuche = 2000000	#200K
Treffer = 0.

while i < Versuche:
	r = random.random()**2 + random.random()**2		#Radius ist ein zufaelliges x^2+y^2
	if r < 1:
		Treffer += 1
	i += 1
	
calcpi = 4. * Treffer / i

print('Treffer:',Treffer)
print('i:',i)
print('Treffer/i:',Treffer/i)
print('Pi berechnet:',calcpi)
print('Pi genau:',round(math.pi,7))
print('Fehler:', round(abs((calcpi - math.pi) / calcpi)*100,3),'%')