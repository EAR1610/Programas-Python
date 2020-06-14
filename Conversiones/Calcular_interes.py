#Se recolectan los datos para realizar la operación.
nombre=input("Dame tu nombre: ")
capitalInicial=float(input(f"Hola {nombre}, dame el capital inicial: "))
tazaInteres=float(input("Dame la taza de interes (ej: 1.5, solo números): "))
tiempo= float(input("Dame el tiempo (cantidad de años): "))
formula= capitalInicial*(1+(tazaInteres)/100)**(tiempo*4) #Formula para la ecuación

print(f"{ nombre}, el valor final de tu inversión despues de {tiempo} años es:", round(formula,2))