from time import sleep
from os import system
from numpy import array, newaxis, transpose, zeros, linalg, matmul, insert


def menu():
    print("********Spline cubico********")
    print("Marta Betsabe Núñez Ibáñez")
    print("Solis Vilchis Roberto Atonatiuh")
    print("1. Leer datos")
    print("2. Interpolar")
    print("3. Salir")


def mostrar(valor=0, x=[], y=[]):
    system('cls')
    print("Tabla de Valores")
    print("        X      Y")
    for i in enumerate(zip(x,y)):
        print(i[0],"-  ",i[1][0],"  ",i[1][1])


def leer_datos():
    correcto = False
    #y = [-1.1,0.27,-0.29,0.56,1]  #[0.36,2.12,2.38,3.24,3.04,3.72,4,2.46,1.58,1.5,3.3,3.74,2.96,0.62,0.66,0.46,0.78]#[4.17, 3.73, 3.56, 2.37, 1.3, 0.48, .94]
    #x = [0.95,1.73,2.23,2.77,2.99]   #[3.08,2.58,0.92,1.86,2.76,3,4,4.02,3.56,4.98,6.94,9.02,10.22,9.98,8.98,8.1,7.62]#[1.24, 2.04, 3.67, 4.59, 6, 7.28, 10.04]
    while not correcto:
        y = []
        x = []
        valor = int(input("Cuantos pares hay en la tabla?: "))
        for i in range(valor):
            x.append(float(input(f"Valor para X{i}: ")))
            y.append(float(input(f"Valor para Y{i}: ")))
            system('cls')
        mostrar(valor, x, y)
        c = input("La tabla es correcta?: si/no ")
        if c.lower() == "no":
            resp = int(input("Quieres cambiar la tabla completa o un valor?: 0-completa  1-valor(es): "))
            if resp == 0:
                correcto = False
                continue
            if resp == 1:
                indice = input("Ingresa los indices que quieres cambiar separados por comas 2,3,5,etc: ")
                indice = indice.split(",")
                for i in indice:
                    x[int(i)] = float(input(f"Valor para X{int(i)}: "))
                    y[int(i)] = float(input(f"Valor para Y{int(i)}: "))
                correcto = True


        else:
            correcto = True
    system('cls')
    return x, y


def spline(x, y):
    h = []
    f1 = []
    for i in range(len(x)-1):
        h.append(x[i+1]-x[i])
    for i in range(len(x)-1):
        f1.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    f1_diff = array([0.0 for x in range(len(f1)-1)])[newaxis].T
    for i in range(len(f1)-1):
        f1_diff[i] = ((f1[i+1]-f1[i])*6)
    f1_diff = f1_diff.T
    f1_diff = transpose(array(f1_diff))
    matrix = zeros((len(h)-1, len(x)))
    limit = 0
    for i in range(matrix.shape[0]):
        cont = 0
        for j in range(limit, limit+3):
            if cont == 0:
                matrix[i, j] = h[limit]
            elif cont == 1:
                matrix[i, j] = 2*(h[limit+1]+h[limit])
            elif cont == 2:
                matrix[i, j] = h[limit+1]
            cont += 1
        limit = limit + 1
    # matrix_ver = matrix
    matrix = matrix[:, 1:-1]
    inv_matrix = linalg.inv(matrix)
    vector = matmul(inv_matrix, f1_diff)

    vector = insert(vector, 0, 0)
    vector = insert(vector, len(vector), 0)
    vector = vector.reshape(len(vector),1)
    tabla_coef = dict()
    for i in range(3):
        aux = []
        if i==0:
            for j in range(len(vector) - 1):
                aux.append(((vector[j+1]-vector[j])/(6*h[j]))[0])
            tabla_coef['ai']=aux
        if i==1:
            for j in range(len(vector) - 1):
                aux.append((vector[j]/2)[0])
            tabla_coef['bi'] = aux
        if i==2:
            for j in range(len(vector) - 1):
                aux.append((((y[j+1]-y[j])/h[j])-((vector[j+1] + 2*vector[j])/6)*h[j])[0])
            tabla_coef['ci'] = aux

    print("Polinomios: ")
    for i in enumerate(zip(tabla_coef['ai'], tabla_coef['bi'], tabla_coef['ci'], y[:-1])):
        print(
            f"g{i[0]}x: {round(i[1][0], 3)}(x-{x[i[0]]})^3+{round(i[1][1], 3)}(x-{x[i[0]]})^2+{round(i[1][2], 3)}(x-{x[i[0]]})+{round(i[1][3], 3)}    {x[i[0]]}<=x<={x[i[0] + 1]}")


def spline_main(x=[], y=[]):
    spline_ = True
    while spline_:
        system('cls')
        menu()
        opcion = int(input("opcion: "))
        if opcion == 1:
            system('cls')
            x, y = leer_datos()
        elif opcion == 2:
            system('cls')
            otra = True
            while otra:
                if len(x) == 0:
                    print("Debe ingresar los datos primero.")
                    sleep(2)
                    system('cls')
                    break
                spline(x, y)
                c = input("Quiere interpolar con otra tabla? si/no: ")
                if c.lower() == "si":
                    y, x = leer_datos()
                else:
                    otra = False
                    spline_ = False

        elif opcion == 3:
            spline_ = False
    return x, y


if __name__ == "__main__":
    spline_main()