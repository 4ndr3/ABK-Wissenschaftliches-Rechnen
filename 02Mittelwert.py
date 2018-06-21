print("Aufgabe 2" )

print("1. Zahl")
x1 = float(input())

print("2. Zahl")
x2 = float(input())

print("3. Zahl")
x3 = float(input())

mittel = (x1 + x2 + x3) / 3

delta1 = mittel - x1
delta2 = mittel - x2
delta3 = mittel - x3

print("Mittelwert  ist:" , mittel)
print("X1:",x1,"Abweichung:",delta1)
print("X2:",x2,"Abweichung:",delta2)
print("X3:",x3,"Abweichung:",delta3)