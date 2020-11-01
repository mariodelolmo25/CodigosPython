#_-_ coding: utf8 _-_
print ("Autor: Mario del Olmo [Versión: 1.0]\n")
print("Bienvenido al generador de valores aleatorios.\n")

import random
import time
# Declaración de variables por usuario
segundero = int(1)
inicio = int(input("Introduce valor inicial de rango: "))
fin = int(input("Introduce valor final de rango: "))

if inicio > fin:
  print ("") #intro
  print ("\tERROR: El final del rango no puede ser mayor al inicio\n")
  inicio = int(input("\t\tIntroduce valor inicial de rango: "))
  fin = int(input("\t\tIntroduce valor final de rango: "))

duracion = int(input("Total de segundos que quieres que el programa funcione (total generados): "))

if duracion <= 0:
  print ("")
  print ("\t""ERROR: La duración no puede ser menor o igual que 0")
  duracion = int(input("Total de segundos que quieres que el programa funcione: "))

print ("") #intro
# Instrucciones y comienzo
print ("El programa mostrará un número aleatorio durante el tiempo que especifiques\n")
input("Pulsa cualquier tecla para comenzar")
print ("") #intro
# Aleatoriedad
def aleatoridad():
  numeroRango = random.randint( inicio, fin )
  print (numeroRango, "\t(",segundero,"/",duracion,"seg.)")
#Contador de tiempo
while True:
  aleatoridad()
  segundero += 1
  time.sleep(1)
  if segundero > duracion:
    print ("") #intro
    print ("\t""Fin de la instrucción")
    break #Finaliza el bucle, en consecuencia el programa.
