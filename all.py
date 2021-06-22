from os import system
from time import sleep

from newton import newton_main
from diferencias_divididas import interpolacion
from SplineCubico import spline, mostrar, leer_datos
from diferenciacion_integracion import dif_int_main


def menu():
    print("********Métodos Numéricos********")
    print("Marta Betsabe Núñez Ibáñez")
    print("Solis Vilchis Roberto Atonatiuh")
    print("1. Sistemas de ecuaciones no lineales")
    print("2. Interpolación y ajuste de curvas")
    print("3. Diferenciación e integración (datos igualmente espaciados)")
    print("4. Salir")


def sub_menu():
    print("********Métodos Numéricos********")
    print("Marta Betsabe Núñez Ibáñez")
    print("Solis Vilchis Roberto Atonatiuh")
    print("1. Leer la tabla")
    print("2. Interpolación (Diferencias divididas)")
    print("3. Ajuste por spline cúbico.")
    print("4. Regresar al menú principal")


def main():
    x2, y2 = [], []
    x3, y3 = [], []
    dif_ = True
    while dif_:
        system('cls')
        menu()
        try:
            opcion = int(input("opcion: "))
        except:
            opcion = 0
        if opcion == 1:
            system('cls')
            newton_main()
        elif opcion == 2:
            aux_spline = True
            while aux_spline:
                system('cls')
                if len(x2)!=0:
                    print("Ya existe una tabla, si utilizas algún método por defecto se usará esa.")
                    sleep(1.5)
                sub_menu()
                try:
                    opcion2 = int(input("opcion: "))
                except:
                    opcion2 = 0
                if opcion2 == 1:
                    system('cls')
                    x2, y2 = leer_datos()
                elif opcion2 == 2:
                    system('cls')
                    if len(x2)==0:
                        print("Necesitas ingresar una tabla primero.")
                        sleep(1.5)
                        continue
                    print("Resultado: ", interpolacion(x2, y2))
                    input("Presiona una tecla para continuar.")
                elif opcion2 == 3:
                    system('cls')
                    if len(x2)==0:
                        print("Necesitas ingresar una tabla primero.")
                        sleep(1.5)
                        continue
                    spline(x2, y2)
                    input("Presiona una tecla para continuar.")
                elif opcion2 == 4:
                    aux_spline = False
                else:
                    print("La opción es incorrecta. Intenta con otro valor")
        elif opcion == 3:
            system('cls')
            x3, y3 = dif_int_main(x3, y3)
        elif opcion == 4:
            print("Hasta pronto...")
            dif_ = False
            sleep(1.5)
        else:
            print("La opción es incorrecta. Intenta con otro valor")

# y = [0.96079, 0.75910, 0.48554, 0.25142, 0.10540]
# x = [0.2,0.525,0.85,1.175,1.5]
main()