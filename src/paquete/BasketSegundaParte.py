# coding:utf-8

'''
Created on 9 feb. 2021

@author: Moisés Adamuz y José Villalón Rivero


'''

from collections import Counter
import statistics

#Metodo para mostrar los distintos métodos estadísticos pedidos de cada lista de datos
def estadisticas(nombre):
    for i in range(0, len(nombre)): 
                nombre[i] = int(nombre[i]) 
    print("Media: " + str(statistics.mean(nombre)))
    #Evitamos usar ".mode(data)" por si hay duplicidad de números, lo que provoca errores
    print("Moda: " + str(Counter(nombre).most_common()[0][0]))
    print("Mediana: " + str(statistics.median(nombre)))
    print("Máximo: " + str(max(nombre)))
    print("Mínimo: " + str(min(nombre)))
    print(" ")

def listar():
    Puntos = []
    Perdidas = []
    Recuperciones = []
    Asistencias = []
    Fallados = []
    try:
        print("¿Nombre del fichero?")
        nombre = input()
        print(f"Leyendo el fichero {nombre}.txt\n")
        f = open(f"{nombre}.txt","r") # Abrir fichero para leer
    except Exception:
        exit()
    fin = False # Variable para controlar fin del bucle
    linea = f.readline() # Lectura de una línea
    print(linea)
    while not fin: # Bucle para recorrer fichero
        linea = f.readline() # Lectura de una línea
        res = linea.split("     -       ",4)
        if res[0]!='':
            Puntos.append(res[0])
            Perdidas.append(res[1])
            Recuperciones.append(res[2])
            Asistencias.append(res[3])
            Fallados.append(res[4])
        if not linea: # Comprobar si hemos llegado a fin de fichero
            fin = True
            print("Puntos")
            estadisticas(Puntos)
            
            print("Balones Perdidos")
            estadisticas(Perdidas)
            
            print("Balones Recuperados")
            estadisticas(Recuperciones)
           
            print("Asistencias")
            estadisticas(Asistencias)
            
            print("Tiros Fallados")
            estadisticas(Fallados)
        else:
            print(linea)
    f.close() # Cerrar 