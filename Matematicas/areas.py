"""Busca el area de varias formas geometricas"""

import math

def area_rectangular(base, altura):
    """Calcula el area de un rectangulo
    Ejemplo area_rectangular(10,20)
    La respuesta sería: 200"""
    return base*altura

def area_cuadrado(largo_lado):
    """Calcula el area de un cuadrado
    Ejemplo area_cuadrado(10)
    La respuesta sería 100"""
    return largo_lado * largo_lado

def area_triangular(longitud, amplitud):
    """Calcula el area de un triangulo
    Ejemplo area_triangulo(10,10)
    La respuesta sería 50.0"""
    return 1/2 * longitud * amplitud

def area_paralelogramo(base, altura):
    """Calcula el area de un palarelogramo
    Ejemplo area_paralelogramo(10, 20)
    La respuesta sería 200"""
    return base * altura

def area_trapecio(base1, base2, altura):
    """Calcula el area de un trapecio
    Ejemplo area_trapecio(10,20,30)
    La respuesta sería 450"""
    return 1 / 2 * (base1 + base2) * altura

def area_circulo(radio):
    """Calcula el area de un circulo
    Ejemplo area_circulo(20)
    La respuesta sería 1256.6370614359173"""
    return math.pi * radio * radio

def area_cilindro(radio, altura):
    """Calcula el area de un cilindro
    Ejemplo area_cilindro(4, 10)
    La respuesta sería 351.86"""
    return 2 * math.pi * radio * (radio + altura)

def area_exagono(lados):
    """Calcula el area de un hexágono
    Ejemplo area_exagono(7)
    La respuesta sería 127.26"""
    perimetro= lados * 6
    h=lados * lados
    hipotenusa = math.pow((lados / 2), 2)
    apotema= round(math.sqrt(h - hipotenusa), 2)
    print(perimetro, hipotenusa, apotema)
    return round((perimetro * apotema) / 2, 2)

def main():
    print('Areas de varias formas geométricas')
    print('¿Qué quieres calcular?\nArea de un rectángulo: 1\nArea de un cuadrado: 2\nArea de un triaungulo: 3\nArea de un paralelogramo: 4\nArea de un trapecio: 5\nArea de un circulo: 6\nArea cilindro: 7\Area exagonal: 8')
    eleccion = int(input('Dame tu elección (1 - 8): '))
    if eleccion == 1:
        print("Has elegido el area de un rectángulo")
        base=int(input('Dame la base del rectangulo: '))
        altura = int(input('Dame la altura del rectangulo: '))
        print(area_rectangular(base, altura))
    elif eleccion == 2:
        print('Has elegido area de un cuadrado')
        largo_lado=int(input('Dame el lado largo de un cuadrado: '))
        print(area_cuadrado(largo_lado))
    elif eleccion == 3:
        print('Has elegido area de un triangulo')
        longitud=int(input('Dame la longitud del triangulo: '))
        amplitud=int(input('Dame la amplitud del triangulo: '))
        print(area_triangular(longitud, amplitud))
    elif eleccion == 4:
        print('Has elegido el area de un paralelogramo')
        base=int(input('Dame el area de un paralelogramo: '))
        altura=int(input('Dame la altura del paralelogramo: '))
        print(area_paralelogramo(base, altura))
    elif eleccion == 5:
        print('Has elegido area de un trapecio')
        base1= int(input('Dame la base menor del trapecio: '))
        base2= int(input('Dame la base mayor del trapecio: '))
        altura= int(input('Dame la altura del trapecio: '))
        print(area_trapecio(base1,base2,altura))
    elif eleccion == 6:
        print('Has elegido area de un circulo')
        radio=int(input('Dame el radio del circulo: '))
        print(round(area_circulo(radio),2))
    elif eleccion == 7:
        print('Has elegido area de un cilindro')
        radio=int(input('Dame el radio del cilindro: '))
        altura=int(input('Dame la altura del cilindro: '))
        print(round(area_cilindro(radio, altura),2))
    elif eleccion == 8:
        print('Has elegido area de un hexagono')
        lados= int(input('Dame la longitud del lado del hexagono: '))
        print(area_exagono(lados))
    else:
        print('Debes de darme un número del 1 - 8')

if __name__ == '__main__':
    main()