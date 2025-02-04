

n0 = float(input("ingresa el numero para la a"))
n1 = float(input("ingresa el numero para la b"))
n2 = float(input("ingresa el numero para la c"))

#Found the i
if n0 >= n1 and n0 >= n2:
    iid = n0
elif n1 >= n0 and n1 >= n2:
    iid = n1
else:
    iid = n2

#Found the m
if n0 <= n1 and n0 <= n2:
    m = n0
elif n1 <= n0 and n1 <= n2:
    m = n1
else:
    m = n2
#print the mensaje
print(f"el mayor es: {iid} y el menor es: {m}")