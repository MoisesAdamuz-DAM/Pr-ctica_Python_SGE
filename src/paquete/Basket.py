# coding:utf-8

'''
Created on 9 feb. 2021

@author: Moisés Adamuz y José Villalón Rivero


'''
import random

"Rellenar Listas"

p = []  # Puntos
bP = []  # Balones Perdidos
bR = []  # Balones Recuperados
a = []  # Asistencias
tF = []  # Tiros Fallados

"Originamos los rangos de forma aleatoria con random"
for i in range(999):
    p.append(random.randrange(100))
    bP.append(random.randrange(100))
    bR.append(random.randrange(100))
    a.append(random.randrange(100))
    tF.append(random.randrange(100))
    
file = open("file.txt", "w")

file.write("Puntos - Balones Perdidos - Balones Recuperados - Asistencias - Tiros Fallados \n")

for i in range(999):
    cadena = f"{str(p[i])}     -       {str(bP[i])}     -       {str(bR[i])}     -       {str(a[i])}     -       {str(tF[i])}"
    file.write(cadena + "\n")

file.close();

def mostrar():
    with open("file.txt") as file:
        for line in file:
            print(line)

