def pedir_numero_valido(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero")

def pedir_numero_mayor_a_cero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Error: debe ser un numero mayor a 0")
        except ValueError:
            print("Error: debe ingresar un numero")

'''
num = pedir_numero_valido("Ingrese numero de prueba")
print(num)
'''

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def menu():
    menu_activo = True

    while menu_activo:
        print("----MENU OPERACIONES---")
        print("1.- sumar")
        print("2.- restar")
        print("3.- multiplicar")
        print("4.- dividir")
        print("5.- Salir")
        opcion = pedir_numero_mayor_a_cero("Ingrese la opción de menu: ")

        match opcion:
            case 1:
                n1 = pedir_numero_valido("Ingrese primer numero: ")
                n2 = pedir_numero_valido("Ingrese segundo numero: ")
                print(f"resultado: {suma(n1,n2)}")
            case 2:
                n1 = pedir_numero_valido("Ingrese primer numero: ")
                n2 = pedir_numero_valido("Ingrese segundo numero: ")
                print(f"resultado: {resta(n1,n2)}")
            case 3:
                n1 = pedir_numero_valido("Ingrese primer numero: ")
                n2 = pedir_numero_valido("Ingrese segundo numero: ")
                print(f"resultado: {mult(n1,n2)}")
            case 4:
                n1 = pedir_numero_valido("Ingrese primer numero: ")
                n2 = pedir_numero_mayor_a_cero("Ingrese segundo numero: ")
                print(f"resultado: {div(n1,n2)}")
            case 5:
                print("Usted saldrá del programa")
                menu_activo = False
            case _:
                print("opción incorrecta!!")

menu()                





