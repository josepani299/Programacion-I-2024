
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

# Buscando los divisores del coeficiente principal y el termino independiente.
#
# Posibles raices enteras positivas

divisiores_ti = []
for i in range(int(polinomio3[-1])):
    if int(polinomio3[-1]) % (i+1) == 0:
        divisiores_ti.append(i+1)

divisiores_cp = []

for i in range(int(polinomio3[0])):
    if int(polinomio3[0] % (i+1) == 0):
        divisiores_cp.append(i+1)

print(divisiores_cp)
print(divisiores_ti)

# Posibles raices enteras negativas

divisores_cpn = []

for i in range(int(len(divisiores_cp))):
    divisores_cpn.append(divisiores_cp[i]*(-1))

divisores_tin = []

for i in range(int(len(divisiores_ti))):
    divisores_tin.append(divisiores_ti[i]*(-1))

print(divisores_cpn)
print(divisores_tin)

# Unificando los divisores en un solo vector.

divisiores_Enteros = divisiores_ti + divisiores_cp + divisores_tin + divisores_cpn

print(divisiores_Enteros)

# Quitando los elementos repetidos

divisiores_Enteros_Unicos = list(set(divisiores_Enteros))

print(divisiores_Enteros_Unicos)

# Posibles raices racionales de estilo Ti/cp

# Intendo generar el acumulador para establecer si es  una raiz o no

acumulador = 0
for i in range(4):
    print(f"{polinomio3[i]}*({polinomio3[1]})^{grados-1}")
    acumulador = acumulador + polinomio3[i]*(polinomio3[-1])**(grados-1)
    grados -= 1
    print(acumulador)
