#_-_ coding: utf8 _-_
#__INICIO
#Autor e imports
print ("Autor: Mario del Olmo [Versión: 0.2]\n")
print ("Bienvenido al programa de cálculo.\n")

import random
import time
from colorama import init, Fore, Back, Style

# Instrucciones visuales
inicio = 0
print ("El programa preguntará un rango de valores el cuál servirá para ubicar los valores.")
print ("El tipo de aporaciones serán: SUMAS, RESTAS y MULTIPLICACIONES")
print ("Cada vez que inicies el programa te preguntará que cálculos quieres hacer.")
print ("Se realizarán diez operaciones, al final del programa se mostrará el recuento de aciertos y fallos con una nota correspondiente\n")
print ("Pulsa INTRO para comenzar")
input()
print ((30 * "-"),"\n")
# DECLARACIÓN DE VARIABLES
# Globalización de variables (implementar en cada funcion)
global resultado
global respuesta
global aciertos
global fallos
global nota
global inicioRango
global finalRango

# Asignación de valores INICIALES
if inicio == 0:
  num1Raw = int(0)
  num2Raw = int(0)
  resultado = int(0)
  respuesta = int(0)
  aciertos = int(0)
  fallos = int(0)
  nota = int(0)
  inicioRango = int(0)
  finalRango = int(0)
  conteo = int(0)
  segundos = int(0)
#___FIN DECLARACIÓN DE VARIABLES

# COMIENZO PARTE LÓGICA

# ALEATORIEDAD

# Define rango
print ("OBTENCIÓN DEL RANGO:\n")
print ("Si se deja en valores nulos provocará un error")
inicioRango = int(input("Inicio del rango de valores: "))
finalRango = (int(input("Final del rango de valores: ")))

print (f"El rango de valores es: [({inicioRango}),({finalRango})]\n")
print ((30 * "-"),"\n")

def numerosAleatorios(): # Funcion que da valor aleatorio a los operandos.
  global num1Raw
  global num2Raw
  global segundos
  num1Raw = random.randint(inicioRango,finalRango )
  num2Raw = random.randint(inicioRango,finalRango )

while conteo <= 10:
  numerosAleatorios()
  def suma(): #SUMA
    global conteo
    global resultado
    global respuesta
    global aciertos
    global fallos
    print ("SUMA")
    conteo += 1
    resultado = num1Raw + num2Raw
    respuesta = int(input (f"\t\n{(num1Raw)} + {(num2Raw)} = "))
    if resultado == respuesta:
      print (Fore.GREEN + "Correcto" + Fore.RESET)
      aciertos += 1
    else: 
      print (Fore.RED + "Incorrecto" + Fore.RESET)
      fallos += 1
  suma()
  numerosAleatorios()
  def resta(): #RESTA
    global conteo
    global resultado
    global respuesta
    global aciertos
    global fallos
    print ("RESTA")
    conteo += 1
    resultado = num1Raw - num2Raw
    respuesta = int(input (f"\t\n{(num1Raw)} - {(num2Raw)} = "))
    if respuesta == resultado:
      print (Fore.GREEN + "Correcto" + Fore.RESET)
      aciertos += 1
    else: 
      print (Fore.RED + "Incorrecto" + Fore.RESET)
      fallos += 1
  resta()
  numerosAleatorios()
  def multi(): #MULTIPLICACIÓN
    global conteo
    global resultado
    global respuesta
    global aciertos
    global fallos
    print ("MULTIPLICACIÓN")
    conteo += 1
    resultado = num1Raw * num2Raw
    respuesta = int(input (f"\t\n{(num1Raw)} x {(num2Raw)} = "))
    if respuesta == resultado:
      print (Fore.GREEN + "Correcto" + Fore.RESET)
      aciertos += 1
    else: 
      print (Fore.RED + "Incorrecto" + Fore.RESET)
      fallos += 1
  multi()

nota = int((aciertos/conteo)*10)
nota = format(nota, ".2f")
print ("") #intro
print ("Fin de la partida:")
print ("\nAciertos:", aciertos)
print ("Fallos:", fallos)
print ("Nota:", nota)
print ("")
exit()
