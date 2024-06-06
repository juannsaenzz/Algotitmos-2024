
#! EJERCICIO 30

#! Desarrollar también una función recursiva que permita calcular el método de la secante de
#! una función f(x).

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    if max_iter == 0 or abs(x1 - x0) < tol:
        return x1
    else:
        y0 = f(x0)
        y1 = f(x1)
        if abs(y1 - y0) < tol:  # Evitar división por cero
            return None
        x_next = x1 - y1 * (x1 - x0) / (y1 - y0)
        return secante(f, x1, x_next, tol, max_iter - 1)

# Ejemplo de uso:
def funcion_ejemplo(x):
    return x**2 - 4  # Función ejemplo: x^2 - 4 = 0 tiene raíces en x = -2 y x = 2

raiz = secante(funcion_ejemplo, -2, 2)
if raiz is not None:
    print("Una raíz de la función es:", raiz)
else:
    print("No se pudo encontrar una raíz. La función es vertical en el intervalo dado.")

