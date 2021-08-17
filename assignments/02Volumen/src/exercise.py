import math
import os
def main():
    os.system("cls")
    radio = float(input("Dame el valor del radio de la esfera: "))
    volumen = 4 / 3 * math.pi * math.pow(radio,3)

    print(f"El volumen de la esfera con radio {radio} es {volumen} unidades cubicas")

if __name__=='__main__':
    main()