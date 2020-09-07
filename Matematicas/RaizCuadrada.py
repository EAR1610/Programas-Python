import math

def fx(x: float, a: float) -> float:
    return math.pow(x, 2) - a

def fx_derivada(x: float) -> float:
    return 2 * x

def obtener_punto_de_init(a: float) -> float:
    empieza = 2.0

    while empieza <= a:
        empieza = math.pow(empieza, 2)

    return empieza

def raiz_cuadrada_iterativa(
    a: float, max_iter: int = 9999, tolerance: float = 0.00000000000001
) -> float:
    """
    La raiz cuadrada esta aproximada usando el método de Newton
    https://en.wikipedia.org/wiki/Newton%27s_method

    """

    if a < 0:
        raise ValueError("Error de dominio matemático")

    valor = obtener_punto_de_init(a)

    for i in range(max_iter):
        valor_previo = valor
        valor = valor - fx(valor, a) / fx_derivada(valor)
        if abs(valor_previo - valor) < tolerance:
            return valor

    return valor

if __name__ == "__main__":
    numero=int(input("Dame el número para obtener su raiz cuadrada: "))
    print(raiz_cuadrada_iterativa(numero))
 