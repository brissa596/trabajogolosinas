
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10],
]


empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}


clavesTecnico = ("admin", "CCCDDD", "2020")

golosinasPedidas = []




def mostrar_menu():
    print("\n MÁQUINA DE GOLOSINAS")
    print("a) Pedir golosina")
    print("b) Mostrar golosinas")
    print("c) Rellenar golosinas (Técnico)")
    print("d) Apagar máquina")


def mostrar_golosinas():
    print("\n--- STOCK DE GOLOSINAS ---")
    for codigo, nombre, stock in golosinas:
        print(f"{codigo}. {nombre} -> Stock: {stock}")


def pedir_golosina():
    legajo = int(input("Ingrese su legajo: "))

    if legajo not in empleados:
        print("Usted no es un empleado de la empresa.")
        return

    while True:
        mostrar_golosinas()
        opcion = input("Ingrese el código de la golosina (o 'salir' para terminar): ")

        if opcion.lower() == "salir":
            break

        codigo = int(opcion)

        encontrado = False
        for golosina in golosinas:
            if golosina[0] == codigo:
                encontrado = True
                if golosina[2] > 0: 
                    golosina[2] -= 1
                    print(f"Se entregó {golosina[1]}.")
                    registrar_pedido(codigo, golosina[1])
                else:
                    print(f"la golosina {golosina[1]} no se encuentra disponible.")
                break

        if not encontrado:
            print("Código inexistente.")


def registrar_pedido(codigo, nombre):
  
    for pedido in golosinasPedidas:
        if pedido[0] == codigo:
            pedido[2] += 1
            return
    golosinasPedidas.append([codigo, nombre, 1])


def rellenar_golosinas():
    print("Ingrese las 3 claves de técnico en orden:")
    clave1 = input("Clave 1: ")
    clave2 = input("Clave 2: ")
    clave3 = input("Clave 3: ")

    if (clave1, clave2, clave3) != clavesTecnico:
        print("No tiene permiso para ejecutar la función de recarga.")
        return

    codigo = int(input("Ingrese el código de la golosina a recargar: "))
    cantidad = int(input("Ingrese la cantidad a recargar Mayor a 0: "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    encontrado = False
    for golosina in golosinas:
        if golosina[0] == codigo:
            golosina[2] += cantidad
            print(f"Se recargaron {cantidad} unidades de {golosina[1]}. Stock actual: {golosina[2]}")
            encontrado = True
            break

    if not encontrado:
        print("Código inexistente.")


def apagar_maquina():
    print("\n PEDIDOS ")
    total = 0
    for codigo, nombre, cantidad in golosinasPedidas:
        print(f"{codigo}. {nombre} -> Pedidas: {cantidad}")
        total += cantidad
    print(f"\nTotal de golosinas pedidas: {total}")
    print("Apagando máquina")
    exit()



while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").lower()

    if opcion == "a":
        pedir_golosina()
    elif opcion == "b":
        mostrar_golosinas()
    elif opcion == "c":
        rellenar_golosinas()
    elif opcion == "d":
        apagar_maquina()
    else:
        print("Opción no válida.")
