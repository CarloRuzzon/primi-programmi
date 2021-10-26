#Programma che dato il raggio calcola superficie e volume di una sfera
import math 
raggio = input("Inserire il raggio della sfera: ");
raggio = int(raggio);
superficie = 4.0 * math.pi * raggio * raggio;
volume = 4.0 * math.pi * raggio * raggio * raggio / 3.0;
print("Dato il valore del raggio", raggio, ", la superficie vale:", superficie, "e il volume vale: ", volume);
