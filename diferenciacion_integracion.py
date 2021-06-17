from os import system
from time import sleep
# NOTA: impar n-3 1/3 y a los 3 restantes la de simpson 3/8


def menu():
    print("********Diferenciación e Integración********")
    print("Marta Betsabe Núñez Ibáñez")
    print("Solis Vilchis Roberto Atonatiuh")
    print("1. Leer datos")
    print("2. Diferenciación")
    print("3. Integración")
    print("4. Salir")


def espaciado(x):
    h = round(x[1] - x[0], 5)
    for i in range(len(x)-1):
        if h != round(x[i+1] - x[i], 5):
            return None
    else:
        return h


def leer_datos():
    correcto = True
    while correcto:
        num_datos = int(input("Número de datos: "))
        x0 = round(float(input("Valor inicial X0: ")), 5)
        h = round(float(input("Tamaño pasos (h): ")),5)
        x = []
        aux = x0
        for i in range(num_datos):
            x.append(round(aux, 5))
            aux+=h
        y = []
        for i in range(num_datos):
            print(f"x{i}: {x[i]}")
            y.append(float(input(f"Valor para y{i}: ")))
        mostrar(x, y)
        c = input("La tabla es correcta?: si/no ")
        if c.lower() == "no":
            resp = int(input("Quieres cambiar la tabla completa o un valor?: 0-completa  1-valor(es): "))
            if resp == 0:
                correcto = True
                system('cls')
                continue
            elif resp == 1:
                indice = input("Ingresa los indices que quieres cambiar separados por comas 2,3,5,etc: ")
                indice = indice.split(",")
                for i in indice:
                    y[int(i)] = float(input(f"Valor para Y{int(i)}: "))
                sleep(1)
                correcto = False
        else:
            correcto = False
    return x, y, h


def diferenciacion(x, y, ind, h):
    print("\n")
    print("*****Derivada*****")
    print(f"f'({x[ind]}): {(y[ind+1]-y[ind-1])/(2*h)}")
    print(f"f''({x[ind]}): {(y[ind + 1] - 2*y[ind] + y[ind - 1]) / (h**2)}")


def simpson1_3(y, h):
    n = len(y) - 1
    suma = 0
    for i in enumerate(y):
        if i[0] == 0:
            suma += i[1]
        elif i[0] == n:
            suma += i[1]
        else:
            if i[0] % 2 == 0:
                suma += 2 * i[1]
            else:
                suma += 4 * i[1]
    return h*suma/3


def simpson3_8(y, h):
    return (3*h/8)*(y[0]+3*y[1]+3*y[2]+y[3])


def integracion(x, y, h):
    if len(y) % 2 != 0:
        print("h = ", h)
        print(f"Integral de {x[0]} a {x[-1]}: ", simpson1_3(y, h))
    else:
        print("h = ", h)
        print(f"Integral de {x[0]} a {x[-1]}: ", simpson3_8(y[-4:], h)+simpson1_3(y[:-3], h))


def mostrar(x, y):
    system('cls')
    print("Tabla de Valores")
    print("        X      Y")
    for i in enumerate(zip(x,y)):
        print(i[0],"-  ",i[1][0],"  ",i[1][1])


def dif_int_main(x=[], y=[]):
    if len(x) != 0:
        print("!ADVERTENCIA¡: Los valores se ordenaran conforme a X.")
        x, y = map(list, zip(*sorted(zip(x, y))))
        h = espaciado(x)
        if h is None:
            print("No están igualemete espaciados los datos, agrega una nueva tabla")
            x, y, h = leer_datos()
            system('cls')

    dif_ = True
    while dif_:
        system('cls')
        menu()
        opcion = int(input("opcion: "))
        if opcion == 1:
            system('cls')
            x, y, h = leer_datos()
        elif opcion == 2:
            c = True
            if len(x) == 0:
                print("Necesitas ingresar los datos antes.")
                sleep(1)
                continue
            elif len(x) < 3:
                print("Necesitas al menos 3 registros en la tabla.")
                print("Ingresa una con más valores.")
                sleep(1.5)
                continue
            while c:
                system('cls')
                mostrar(x, y)
                while True:
                    ind = int(input("Dame el indice del valor del cual quieras saber la derivada: "))
                    if ind == 0 or ind == (len(x)-1):
                        print("Esos indices son inválidos, necesitas al menos 1 antes y 1 después.")
                        sleep(1.5)
                        continue
                    diferenciacion(x, y, ind, h)
                    break
                res = input("Quieres realizar otra aproximación? s/n: ")
                if res.lower() != 's':
                    break
        elif opcion == 3:
            system('cls')
            if len(x) == 0:
                print("Necesitas ingresar los datos antes.")
                sleep(1.5)
                continue
            integracion(x, y, h)
            input("presiona una tecla para continuar...")
        elif opcion == 4:
            print("Hasta Pronto...")
            sleep(1.5)
            return 0


#y = [0.96079, 0.75910, 0.48554, 0.25142, 0.10540]
#x = [0.2,0.525,0.85,1.175,1.5]
# diff
#y = [0.18096748, 0.25821239, 0.3274923, 0.38940039]
#x = [0.2, 0.3, 0.4, 0.5]
dif_int_main()