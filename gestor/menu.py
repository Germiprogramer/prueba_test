import gestor.helpers as helpers
from gestor.database import Calculadora

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Suma ")
        print("[2] Resta  ")
        print("[3] Multiplicación   ")
        print("[4] División  ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            try:
                num1 = int(input("Elige el primer número:"))
                num2 = int(input("Elige el segundo número:"))
            except:
                pass

            try:
                print(Calculadora.suma(num1,num2))
            except:
                print("Ha habido un error")
                pass


        elif opcion == '2':
            try:
                num1 = int(input("Elige el primer número:"))
                num2 = int(input("Elige el segundo número:"))
            except:
                pass
            try:
                print(Calculadora.resta(num1,num2))
            except:
                print("Ha habido un error")
                pass
        
        elif opcion == '3':
            try:
                num1 = int(input("Elige el primer número:"))
                num2 = int(input("Elige el segundo número:"))
            except:
                pass

            try:
                print(Calculadora.producto(num1,num2))
            except:
                print("Ha habido un error")
                pass
        
        elif opcion == '4':
            try:
                num1 = int(input("Elige el primer número:"))
                num2 = int(input("Elige el segundo número:"))
            except:
                pass

            try:
                print(Calculadora.division(num1,num2))
            except:
                print("Ha habido un error")
                pass

        else:
            print("No se ha recibido el número correcto")
        
        input("Presiona enter para continuar. ")