nombre=input("Dame tu nombre: ") 
eleccion=input(f"Muy bien {nombre}, ¿Qué deseas hacer? \nConvertir galones a litros = 1 \nConvertir litros a galones = 2 \nConvertir litros a mililitros = 3 \nConveritir galones a mililitros = 4\nDame tu opción (solo números): ")

if eleccion=="1" or eleccion=="01":

    galones=float(input("¿Cuantos galones deseas convertir?: "))
    litros=galones*3.7854118
    print(f"{galones} galones equivalen a: {litros} litros.")

elif eleccion=="2" or eleccion=="02":

    litros=float(input("¿Cuantos litros deseas convertir?: "))
    galones=litros*0.2641720512415584
    print(f"{litros} litros equivalen a: {galones} galones")

elif eleccion=="3" or eleccion=="03":

    litros=float(input("¿Cuantos litros deseas convertir?: "))
    mililitros=litros*1000
    print(f"{litros} litros equivalen a: {mililitros} mililitros")

elif eleccion=="4" or eleccion=="04":
    galones=float(input("¿Cuantos galones deseas convertir?: "))
    mililitros=galones*3785.41
    print(f"{galones} galones equivalen a: {mililitros} mililitros: ")
else:
    print("No me has dado un número válido, recuerda que el número debe estar entre 1 y 4 o 01 y 04")
