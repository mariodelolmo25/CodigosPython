#_-_ coding: utf8 _-_
#__INICIO
  #Autor e imports
print ("Autor: Mario del Olmo [Versión: 0.1]\n")
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
  # .
  # .
global num1Procesado
global num2Procesado
global resultado
global respuesta
global aciertos
global fallos
global nota
global iniciolRango
global finalRango
global segundos
# Asignación de valores INICIALES
if inicio == 0:
  num1Raw = int(0)
  num2Raw = int(0)
  num1Procesado = int(0)
  num2Procesado = int(0)
  resultado = int(0)
  respuesta = int(0)
  aciertos = int(0)
  fallos = int(0)
  nota = int(0)
  inicioRango = int(0)
  finalRango = int(0)
  segundos = int(0)
  conteo = int(0)
      #COMPROBACION DE VALORES INICIALES+
'''
print (num1Raw)
print (num2Raw)
print (num1Procesado)
print (num2Procesado)
print (resultado)
print (respuesta)
print (correcto)
print (incorrecto)
print (aciertos)
print (fallos)
print (nota)
print (inicioRango)
print (finalRango)
print (segundos)
print ("FIN COMPROBACION VALORES INICIO")
input ("kj")
'''
#___FIN DECLARACIÓN DE VARIABLES
# COMIENZO PARTE LÓGICA
# ALEATORIEDAD
  # Define rango
print ("OBTENCIÓN DEL RANGO:\n")
inicioRango = int(input("Inicio del rango de valores: "))
finalRango = int(input("Final del rango de valores: "))
print (f"El rango de valores es: [({inicioRango}),({finalRango})]\n")
inicio = int(1)

# print ("¿Que quieres entrenar?")
    # Funcion elegir numeros aleatorios
def numerosAleatorios(): # Funcion que da valor aleatorio a los operandos.
  global num1Raw
  global num2Raw
  global segundos
  num1Raw = random.randint( inicioRango, finalRango )
  num2Raw = random.randint( inicioRango, finalRango )
numerosAleatorios()
    # SUMA
def sumaComprobacion():
  global conteo
  global resultado
  global respuesta
  global aciertos
  global fallos
  global nota
  conteo += 1
  resultado = num1Raw + num2Raw
  respuesta = int(input (f"\t\n{(num1Raw)} + {(num2Raw)} = "))
  if respuesta == resultado:
    print (Fore.GREEN + "Correcto" + Fore.RESET)
    aciertos += 1
  else: 
    print (Fore.RED + "Incorrecto" + Fore.RESET)
    fallos += 1
sumaComprobacion()

while aciertos < 10:
  numerosAleatorios()
  sumaComprobacion()
if aciertos == 10:
  nota = int(((aciertos - fallos) / conteo) * 10)
  nota = format(nota, ".2f")
  print ("") #intro
  print ("Fin de la partida")
  print ("Aciertos:", aciertos)
  print ("Fallos:", fallos)
  print ("Nota:", nota)
  print ("Tiempo:", segundos, "seg.")

''' No funciona y crashea el programa
while inicio == 1:
  segundos += 1
  time.sleep(1)
'''






# OBJETIVOS DE LA VERSION 1.0:
    # Que te pregunte si quieres hacer sumas, restas o multiplicaiones.
    # Que si sacas mas de un 5.0 se ponga en fondo verde, si no, rojo.
    # El contador de tiempo, que funcione.
    # Revisar las variables inicailes por si sobra alguna.
    # En caso de números negativos, que los ponga entre parentesis.
    # Redondee las operaciones de la forma más adecuada a la respuesta del usuario.
