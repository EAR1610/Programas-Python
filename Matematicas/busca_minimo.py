def busca_minimo(num):
    num_min= num[0]
    for n in num:
        if num_min>n:
            num_min=n
    return num_min

def main():
    print('Dame los números: ')
    datos = list(map(float, input("").split(',')))
    print(busca_minimo(datos))

if __name__=="__main__":
    main()