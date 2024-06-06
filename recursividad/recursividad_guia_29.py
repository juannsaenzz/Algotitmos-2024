
#! EJERCICIO 29

#! Desarrollar una función recursiva que permita calcular el método de la bisección de una función f(x).

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if max_iter == 0 or abs(b - a) < tol:
        return (a + b) / 2
    else:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            return biseccion(f, a, c, tol, max_iter - 1)
        else:
            return biseccion(f, c, b, tol, max_iter - 1)

# Ejemplo de uso:
def funcion_ejemplo(x):
    return x**2 - 4  # Función ejemplo: x^2 - 4 = 0 tiene raíces en x = -2 y x = 2

raiz = biseccion(funcion_ejemplo, -2, 2)
print("Una raíz de la función es:", raiz)
