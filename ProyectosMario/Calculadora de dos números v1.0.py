# _-_ coding: utf8 _-_
#__INICIO
print ("Autor: Mario del Olmo [Versión: 1.2]\n")
print("Bienvenido a la calculadora de dos valores.")
#Input números
numero1Raw = float(input("Introducir primer valor: "))
numero2Raw = float(input("Introducir el segundo valor: "))
print ("") #intro
diffNum = numero2Raw - numero1Raw #no se usa
#__COMPROBACIÓN DE NÚMEROS
if numero1Raw < 0:
  numero1Neg = str(f"({numero1Raw})")
  print (numero1Neg)
else:
  numero1Neg = numero1Raw
if numero2Raw < 0:
  numero2Neg = str(f"({numero2Raw})")
  print (numero2Neg)
else:
  numero2Neg = numero2Raw
#intentar hacer que en los negativos te los ponga entre paréntesis
def comprobaciónNúmeros():
  menorigualcero = numero1Raw + numero2Raw
  if menorigualcero <= 0:
    print ("  AVISO:\n")
    print(f"\tLa suma de ambos números es: {menorigualcero}")
    print("\tTen en cuenta que estás trabajando con números negativos, el resultado puede alterarse.""\n")
  if numero1Raw > numero2Raw:
    print(f"\tEl primer número es mayor al primero, tenlo en cuenta para la división entera.""\n")
comprobaciónNúmeros()
if numero2Raw == 0:
  numero2div = 1
else:
  numero2div = numero2Raw 
print ("") #intro
print (f"Valores introducidos (por orden): ({numero1Raw}); ({numero2Raw})")
comprobación = (f"Valores introducidos (por orden): {(numero1Raw)}; {(numero2Raw)}")
# Ajuste de Valores
#__FORMATO VALORES
# Intentar def format
# A lo bruto
suma = numero1Raw + numero2Raw
resta = numero1Raw - numero2Raw
if numero2Raw != 0:
  división = numero1Raw / numero2Raw
else: 
  división = (numero1Raw / (numero2Raw + numero2div))
multiplicación = numero1Raw * numero2Raw
formatSuma = format(suma, ".2f")
formatResta = format(resta, ".2f")
formatMultiplicación = format(multiplicación, ".2f")
formatDivisión = format(división, ".3f")
#__GIONES DE SEPARACIÓN
longComprobación = len(comprobación)
print ((5 + longComprobación) * "-")
#__MUESTRA OPERACIONES FORMATEADAS
print ("OPERACIONES: \n")
print ("\t" "SUMA:", (numero1Neg), "+", numero2Neg, "=", formatSuma)
print ("\t" "RESTA:", numero1Neg, "-", numero2Neg, "=", formatResta)
print ("\t" "MULTIPLICACIÓN:", numero1Neg, "x", numero2Neg, "=", formatMultiplicación)
if numero2Raw == 0:
  print ("")
  print ("ADVERTENCIA: No se puede dividir entre 0\n")
else:
  print ("\t" "DIVISIÓN:", numero1Neg, "/", numero2Neg, "=", formatDivisión)
  print ("\t""DIVISIÓN ENTERA:", numero1Neg, "//", numero2Neg, "=", numero1Raw // numero2div)

  #CAMBIOS VERSIÓN 1.2:
    # Ahora los números negativos se mostrarán entre paréntesis.
    # Se han corregido algunos errores gramaticales.
    # El nombre de cada operación se representa en mayúsculas.
    # Se ha eliminado una parte del código inservible (antes desactivada en comentario)
    # Ahora la suma, resta y multiplicaión muestran dos cifras decimales en vez de tres.
 
 # FIN DEL PROGRAMA
