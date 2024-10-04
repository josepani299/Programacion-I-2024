
# This is a sample Python script.

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
