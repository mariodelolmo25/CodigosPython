import time
num = int(input("Escribe algo y te diré si es un entero: ")) #Pregunta
y = num / 2
if y == int(y): #Comprueba que sea par o impar
  print("\n \t - Número PAR\n")
else:
	print("\n \t - Número IMPAR\n")

stop = num
ant = num

print ("Los números de su tipo anteriores son: \n")
while num != 0: #Imprime la serie anterior par o impar
  ant = ant - 2
  if ant >= 0:
    print (ant)
    time.sleep (0.05)
    if ant <= 0:
      print ("\n FIN DEL PROGRAMA")
      exit()
    if ant - 1 == 0:
      exit()
