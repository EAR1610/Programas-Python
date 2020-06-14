def romano_a_entero(roman: str) -> int:
    valores= {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,}
    total=0
    lugar=0

    while lugar<len(roman):
        if (lugar + 1 < len(roman)) and (valores[roman[lugar]] < valores[roman[lugar+1]]):
            total+= valores[roman[lugar+1]] - valores[roman[lugar]]
            lugar+=2
        else:
            total+=valores[roman[lugar]]
            lugar+=1
    return total

numero_romano=input('Dame el número romano: ').upper()
print(romano_a_entero(numero_romano))

if __name__ == "__main__":
    import doctest
    doctest.testmod()