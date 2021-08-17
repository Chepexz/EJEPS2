import math
import os

def main():
    os.system("clear")
    a = float(input("ingrese el valor para el cateto 'A' cateto: "))
    b = float(input("ingrese el valor para el cateto 'B' cateto: "))
    c = math.sqrt((a*a+b*b))
    print(str(F"El valor de la Hipotenusa es: {c}"))

if __name__=='__main__':
    main()
