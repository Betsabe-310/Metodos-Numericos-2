from os import system
from math import exp
from numpy import matmul, array, linalg, vstack


def menu():
    print("**********Metodo de Newton Rapson**********\n")
    print("1. Sistema de ecuaciones:")
    print("f1(x, y) = x^2+xy-10=0")
    print("f2(x, y) = y+3xy^2-50=0")

    print("2. Sistema de ecuaciones:")
    print("f1(x, y) = x^2+y^2-9=0")
    print("f2(x, y) = -e^x-2y-3=0")

    print("3. Sistema de ecuaciones:")
    print("f1(x, y,z) = 2x^2-4x+y^2+3z^2+6z+2=0")
    print("f2(x, y,z) = x^2+y^2-2y+2z^2-5=0")
    print("f2(x, y,z) = 3x^2-12x+y^2-3z^2+8=0")

    print("4. Sistema de ecuaciones:")
    print("f1(x, y,z) = x^2-4x+y^2=0")
    print("f2(x, y,z) =x^2-x-12y+1=0")
    print("f2(x, y,z) =3x^2-12x+y^2-3z^2+8=0")

    print("5. Regresar al menú principal")


def primerSistema():
    mas = 's'
    aux = 's'
    while mas == 's':
        print("El sistema de ecuaciones es:\n")
        print("f1(x, y) = x^2+xy-10=0\n")
        print("f2(x, y) = y+3xy^2-50=0\n\n")

    # derivada parcial de la primera funcion
        print("f1'x=2x+y\t")
        print("f1'y=x\t\n")

    # derivada parcial de la segunda funcion
        print("f2'x=3y^2\t")
        print("f2'y=6yx+1\t\n")

        puntos = [0, 0]
        puntos2 = [0, 0]
        errorauxpuntos = [0, 0]
        maxaux1 = 0
        maxaux2 = 0
        error = 0
        tol = 0
        it = 0

        puntos[0] = int(input("Ingresa el primer punto: "))
        puntos[1] = int(input("Ingresa el segundo punto: "))
        it = int(input("\nIngresa las iteraciones: "))
        tol = float(input("Ingresa la tolerancia: "))
        jacobina = [[0 for i in range(2)] for j in range(2)]
        evalFunc = [[0 for i in range(1)] for j in range(2)]
        for k in range(it):
            jacobina[0][0] = 2*puntos[0]+puntos[1]
            jacobina[0][1] = puntos[0]
            jacobina[1][0] = 3*(puntos[1]*puntos[1])
            jacobina[1][1] = 6*puntos[1]*puntos[0]+1

            evalFunc[0][0] = (puntos[0]*puntos[0])+(puntos[0]*puntos[1])-10
            evalFunc[1][0] = puntos[1]+(3*puntos[0]*(puntos[1]*puntos[1]))-50

            #inversa
            arr = array(jacobina)
            arr_inv = linalg.inv(arr)

            multJPorF = matmul(arr_inv, vstack(evalFunc))

            puntos2[0] = puntos[0] - multJPorF[0,0]
            puntos2[1] = puntos[1] - multJPorF[1,0]

            for i in range(2):
                errorauxpuntos[i] = abs(puntos2[i]-puntos[i])

            if errorauxpuntos[0] > errorauxpuntos[1]:
                maxaux1 = errorauxpuntos[0]
            else:
                maxaux1 = errorauxpuntos[1]
            if abs(puntos2[0]) > abs(puntos2[1]):
                maxaux2 = puntos2[0]
            else:
                maxaux2 = puntos2[1]
            error = maxaux1/abs(maxaux2)

            puntos[0] = puntos2[0]
            puntos[1] = puntos2[1]
            if error < tol:
                print("\nFin por toleracia:")
                print("\nIteraciones: ", k+1)
                print("\nerror: ", error)
                print("\npuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))
                break
            elif it == k+1:
                print("\nFin por Iteraciones: ", k+1)
                print("\nerror: ", error)
                print("\npuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))
                break
            print("\n")
            print("ITERACION: ", k+1)
            print("\nERROR: ", error)
            print("\npuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))
        aux = input("\n¿Quiéres aproximar otro punto? s o n\n")

        if aux == 'n':
            mas = 'n'
        system("cls")


# Segunda ecuación
def segundoSistema():
    mas = 's'
    aux = 's'
    while mas == 's':
        print("El sistema de ecuaciones es:\n")
        print("f1(x, y) = x^2+y^2-9=0\n")
        print("f2(x, y) = -e^x-2y-3=0\n\n")

        # derivada parcial de la primera funcion
        print("f1'x=2x \t")
        print("f1'y=2y\t\n")

        # derivada parcial de la segunda funcion
        print("f2'x=-e^x\t")
        print("f2'y=-2\t\n")

        puntos = [0, 0]
        puntos2 = [0, 0]
        errorauxpuntos = [0, 0]
        maxaux1 = 0
        maxaux2 = 0
        error = 0
        tol = 0
        it = 0

        puntos[0] = int(input("Ingresa el primer punto: "))
        puntos[1] = int(input("Ingresa el segundo punto: "))

        it = int(input("Ingresa las iteraciones: "))
        tol = float(input("Ingresa la tolerancia: "))

        jacobina = [[0 for i in range(2)] for j in range(2)]
        evalFunc = [[0 for i in range(1)] for j in range(2)]
        for k in range(it):
            jacobina[0][0] = 2*puntos[0]
            jacobina[0][1] = 2*puntos[1]
            jacobina[1][0] = -exp(puntos[0])
            jacobina[1][1] = -2

            evalFunc[0][0] = (puntos[0]*puntos[0])+(puntos[1]*puntos[1])-9
            evalFunc[1][0] = -exp(puntos[0])-(2*puntos[1])-3

            # inversa
            arr = array(jacobina)
            arr_inv = linalg.inv(arr)

            # print("Multiplicacion: \n")
            multJPorF = matmul(arr_inv, vstack(evalFunc))

            # print(multJPorF[0,0])
            # print(multJPorF[1,0])

            puntos2[0] = puntos[0] - multJPorF[0, 0]
            puntos2[1] = puntos[1] - multJPorF[1, 0]

            for i in range(2):
                errorauxpuntos[i] = abs(puntos2[i]-puntos[i])

            if errorauxpuntos[0] > errorauxpuntos[1]:
                maxaux1 = errorauxpuntos[0]
            else:
                maxaux1 = errorauxpuntos[1]
            if abs(puntos2[0]) > abs(puntos2[1]):
                maxaux2 = puntos2[0]
            else:
                maxaux2 = puntos2[1]
            error = maxaux1 / abs(maxaux2)

            puntos[0] = puntos2[0]
            puntos[1] = puntos2[1]
            if error < tol:
                print("\nFin por toleracia:")
                print("\nIteraciones: ", k+1)
                print("\nError: ", error)
                print("\npuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))
                break
            elif it == k+1:
                print("\nFin por Iteraciones: ", k+1)
                print("\nError: ", error)
                print("\npuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))
                break
            print("\n\n")
            print("ITERACION: ", k+1)
            print("\nERROR: ", error)
            print("\nPuntos: x: {} y: {}".format(puntos2[0], puntos2[1]))

        aux = input("\n¿Quiéres aproximar otro punto? s o n:")
        if aux == 'n':
            mas = 'n'
        system("cls")


def tercerSistema():
    mas='s'
    aux='s'
    while mas == 's':
        print("El sistema de ecuaciones es:\n")
        print("f1(x, y,z) = 2x^2-4x+y^2+3z^2+6z+2=0\n")
        print("f2(x, y,z) = x^2+y^2-2y+2z^2-5=0\n")
        print("f2(x, y,z) = 3x^2-12x+y^2-3z^2+8=0\n\n")

        # derivada parcial de la primera funcion
        print("f1'x=4x-4\t")
        print("f1'y=2y \t")
        print("f1'z=6z+6\t\n")

        # derivada parcial de la segunda funcion
        print("f2'x=2x \t")
        print("f2'y=2y-2\t")
        print("f2'z=4z\t\n")

        # derivada parcial de la tercera funcion
        print("f3'x=6x-12\t")
        print("f3'y=2y \t")
        print("f3'z=-6z\t\n")

        puntos = [0, 0, 0]
        puntos2 = [0, 0, 0]
        errorauxpuntos = [0, 0, 0]
        maxaux1 = 0
        maxaux2 = 0
        error = 0
        tol = 0
        it = 0

        puntos[0] = int(input("Ingresa el primer punto: "))
        puntos[1] = int(input("Ingresa el segundo punto: "))
        puntos[2] = int(input("Ingresa el tercer punto: "))
        it = int(input("\nIngresa las iteraciones:"))
        tol = float(input("\nIngresa la tolerancia:"))

        jacobina = [[0 for i in range(3)] for j in range(3)]
        evalFunc = [[0 for i in range(1)] for j in range(3)]
        for k in range(it):
            jacobina[0][0] = 4*puntos[0]-4
            jacobina[0][1] = 2*puntos[1]
            jacobina[0][2] = 6*puntos[2]+6
            jacobina[1][0] = 2*puntos[0]
            jacobina[1][1] = 2*puntos[1]-2
            jacobina[1][2] = 4*puntos[2]
            jacobina[2][0] = 6*puntos[0]-12
            jacobina[2][1] = 2*puntos[1]
            jacobina[2][2] = -6*puntos[2]

            evalFunc[0][0] = 2*pow(puntos[0], 2)-4*puntos[0]+pow(puntos[1], 2)+3*pow(puntos[2], 2)+6*puntos[2]+2
            evalFunc[1][0] = pow(puntos[0], 2)+pow(puntos[1], 2)-2*puntos[1]+2*pow(puntos[2], 2)-5
            evalFunc[2][0] = 3*pow(puntos[0], 2)-12*puntos[0]+pow(puntos[1], 2)-3*pow(puntos[2], 2)+8

            # inversa
            arr = array(jacobina)
            arr_inv = linalg.inv(arr)

            multJPorF = matmul(arr_inv, vstack(evalFunc))

            puntos2[0] = puntos[0] - multJPorF[0, 0]
            puntos2[1] = puntos[1] - multJPorF[1, 0]
            puntos2[2] = puntos[2] - multJPorF[2, 0]

            for i in range(3):
                errorauxpuntos[i] = abs(puntos2[i]-puntos[i])
            if errorauxpuntos[0]>errorauxpuntos[1] and errorauxpuntos[0] > errorauxpuntos[2]:
                maxaux1 = errorauxpuntos[0]
            elif errorauxpuntos[1]>errorauxpuntos[0] and errorauxpuntos[1] > errorauxpuntos[2]:
                maxaux1 = errorauxpuntos[1]
            else:
                maxaux1 = errorauxpuntos[2]

            if abs(puntos2[0]) > abs(puntos2[1]) and abs(puntos2[0]) > abs(puntos2[2]):
                maxaux2 = puntos2[0]
            elif abs(puntos2[1]) > abs(puntos2[0]) and abs(puntos2[1]) > abs(puntos2[2]):
                maxaux2 = puntos2[1]
            else:
                maxaux2 = puntos2[2]
            error = maxaux1 / abs(maxaux2)

            puntos[0] = puntos2[0]
            puntos[1] = puntos2[1]
            puntos[2] = puntos2[2]

            if error < tol:
                print("\nFin por toleracia:")
                print("\nIteraciones: ", k+1)
                print("\nError: ", error)
                print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))
                break
            elif it == k+1:
                print("\nFin por Iteraciones: ", k+1)
                print("\nError: ", error)
                print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))
                break
            print("\n")
            print("\nITERACION: ", k+1)
            print("\nERROR: ", error)
            print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))

        aux = input("\n¿Quiéres aproximar otro punto? s o n\n")
        if aux == 'n':
            mas='n'
        system("cls")


