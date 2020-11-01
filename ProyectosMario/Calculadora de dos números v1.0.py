#NOTAS DE VERSIÓN 1.1:
  #Línea 77: ahora divide entre numero2div. Antes entre numero2


# _-_ coding: utf8 _-_
#__INICIO
print("Bienvenido a la calculadora de dos valores. Versión: 1.1")
#Input números
numero1 = float(input("Introducir primer valor: "))
numero2 = float(input("Introducir el segundo valor: "))
print ("") #intro
diffNum = numero2 - numero1 #no se usa
#__COMPROBACIÓN DE NÚMEROS

#intentar hacer que en los negativos te los ponga entre paréntesis

def comprobaciónNúmeros():
  menorigualcero = numero1 + numero2
  if menorigualcero <= 0:
    print ("  AVISO:\n")
    print(f"\tLa suma de ambos números es: {menorigualcero}")
    print("\tTen en cuenta que estás trabajando con números negativos, el resultado puede alterarse.""\n")
  if numero2 > numero1:
    print(f"\tEl segundo número es mayor al primero, tenlo en cuenta para la división entera.""\n")
comprobaciónNúmeros()
if numero2 == 0:
  numero2div = 1
else:
  numero2div = numero2 
print ("") #intro
print (f"Valores introducidos (por orden): ({numero1}); ({numero2})")
comprobación = (f"Valores introducidos (por orden): {(numero1)}; {(numero2)}")
# Ajuste de Valores

#__FORMATO VALORES

# Intentar def format
# A lo bruto
suma = numero1 + numero2
resta = numero1 - numero2
if numero2 != 0:
  división = numero1 / numero2
else: 
  división = (numero1 / (numero2 + numero2div))
multiplicación = numero1 * numero2
formatSuma = format(suma, ".3f")
formatResta = format(resta, ".3f")
formatMultiplicación = format(multiplicación, ".3f")
formatDivisión = format(división, ".3f")
# Intento de def
'''
def formatValores():
  suma = numero1 + numero2
  resta = numero1 - numero2
  división = numero1 / numero2
  multiplicación = numero1 * numero2
  formatSuma = format(suma, ".3f")
  formatResta = format(resta, ".3f")
  formatMultiplicación = format(multiplicación, ".3f")
  formatDivision = format(división, ".3f")

formatValores()
'''
#__GIONES DE SEPARACIÓN
longComprobación = len(comprobación)
print ((5 + longComprobación) * "-")
#__MUESTRA OPERACIONES FORMATEADAS
print("OPERACIONES: \n")
print("\t" "Suma:", (numero1), "+", numero2, "=", formatSuma)
print("\t" "Resta:", numero1, "-", "(",numero2,")", "=", formatResta)
print("\t" "Multiplicación:", numero1, "x", numero2, "=", formatMultiplicación)
if numero2 == 0:
  print ("")
  print ("ADVERTENCIA: No se puede dividir entre 0\n")
else:
  print("\t" "División:", numero1, "/", numero2, "=", formatDivisión)
  print("\t""División entera:", numero1, "//", numero2, "=", numero1 // numero2)
