import time #Importa el tiempo
loop = True #Variable del While
ani = -1
while loop == True: #Empieza el loop
    
 var1 = int(input("[primer numero]"))
 var3 = input("[signo]")
 var2 = int(input("[Segundo numero]"))
 
 if var3 == "+":
  print(f"resultado de la suma:{var1 + var2}")
  ani += 8
  time.sleep (3)
  while ani > 0:
    print("")
    ani -= 1
    time.sleep(0.1)
    
 elif var3 == "-":
  print(f"resultado de la resta:{var1 - var2}")
  ani += 8
  time.sleep (3)
  while ani > 0:
    print("")
    ani -= 1
    time.sleep(0.1)
    
 elif var3 == "*":
  print(f"resultado de la multiplicacion:{var1 * var2}")
  ani += 8
  time.sleep (3)
  while ani > 0:
    print("")
    ani -= 1
    time.sleep(0.1)
    
 elif var3 == "/":
  print(f"resultado de la division:{var1 // var2}")
  ani += 8
  time.sleep (3)
  while ani > 0:
    print("")
    ani -= 1
    time.sleep(0.1)
    
 else:
  print("Error, Porfavor ponga en el signo")
  ani += 8
  time.sleep (3)
  while ani > 0:
    print("")
    ani -= 1
    time.sleep(0.1)