def cuartoSistema():
    mas='s'
    aux='s'
    while mas == 's':
        print("El sistema de ecuaciones es:")
        print("f1(x, y,z) = x^2-4x+y^2=0")
        print("f2(x, y,z) =x^2-x-12y+1=0")
        print("f2(x, y,z) =3x^2-12x+y^2-3z^2+8=0")

        # derivada parcial de la primera funcion
        print("f1'x=2x-4\t")
        print("f1'y=2y\t")
        print("f1'z=0\t\n")

        # derivada parcial de la segunda funcion
        print("f2'x=2x-1 \t")
        print("f2'y=-12\t")
        print("f2'z=0\t\n")

        # derivada parcial de la tercera funcion
        print("f3'x=6x-12\t")
        print("f3'y=2y \t")
        print("f3'z=-6z\t\n")

        puntos = [0, 0, 0]
        puntos2 = [0, 0, 0]
        errorauxpuntos = [0, 0, 0]
        maxaux1 = 0
        maxaux2 = 0
        error = 0
        tol = 0
        it = 0

        puntos[0] = int(input("Ingresa el primer punto: "))
        puntos[1] = int(input("Ingresa el segundo punto: "))
        puntos[2] = int(input("Ingresa el tercer punto: "))
        it = int(input("\nIngresa las iteraciones:"))
        tol = float(input("\nIngresa la tolerancia:"))

        jacobina = [[0 for i in range(3)] for j in range(3)]
        evalFunc = [[0 for i in range(1)] for j in range(3)]
        for k in range(it):
            jacobina[0][0] = 2*puntos[0]-4
            jacobina[0][1] = 2*puntos[1]
            jacobina[0][2] = 0
            jacobina[1][0] = 2*puntos[0]-1
            jacobina[1][1] = -12
            jacobina[1][2] = 0
            jacobina[2][0] = 6*puntos[0]-12
            jacobina[2][1] = 2*puntos[1]
            jacobina[2][2] = -6*puntos[2]

            evalFunc[0][0] = pow(puntos[0], 2)-4*puntos[0]+pow(puntos[1], 2)
            evalFunc[1][0] = pow(puntos[0], 2)-puntos[0]-12*puntos[1]+1
            evalFunc[2][0] = 3*pow(puntos[0], 2)-12*puntos[0]+pow(puntos[1], 2)-3*pow(puntos[2], 2)+8

            # inversa
            arr = array(jacobina)
            arr_inv = linalg.inv(arr)

            multJPorF = matmul(arr_inv, vstack(evalFunc))

            puntos2[0] = puntos[0] - multJPorF[0, 0]
            puntos2[1] = puntos[1] - multJPorF[1, 0]
            puntos2[2] = puntos[2] - multJPorF[2, 0]

            for i in range(3):
                errorauxpuntos[i] = abs(puntos2[i]-puntos[i])

            if errorauxpuntos[0] > errorauxpuntos[1] and errorauxpuntos[0] > errorauxpuntos[2]:
                maxaux1 = errorauxpuntos[0]
            elif errorauxpuntos[1] > errorauxpuntos[0] and errorauxpuntos[1] > errorauxpuntos[2]:
                maxaux1 = errorauxpuntos[1]
            else:
                maxaux1 = errorauxpuntos[2]

            if abs(puntos2[0]) > abs(puntos2[1]) and abs(puntos2[0]) > abs(puntos2[2]):
                maxaux2 = puntos2[0]
            elif abs(puntos2[1]) > abs(puntos2[0]) and abs(puntos2[1]) > abs(puntos2[2]):
                maxaux2 = puntos2[1]
            else:
                maxaux2 = puntos2[2]
            error = maxaux1 / abs(maxaux2)

            puntos[0] = puntos2[0]
            puntos[1] = puntos2[1]
            puntos[2] = puntos2[2]

            if error < tol:
                print("\nFin por toleracia: \n")
                print("\nIteraciones: ", k+1)
                print("\nError: ", error)
                print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))
                break
            elif it == k+1:
                print("\nFin por Iteraciones: ", k+1)
                print("\nError: ", error)
                print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))
                break
            print("\n")
            print("\nITERACION: ", k+1)
            print("\nERROR: ", error)
            print("\nPuntos: x: {} y: {} z: {}".format(puntos2[0], puntos2[1], puntos2[2]))

        aux = input("\n¿Quiéres aproximar otro punto? s o n\n")
        if aux == 'n':
            mas='n'
        system("cls")


def newton_main():
    newton = True
    while newton:
        system('cls')
        menu()
        opcion = int(input("Selecciona una opcion: "))
        system('cls')
        if opcion == 1:
            primerSistema()
        elif opcion == 2:
            segundoSistema()
        elif opcion == 3:
            tercerSistema()
        elif opcion == 4:
            cuartoSistema()
        elif opcion == 5:
            newton = False
        else:
            print("Esa opción no es valida, intente de nuevo.")


if __name__ == "__main__":
    newton_main()