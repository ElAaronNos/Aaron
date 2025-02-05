items = [] #Lista
Oprecio = 0 #Precio Original
num_items = 1 #Numeros de los items
a = 1
b = 2
c = 3
d = 4

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
while True: #Codigo
 print("----------------------------------------------------------------------------------------------------------------")
 print("[1]Agregar compra") #Debe dar una opcion en articulo y precio y en el output mostrar el articulo
 print("[2]Borrar producto")
 print("[3]Ver productos")
 print("[4]Total")
 print("[5]Salir")
 print("----------------------------------------------------------------------------------------------------------------")
 num = int(input()) #Opcion Elegida
 
 if num == 1: #¿Que desea comprar?
  print("¿que deseas llevar?")
  select = input()
  items.append(select) #Agrega
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
  print(f"¿Esta seguro que desea borrar su lista de compras, tienes:{items}? Y/N")
  ver = input()
  if ver == "Y": #Si
      items.remove(select)
      num_items = 0
      print("Se ah borrado la lista")
      time.sleep(2)
      clear()
  else: #No
      print("No se ah eliminado nada")
      time.sleep(2)
      clear()
      
 elif num == 3: #Cuantos Items tengo
     print(f"Usted Tiene: {items}")
     time.sleep(3)
     clear()
     
 elif num == 4: #total
     randomer = random.randint(1, 4)
     if randomer == 1:
         a *= Oprecio
     elif randomer == 2:
         b *= Oprecio
     elif randomer == 3:
         c *= Oprecio
     else:
         d *= Oprecio 
     print(f"El precio total de su carrito:{Oprecio}")
     time.sleep(3)
     clear()
     
 elif num == 5: #Exit
     print("Gracias Por Comprar :)")
     time.sleep(3)
     clear()
     break #END

