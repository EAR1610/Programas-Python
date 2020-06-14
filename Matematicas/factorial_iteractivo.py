def factorial(n:int) ->int:

    if n != int(n):
        raise ValueError('La funcion factorial solamente acepta valores enteros')
    if n < 0:
        raise ValueError('La funcion factorial no define números negativos')

    valores=1
    for i in range(1, n+1):
        valores *=i
    return valores

if __name__=="__main__":
    n=int(input('Dame un número entero positivo: ').strip() or 0)
    print(f'El factorial de {n} es {factorial(n)}')
    