def main():
    nombre=input("Dame tu nombre: ")
    a_paterno=input("Dame tu apellido paterno: ")
    a_materno=input("Dame tu apellido materno: ")
    nombre_completo= nombre +" "+ a_paterno +" " +a_materno
    print("Es un gusto conocerte: ", nombre_completo)


if __name__=='__main__':
    main()