import time
x = float(input("Introduce valor inicial: "))
dias = 0
diass = int(input("Introducir días: "))
def funcion():
  global x
  global dias
  print ("Día:",dias,"->", x, "€")
  x = x * 2
  dias = dias + 1
  time.sleep(0.01)


while dias <= diass:
  funcion()
else:
  exit()
