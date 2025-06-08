import time, random

#----- INFORMACION DE LA BASE DE DATOS -----#

# FUNCION PARA GENERAR UNA LISTA DE MANERA DINAMICA
def generar_alumnos(n, legajo_inicial=1):
    nombres_base = ["Franco", "Brian", "Martina", "Mateo", "Lucia", "Lucas", "Martin", "Luciana", "Brenda", "Ana", "Marcos", "David", "Rocio", "Luz", "Valentina", "Ulises", "Roman", "Emiliano"]
    alumnos_generados = []

    for i in range(n):
        nombre = random.choice(nombres_base)
        legajo = legajo_inicial + i
        promedio = random.randint(0, 100)
        alumnos_generados.append({"nombre": nombre, "legajo": legajo, "promedio": promedio})

    return alumnos_generados

alumnos = generar_alumnos(500, 1)

# ALGORITMO DE BUSQUEDA LINEAL
def busqueda_lineal(lista, clave):

    for alumno in lista:
        if alumno["legajo"] == clave:
            return alumno
    
    return None

# ALGORITMO DE BUSQUEDA BINARIA
def busqueda_binaria(lista_ordenada, clave):

    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        legajo_actual = lista_ordenada[medio]["legajo"]

        if legajo_actual == clave:
            return lista_ordenada[medio]
        elif legajo_actual < clave:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None

# ALGORITMO DE ORDENAMIENTO RAPIDO (QUICKSORT)
def ordenamiento_rapido(lista, clave):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
    mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]

    return ordenamiento_rapido(menores, clave) + [pivote] + ordenamiento_rapido(mayores, clave)

# ALGORITMO DE ORDENAMIENTO BURBUJA
def ordenamiento_burbuja(lista, clave):
    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][clave] > lista[j + 1][clave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


# FUNCION PARA BUSCAR ALUMNOS POR LEGAJO
def busca_alumnos(lista, legajo):

    opcion_busqueda = input("""¿Qué tipo de búsqueda quiere hacer? 

    1. Busqueda Lineal.
    2. Busqueda Binaria.

    Seleccione una opción: """)

    if opcion_busqueda == "1":
        print("INICIO BUSQUEDA LINEAL")
        print("------------------------")
        tiempo_inicio = time.perf_counter()
        alumno_obtenido = busqueda_lineal(lista, legajo)
        if alumno_obtenido:
            tiempo_fin = time.perf_counter()
            tiempo_transcurrido = (tiempo_fin - tiempo_inicio) * 1000 # LO PASAMOS A MILISEGUNDOS

            print(f"Tiempo transcurrido: {tiempo_transcurrido:.3f} milisegundos") # MUESTRO 3 DECIMALES
            print(f"Alumno encontrado: {alumno_obtenido}")
            print("------------------------")
            print("FIN BUSQUEDA LINEAL")
        else:
            print(f"No se encontró el alumno con el legajo {legajo}")

    elif opcion_busqueda == "2":
        print("INICIO BUSQUEDA BINARIA")
        print("------------------------")

        # PRIMERO ORDENO LA LISTA
        lista_ordenada = ordenamiento_rapido(lista, "legajo")

        tiempo_inicio = time.perf_counter()
        alumno_obtenido = busqueda_binaria(lista_ordenada, legajo)
        if alumno_obtenido:
            tiempo_fin = time.perf_counter()
            tiempo_transcurrido = (tiempo_fin - tiempo_inicio) * 1000 # LO PASAMOS A MILISEGUNDOS

            print(f"Tiempo transcurrido: {tiempo_transcurrido:.3f} milisegundos") # MUESTRO 3 DECIMALES
            print(f"Alumno encontrado: {alumno_obtenido}")
            print("------------------------")
            print("FIN BUSQUEDA BINARIA")
        else:
            print(f"No se encontro el alumno con el legajo {legajo}")
    
    else:
        print("Opcion invalida.")
        return


# FUNCION PARA ORDENAR ALUMNOS POR CLAVE
def ordena_alumnos(lista, clave):
    """
    if clave not in["nombre", "legajo", "promedio"]:
        print("La clave ingresada no es válida. Las claves válidas son nombre, legajo y promedio")
        return
    """

    opcion_ordenamiento = input("""¿Qué tipo de ordenamiento quiere hacer? 

    1. Ordenamiento rapido.
    2. Ordenamiento burbuja.

    Seleccione una opción: """)

    if opcion_ordenamiento == "1":

        print("INICIO ORDENAMIENTO RAPIDO")
        print("------------------------")
        tiempo_inicio = time.perf_counter()

        lista_ordenada = ordenamiento_rapido(lista, clave)

        tiempo_fin = time.perf_counter()

        tiempo_transcurrido = (tiempo_fin - tiempo_inicio) * 1000

        # print(f"Tiempo transcurrido: {tiempo_transcurrido:.3f} milisegundos")
        print(f"Lista ordenada: {lista_ordenada}")
        print("------------------------")
        print("FIN ORDENAMIENTO RAPIDO")

    elif opcion_ordenamiento == "2":

        print("INICIO ORDENAMIENTO BURBUJA")
        print("------------------------")
        tiempo_inicio = time.perf_counter()

        lista_ordenada = ordenamiento_burbuja(lista, clave)

        tiempo_fin = time.perf_counter()

        tiempo_transcurrido = (tiempo_fin - tiempo_inicio) * 1000

        # print(f"Tiempo transcurrido: {tiempo_transcurrido:.3f} milisegundos")
        print(f"Lista ordenada: {lista_ordenada}")
        print("------------------------")
        print("FIN ORDENAMIENTO BURBUJA")

    else:
        print("opcion invalida")


#----- PROGRAMA PRINCIPAL -----#
print("Trabajo Practico Integrador - Algoritmos de Busqueda y Ordenamiento")
print("Brian Gutierrez Colque - Franco Herrera")
print("---------------------------------------")
opcion = input("""¿Qué desea hacer? 

1. Buscar alumno por legajo.
2. Ordenar alumnos por clave.

Seleccione una opción: """)

if opcion == "1":

    legajo_a_buscar = int(input("Ingrese el legajo del alumno a buscar: "))
    busca_alumnos(alumnos, legajo_a_buscar)

elif opcion == "2":

    clave = input("Ingrese la clave por la que va a ordenar [nombre], [legajo] o [promedio]: ")
    ordena_alumnos(alumnos, clave)

else:
    print ("Opción inválida")