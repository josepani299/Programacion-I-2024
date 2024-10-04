
#Raices de un polinomio de grado 1

def grado1():
    pendiente=float(input("Ingrese la pendiente de la recta: "));
    ordenada=float(input("Ingrese la ordenada de la recta:  "));
    raiz=(-pendiente/ordenada);
    print(f"la rairz de la recta {pendiente}X{ordenada} es: {raiz}");

#Raices del polinomio de grado 2;
def grado2():
    import math
    a=float(input("Ingrese el coeficiente principal"));
    b=float(input("Ingrese el valor b de la ecuacion"));
    c=float(input("Ingrese la ordenada al origen"));
    Dis= float(math.sqrt( b**2 - 4*a*c));
    if Dis<0 :
        print("No tiene raices reales");
    else:
        x1 = float((-b+Dis)/2*a);
        x2 = float((-b - Dis) / 2 * a);
        print(f"Las raices de la ecuacion son: {x1} y {x2} ");


#Hacer un segun para el panel principal



<<<<<<< HEAD
=======
Grado_Polinomio=input("Ingrese el grado del polinomio  ")

print("El grado del polinomio es:", Grado_Polinomio)

print("El grado de un polinomio es el exponente mas grande que se encuentra en el polinomio")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print("2024")
print("Matematica")
print("No se que estoy haciendo")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
>>>>>>> 258f95e2e39e29f77b05a72ec352585665f21e78
