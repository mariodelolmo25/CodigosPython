x = int(input("Introducir primer valor: "))
y = int(input("Introducir segundo valor: "))
print ("\n")
print ("1: Suma")
print ("2: Resta")
print ("3: Multi\n")

n = int(input("¿Que operacion quieres hacer? "))

def suma():
  print (f"{x} + {y} = {x + y}")

def resta():
  print (f"{x} - {y} = {x - y}")

def multi():
  print (f"{x} x {y} = {x * y}")


if n == 1:
  suma()

if n == 2:
  resta()

if n == 3:
  multi()

print ("FIN DEL PROGRAMA")
