
#! EJERCICIO 31

#! Por último, desarrollar otra función recursiva que permita calcular el método de Newton-Ra-
#! phson de una función f(x).

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    if max_iter == 0 or abs(f(x0)) < tol:
        return x0
    else:
        x_next = x0 - f(x0) / df(x0)
        return newton_raphson(f, df, x_next, tol, max_iter - 1)

# Ejemplo de uso:
def funcion_ejemplo(x):
    return x**2 - 4  # Función ejemplo: x^2 - 4 = 0 tiene raíces en x = -2 y x = 2

def derivada_ejemplo(x):
    return 2 * x

raiz = newton_raphson(funcion_ejemplo, derivada_ejemplo, 2)
print("Una raíz de la función es:", raiz)
