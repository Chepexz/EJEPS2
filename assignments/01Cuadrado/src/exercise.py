import math
import os
def main():
    os.system("cls")
    lado = float(input("Dame tu valor del lado del cuadrado "))

    perimetro = 4 * lado
    """
    area = lado * lado
    area = lado ** 2
    """
    area = math.pow(lado,2)

    print("El perímetro del cuadrado de lado " + str(lado) + "es " + str(perimetro))
    print(f"El área del cuadrado de lado {lado} es: {area}")

if __name__=='__main__':
    main()
