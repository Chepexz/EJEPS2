import math
import os

def main():
    os.system("clear")
    h = 6
    l = 15
    perimetro= (h * 2) + (l * 2)
    area= h * l

    print(F"Base rectángulo = {l}")
    print(F"Altura rectángulo = {h}")
    print(F"Perimetro del rectángulo = {perimetro}")
    print(F"Área del rectángulo = {area}")

if __name__=='__main__':
    main()

