"""Convierte un número decimal a numeros binarios"""

def decimal_a_binario(num:int) ->str:

    if num==0:
        return "0b0"
    
    negativo=False

    if num<0:
        negativo=True
        num=-num
    
    binario = []

    while num>0:
        binario.insert(0, num % 2)
        num >>=1
    
    if negativo:
        return ("-0b"+"".join(str(e) for e in binario))

    return ("".join(str(e) for e in binario))

numero_decimal=int(input("Dame el número decimal: "))

print(decimal_a_binario(numero_decimal))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    