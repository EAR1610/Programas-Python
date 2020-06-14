def coeficiente_binomial(n, k):
    C=[0 for i in range(k + 1)]
    C[0]=1

    for i in range(1, n + 1):
        j = min(i,k)
        while j>0:
            C[j] += C[j - 1]
            j-=1
    return C[k]

n=int(input('Dame el número de conjuntos: '))
k=int(input('Dame el número de elementos para escoger en el conjunto: '))
print(coeficiente_binomial(n,k))