items = [] #Lista
precio = [] #Precio
num_items = 1 #Numeros de los items

def clear():
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)
 print("")
 time.sleep (0.1)#Animation #Animacion
import time #Importa el tiempo
import random #Importa el randomizador

print("Hola bienvenido a la tienda :) escriba una opcion con los numeros o las letras que le indique")

#Codigo
while True:
 print("----------------------------------------------------------------------------------------------------------------")
 print("[1]Agregar compra")
 print("[2]Borrar un producto")
 print("[3]Ver productos")
 print("[4]Total de la compra")
 print("[5]Salir")
 print("----------------------------------------------------------------------------------------------------------------")
 num = int(input()) #Opcion Elegida
 
 if num == 1: #¿Que desea comprar?
  print("¿que deseas llevar?")
  select = input()
  print("¿Cual es el precio de la compra?")
  precio_a = float(input())
  items.append(select) #Agrega
  precio.append(precio_a)
  if num_items == 1:
   print(f"tiene en el carrito: 1 producto")
   time.sleep(1.5)
  elif num_items > 1:
   print(f"tiene en el carrito: {num_items} productos")
   time.sleep(3)
  num_items += 1
  Oprecio = random.randint(1, 15)
  clear()

 elif num == 2:
  if num_items > 1:
   print(f"¿Que desea borrar?")
   select = input()
   print(f"¿Esta seguro que desea borrar {select} de su lista? Y/N")
   ver = input()
   if ver == "Y": #Si
       items.remove(select)
       num_items -= 1
       print(f"Se ah borrado {select}")
       time.sleep(2)
       clear()
   else: #No
       print("No se ah eliminado nada")
       time.sleep(2)
       clear()
  else:
    print("No tiene nada en el carrito")
    time.sleep(2)
    clear()

 elif num == 3: #Cuantos Items tengo
     if num_items > 1:
      print(f"Usted Tiene: {items}")
      time.sleep(3)
      clear()
     else:
      print("No tiene nada en el carrito") 
 elif num == 4: #total
     if num_items > 1:
      Fprecio = sum(precio)
      print(f"El precio total de su carrito:{Fprecio}$")
      time.sleep(3)
      clear()
     else: 
      print("No tiene nada en el carrito") 
     
 elif num == 5: #Exit
     print("Gracias Por Comprar :)")
     time.sleep(3)
     clear()
     break #END

