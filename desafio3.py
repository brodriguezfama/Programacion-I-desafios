restaurantes=[[1,"Don Julio","Guillermo González","Carnes"],
              [2,"El Preferido de Palermo","Juan Pablo","Fusión"],
              [3,"La Cabrera","Martín Cabrera","Carnes"],
              [4,"El Club del Vino","Laura Martínez","Vinos"],
              [5,"Tegui","Nicolás Riera","Gastronomía Fina"],
              [6,"Pizzería Guerrín","María González","Pizzas"]]

def organizar(restaurantes_):
    rts_ord=[[ID,Nombre[:15],Propietario[:12],Cocina[:10]]
             for ID,Nombre,Propietario,Cocina in restaurantes_]
    for i in range(len(rts_ord)):
        rts_ord[i][1]=rts_ord[i][1].upper()
        rts_ord[i][2]=rts_ord[i][2].upper()
        rts_ord[i][3]=rts_ord[i][3].upper()
    rts_ord2=sorted(rts_ord,key=lambda x:(x[1],x[2],x[0]))
    return rts_ord2

def crear(a):
    a.append([])
    for campo in a[0]:
        a[-1].append(0)
    bandera = 0
    while bandera == 0:
        nombre = input("Ingrese el nombre del restaurante: ")
        if nombre.isalpha() or " " in nombre:
            propietario = input("Ingrese el nombre del propietario: ")
            if propietario.isalpha() or " " in propietario:
                cocina = input("Ingrese el tipo de cocina: ")
                if cocina.isalpha() or " " in cocina:
                    bandera = -1
    a[-1][0] = a[0][0] + 1
    a[-1][1] = nombre
    a[-1][2] = propietario
    a[-1][3] = cocina
    return a

def leer(b):
    print(f"{'ID':>6} {'Nombre':^20} {'Propietario':^15} {'Cocina':<10}")
    print("="*50)
    for ID, Nombre, Propietario, Cocina in b:
        print(f"{ID:>6} {Nombre:^20} {Propietario:^15} {Cocina:<10}")

def actualizar(c):
    bandera = 0
    while bandera == 0:
        opcion = int(input("¿Qué dato quiere actualizar?: 1-ID, 2-Nombre, 3-Propietario, 4-Cocina: "))
        bandera = 1
        if opcion == 1:
            id_cambiar = int(input("Ingrese el ID que desea cambiar: "))
            encontrado = False
            index = -1
            while not encontrado and index < len(c) - 1:
                index += 1
                if c[index][0] == id_cambiar:
                    encontrado = True
            if encontrado:
                c[index][0] = int(input("Ingrese el nuevo ID: "))
                return c
            else:
                print("Error, el ID ingresado no se encuentra.")
        else:
            id_fila = int(input("Ingrese el ID de la fila del restaurante que desea actualizar: "))
            encontrado = False
            index = -1
            while not encontrado and index < len(c) - 1:
                index += 1
                if c[index][0] == id_fila:
                    encontrado = True
            if not encontrado:
                print("No se encuentra el ID ingresado.")
            else:
                actualizar_opcion = int(input("¿Qué desea cambiar?: 1-Nombre, 2-Propietario, 3-Cocina: "))
                if actualizar_opcion == 1:
                    c[index][1] = input("Ingrese el nuevo nombre: ")
                    return c
                elif actualizar_opcion == 2:
                    c[index][2] = input("Ingrese el nuevo propietario: ")
                    return c
                elif actualizar_opcion == 3:
                    c[index][3] = input("Ingrese el nuevo tipo de cocina: ")
                    return c
                else:
                    print("Dato incorrecto")
                    bandera = 0
def eliminar(d):
    encontrado = False
    index = -1
    while not encontrado and index < len(d) - 1:
        id_eliminar = input("Ingrese el ID que desea eliminar: ")
        index += 1
        if d[index][0] == id_eliminar and id_eliminar.isnumeric():
            d.pop(index)
            return d
        else:
            print("No se encontró el ID ingresado.")
            encontrado = False

restaurantes_ordenados = organizar(restaurantes)
flag1 = 0
flag2 = -1
while flag1 == 0:
    if flag2 == 0:
        restaurantes_ordenados = organizar(restaurantes)
        flag2 = -1
    des = int(input("Seleccione una acción: 1. CREAR, 2. LEER, 3. ACTUALIZAR, 4. ELIMINAR, 5. DETENER: "))
    if des == 1:
        restaurantes_ordenados = crear(restaurantes_ordenados)
        flag2 = 0
    elif des == 2:
        leer(restaurantes_ordenados)
    elif des == 3:
        restaurantes_ordenados = actualizar(restaurantes_ordenados)
        flag2 = 0
    elif des == 4:
        restaurantes_ordenados = eliminar(restaurantes_ordenados)
        flag2 = 0
    elif des == 5:
        flag1 = 1