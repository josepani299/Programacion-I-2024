
# Raices de un polinomio de grado 1#

def grado1():
    pendiente = float(input("Ingrese la pendiente de la recta: "))
    ordenada = float(input("Ingrese la ordenada de la recta:  "))
    raiz = (-pendiente/ordenada)
    print(f"la rairz de la recta {pendiente}X{ordenada} es: {raiz}")


# Raices del polinomio de grado 2;


def grado2():
    import math
    a = float(input("Ingrese el coeficiente principal"))
    b = float(input("Ingrese el valor b de la ecuacion"))
    c = float(input("Ingrese la ordenada al origen"))
    dis = float(math.sqrt(b**2 - 4*a*c))
    if dis < 0:
        print("No tiene raices reales")
    else:
        x1 = float((-b+dis)/2*a)
        x2 = float((-b - dis) / 2 * a)
        print(f"Las raices de la ecuacion son: {x1} y {x2} ")


# Intentando la de grado 3:

# Ingresando valores de los coeficientes de polinomio de grado 3 guardandolo en un vector

polinomio3 = [0]*4
grados = len(polinomio3)
exponente = len(polinomio3)
for i in range(4):
    polinomio3[i] = float(input(f"Ingrese el valor delante de X^{exponente-1}: "))
    exponente -= 1


# Buscando los divisiores de un numero

divisiores = [0] * int(polinomio3[-1])
numerodiv = len(divisiores)

for i in range(numerodiv):
    if int(polinomio3[-1]) % (i+1) == 0:
        divisiores[i] = i

for i in range(numerodiv):
    print(divisiores[i])


# Intendo generar el acumulador para establecer si es  una raiz o no
acumulador = 0
for i in range(4):
    print(f"{polinomio3[i]}*({polinomio3[1]})^{grados-1}")
    acumulador = acumulador + polinomio3[i]*(polinomio3[-1])**(grados-1)
    grados -= 1
    print(acumulador)

# probando con grado 3
# i = int(0)
# grado = int(input("Ingrese el grado del polinomio: "))
# expo = grado
# pol = [0]*(grado+1)
# for i in range(grado+1):
#   pol[i] = float(input(f"ingrese el valor del exponente nº {expo} "))
#  expo = expo-1
# Hacer un segun para el panel principal
