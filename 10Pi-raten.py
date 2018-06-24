import math
import random
random.seed()

i = 0
Versuche = 2000000	#200K
Treffer = 0.

while i < Versuche:
	r = math.sqrt(random.random()**2 + random.random()**2)		#Radius ist ein zufaelliges Wurzel(x^2+y^2)
	if r < 1:
		Treffer += 1
	i += 1
	
calcpi = 4. * Treffer / i	
'''pi ist das Flaechenverhaeltnis zwischen den der Flaeche innheralb eines Kreises und der Gesamtflaeche x*y. Da man nur in einem Kreisquartal rechnet, rechnet man *4'''

print('Pi berechnet:',calcpi)
print('Pi genau:',round(math.pi,7))
print('Genauigkeit:', round((calcpi / math.pi)*100,3),'%')