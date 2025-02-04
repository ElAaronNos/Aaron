import time
sec = -1
name = input("Por favor, ingrese tu nombre: ")
age = int(input("porfavor ingresa tu edad"))
height = float(input("porfavor ingresa tu altura"))
sec += 8  #le da un valor a sec para que empieze el loop
#-----------------------------------------------------------------------------------------------------------------------#
while sec > 0: #Crea una animacion que termina cuando sec llega a 0
    print("")
    sec -= 1
    time.sleep(0.1)
#-----------------------------------------------------------------------------------------------------------------------#
print(f"Hola mi nombre es: {name}, tengo: {age} años, y mido {height}.cm")
while sec < 4:
    print("")
    sec += 1
    time.sleep(0.1)
time.sleep(120)


