def busca_maximo(nums):
    num_max=nums[0]
    for x in nums:
        if x > num_max:
            num_max = x
    return num_max

def main():
    print('Dame los números a continuación: ')
    datos = list(map(float, input("").split(',')))
    print(busca_maximo(datos))

if __name__ == "__main__":
    main()