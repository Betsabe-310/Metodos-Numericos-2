import os
import time


def menu():
    print("********Interpolación Polinomial********")
    print("1. Leer datos")
    print("2. Leer datos para interpolar")
    print("3. Salir")


def mostrar(valor, x, y):
    os.system('cls')
    print("Y   \tX")
    for i in range(valor):
        print(f"Y{i}:{y[i]}\tX{i}:{x[i]}")


def leer_datos():
    orden = True
    correcto = False
    y = []
    x = []
    while not correcto:
        valor = int(input("Cuantos pares hay en la tabla?: "))
        for i in range(valor):
            x.append(float(input(f"Valor para X{i}: ")))
            y.append(float(input(f"Valor para Y{i}: ")))
            os.system('cls')
        mostrar(valor, x, y)
        for i in range(valor):
            if (x[i] > x[i + 1]):
                orden = False
                break
            if i >= valor - 2:
                break
        if not orden:
            print("Los valores no estan ordenados.\nLos valores se ordenaran conforme a X.")
            x, y = map(list, zip(*sorted(zip(x, y))))
            mostrar(valor, x, y)
        c = input("La tabla es correcta?: si/no ")
        if c.lower() == "no":
            correcto = False
            print("Debe ingresar los datos nuevamente.")
        else:
            correcto = True

    return y, x



def interpolacion(x, y):
    print("ADVERTENCIA: Los valores se ordenaran conforme a X.")
    print("Unicamente para este método pero la tabla original quedará intacta.")
    x, y = map(list, zip(*sorted(zip(x, y))))
    correcto = False
    resultado = 0
    while not correcto:
        interpolar = float(input("Punto a interpolar: "))
        if (interpolar < x[0] or  interpolar > x[-1]):
            print("El valor no esta dentro del intervalo de valores de la tabla")
            print("Ingrese el valor de nuevo.")
            time.sleep(1.5)
            correcto = False
            continue

        grado = -1
        while grado == -1:
            grado = int(input("Grado Polinomio: "))
            if (len(y) < grado+1):
                print("No hay suficientes puntos para interporlar a ese grado.")
                print("Ingresa otro valor")
                grado = -1

        lista_grados = [y]
        contador = 1
        for i in range(grado):
            aux = []
            aux_y = lista_grados[-1].copy()
            for j in range(len(aux_y) - 1):
                aux.append((aux_y[j + 1] - aux_y[j]) / (x[j + contador] - x[j]))
            contador += 1
            lista_grados.append(aux)

        restas = []
        for i in range(len(x)):
            r = 1
            for j in range(i + 1):
                r *= (interpolar - x[j])
            restas.append(r)

        resultado = lista_grados[0][0]
        for i in range(grado):
            resultado += restas[i] * lista_grados[i + 1][0]
        break

    return resultado


def dif_main(x=[], y=[]):
    if len(x) != 0:
        print("ADVERTENCIA: Los valores se ordenaran conforme a X.")
        x, y = map(list, zip(*sorted(zip(x, y))))
    dif_ = True
    while dif_:
        os.system('cls')
        menu()
        opcion = int(input("opcion: "))
        if opcion == 1:
            os.system('cls')
            y, x = leer_datos()
        elif opcion == 2:
            os.system('cls')
            otra = True
            while otra:
                otra = True
                if len(x) == 0:
                    print("Debe ingresar los datos primero.")
                    time.sleep(1)
                    os.system('cls')
                    break
                resultado = interpolacion(y, x)
                print("El resultado es: ", resultado)
                c = input("Quiere hacer otra interpolacion con la misma tabla? si/no: ")
                if c.lower() == "si":
                    continue
                else:
                    otra = False
                c = input("Quiere regresar al menu principal? si/no: ")
                if c.lower() == "si":
                    continue
                else:
                    dif_ = False

        elif opcion == 3:
            dif_ = False
    return x, y


if __name__ == "__main__":
    dif_main()