def fibonacci_iteractivo(n):
    n = int(n)
    secuancia_inicial=[0,1]
    a, b= 0, 1
    for _ in range(n-len(secuancia_inicial)):
        a, b= b, a + b
        secuancia_inicial.append(b)
    return secuancia_inicial

n=int(input('Dame el número para mostrarte su secuencia Fibonacci: '))
print(fibonacci_iteractivo(n))