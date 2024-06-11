from Package_operaciones.Input import get_int, get_str
import os


def cargar_peliculas():
    lista_peliculas = []
    archivo_existente = os.path.exists('peliculas.csv')

    if not archivo_existente:
        with open('peliculas.csv', 'w') as archivo_nuevo:
            archivo_nuevo.write("Título,Género,Año de lanzamiento,Duración,ATP,Plataformas\n")
    
    try:
        with open('peliculas.csv', 'r') as archivo:
            next(archivo)  # omitir la primera línea (encabezados)
            for linea in archivo:
                datos = linea.strip().split(',')
                pelicula = {
                    "Título": datos[0],
                    "Género": datos[1],
                    "Año de lanzamiento": int(datos[2]),
                    "Duración": int(datos[3]),
                    "ATP": datos[4].lower() == "true",  # convertir "true" a True, "false" a False
                    "Plataformas": datos[5].split(';')
                }
                lista_peliculas.append(pelicula)
    except FileNotFoundError:
        print("No se pudo abrir el archivo 'peliculas.csv'.")

    return lista_peliculas

def guardar_peliculas(lista_peliculas):
    try:
        with open('peliculas.csv', 'w') as archivo:
            archivo.write("Título,Género,Año de lanzamiento,Duración,ATP,Plataformas\n")
            for pelicula in lista_peliculas:
                archivo.write(f"{pelicula['Título']},{pelicula['Género']},{pelicula['Año de lanzamiento']},"
                              f"{pelicula['Duración']},{pelicula['ATP']},{';'.join(pelicula['Plataformas'])}\n")
        print("Listado de películas guardado exitosamente en 'peliculas.csv'")
    except Exception as e:
        print(f"Error al guardar el listado de películas: {str(e)}")
# Verifica que el titulo no exceda los 30 caracteres, que sus caracteres sean alfanuméricos y especiales y que no haya
# dos peliculas con el mismo titulo(utiliza las funciones titulo_unico() y validar_caracteres()).
def validar_titulo(titulo, lista_peliculas):
    while True:
        if len(titulo) > 30:
            titulo = get_str("El título no puede exceder los 30 caracteres: ", 1, 30)
        elif validar_caracteres(titulo):
            if titulo_unico(titulo):
                return titulo
            else:
                titulo = get_str("Ya existe una película con ese título. Ingrese otro: ", 1, 30)
        else:
            titulo = get_str("El título solo puede contener caracteres alfanuméricos y caracteres especiales: ", 1, 30)

def titulo_unico(titulo: str) -> bool:
    try:
        with open('peliculas.csv', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(',')
                if datos[0] == titulo:
                    return False
    except FileNotFoundError:
        return True
    return True

# Comprueba que el título esté compuesto por caracteres alfanuméricos y especiales, si lo está retorna true, si no, false
def validar_caracteres(titulo: str):
    for char in titulo:
        if ord(char) < 32 or ord(char) > 126:
            return False
    return True

# Lista de géneros válidos
generos_validos = [
    "accion", "aventura", "animacion", "biografico", "comedia", "comedia romantica", "comedia dramatica", "crimen",
    "documental", "drama", "fantasia", "historico", "infantil", "musical", "misterio", "policiaco", "romance",
    "ciencia ficcion", "suspenso", "terror", "western", "belico", "deportivo", "noir", "experimental", "familiar",
    "superheroes", "espionaje", "artes marciales", "fantastico", "catastrofe", "melodrama", "erotico", "cine independiente",
    "zombies", "vampiros", "cyberpunk", "steampunk", "distopia", "utopia", "road movie", "docuficcion", "mockumentary",
    "gotico", "slasher", "adolescente", "culto", "maravilloso"
]

# Valida el ingreso del género
def validar_genero(genero):
    while True:
        os.system('cls')
        if len(genero) > 30:
            os.system('cls')
            genero = get_str(f"El género no puede exceder los 30 caracteres:\n{generos_validos}", 1, 30)
        else:
            genero_sin_tildes = convertir_cadena_simple(genero.lower())
            if genero_sin_tildes in generos_validos:
                return genero_sin_tildes
            else:
                genero = get_str(f"El género ingresado no es válido. Por favor, elija uno de los géneros válidos.\n{generos_validos}",1,30)

# Convierte el género ingresado a una palabra sin tildes para facilitar el ingreso
def convertir_cadena_simple(cadena: str):
    cadena_simple = cadena.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return cadena_simple

#pide y valida la duracion dada por el usuario
def validar_duracion(duracion):
    while True:
        if duracion.isdigit():
            duracion_pelicula = int(duracion)
            if duracion_pelicula >= 0:
                return duracion_pelicula
        duracion = input("Error, ingrese una duración válida (en minutos): ")

# Valida si la película es o no es ATP y devuelve true o false
def validar_ATP():
    while True:
        respuesta_usuario = respuesta_si_no("Es ATP (apta para todo público)? Si/No: ")
        if respuesta_usuario is not None:
            return respuesta_usuario

def respuesta_si_no(mensaje):
    while True:
        respuesta = get_str(mensaje, 2, 3)
        respuesta = respuesta.lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Por favor, responda con 'si' o 'no'.")

        
# Genera el id de las películas de la lista. Si no hay, su id será 1 y si hay, toma el valor del último id
def generar_nuevo_id(lista_peliculas):
    if not lista_peliculas:  # Verifica si la lista está vacía
        return 1  # Si está vacía, el primer ID será 1
    else:
        # Buscar el último ID y asignar el siguiente
        ultimo_id = 0
        for pelicula in lista_peliculas:
            id_pelicula = pelicula.get("ID", 0)
            if id_pelicula > ultimo_id:
                ultimo_id = id_pelicula
        nuevo_id = ultimo_id + 1
        return nuevo_id

#busca la pelicula por el titulo
def buscar_pelicula_por_titulo(lista_peliculas, titulo):
    for pelicula in lista_peliculas:
        if pelicula["Título"] == titulo:
            return pelicula
    return None

# Se usa en modificar película
def modificar_genero_pelicula(lista_peliculas, titulo, nuevo_genero):
    for pelicula in lista_peliculas:
        if pelicula["Título"] == titulo:
            pelicula["Género"] = nuevo_genero
            print("¡Género actualizado con éxito!")
            return True
    return False

#Imprime la pelicula en su formato correspondiente
def imprimir_info_pelicula(pelicula):
    print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
        pelicula["Título"], pelicula["Género"], pelicula["Año de lanzamiento"], 
        pelicula["Duración"], "si" if pelicula["ATP"] else "no", ";".join(pelicula["Plataformas"])
    ))

#Se usa para ver si quiere elegir ascendentemente o descentemente(sirve para la funcion ordenar_peliculas())
def elegir_orden():
    while True:
        orden = input("Desea ordenar de forma ascendente o descendente? (asc/desc): ").strip().lower()
        if orden in ["asc", "desc"]:
            return orden
        else:
            print("Por favor, ingrese 'asc' para ascendente o 'desc' para descendente.")

def ordenar_peliculas_por_titulo(lista_peliculas, orden):#ordena peliculas por su titulo de forma ascendente o descente segun el usuario
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (orden == "asc" and lista_peliculas[j]["Título"] > lista_peliculas[j + 1]["Título"]) or \
               (orden == "desc" and lista_peliculas[j]["Título"] < lista_peliculas[j + 1]["Título"]):
                lista_peliculas[j], lista_peliculas[j + 1] = lista_peliculas[j + 1], lista_peliculas[j]
    return lista_peliculas

def ordenar_peliculas_por_genero(lista_peliculas, orden):#ordena peliculas por su genero de forma ascendente o descente segun el usuario
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (orden == "asc" and lista_peliculas[j]["Género"] > lista_peliculas[j + 1]["Género"]) or \
               (orden == "desc" and lista_peliculas[j]["Género"] < lista_peliculas[j + 1]["Género"]):
                lista_peliculas[j], lista_peliculas[j + 1] = lista_peliculas[j + 1], lista_peliculas[j]
    return lista_peliculas

def ordenar_peliculas_por_año(lista_peliculas, orden):#ordena peliculas por su año de lanzamiento de forma ascendente o descente segun el usuario
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (orden == "asc" and lista_peliculas[j]["Año de lanzamiento"] > lista_peliculas[j + 1]["Año de lanzamiento"]) or \
               (orden == "desc" and lista_peliculas[j]["Año de lanzamiento"] < lista_peliculas[j + 1]["Año de lanzamiento"]):
                lista_peliculas[j], lista_peliculas[j + 1] = lista_peliculas[j + 1], lista_peliculas[j]
    return lista_peliculas

def ordenar_peliculas_por_duracion(lista_peliculas, orden):#ordena peliculas por su duracion de forma ascendente o descente segun el usuario
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (orden == "asc" and lista_peliculas[j]["Duración"] > lista_peliculas[j + 1]["Duración"]) or \
               (orden == "desc" and lista_peliculas[j]["Duración"] < lista_peliculas[j + 1]["Duración"]):
                lista_peliculas[j], lista_peliculas[j + 1] = lista_peliculas[j + 1], lista_peliculas[j]
    return lista_peliculas

def calcular_duracion_promedio(lista_peliculas):#Calcula la duracion promedio
    if not lista_peliculas:
        return 0

    total_duracion = 0
    for pelicula in lista_peliculas:
        total_duracion += pelicula["Duración"]

    promedio_duracion = total_duracion / len(lista_peliculas)
    return promedio_duracion

def contar_peliculas_por_año(lista_peliculas):
    conteo_por_año = {}

    for año in range(2005, 2025):
        conteo_por_año[año] = 0
        
    for pelicula in lista_peliculas:
        año_lanzamiento = pelicula["Año de lanzamiento"]
        if 2005 <= año_lanzamiento <= 2024:
            conteo_por_año[año_lanzamiento] += 1

    return conteo_por_año

def calcular_porcentaje_genero(lista_peliculas):
    genero_contador = {}
    total_peliculas = len(lista_peliculas)

    for pelicula in lista_peliculas:
        genero = pelicula["Género"]
        if genero in genero_contador:
            genero_contador[genero] += 1
        else:
            genero_contador[genero] = 1

    print("Porcentaje por género:")
    for genero in genero_contador:
        contador = genero_contador[genero]
        porcentaje = (contador / total_peliculas) * 100
        porcentaje_formateado = "{:.2f}%".format(porcentaje)
        print(f"{genero}: {porcentaje_formateado}")

def calcular_porcentaje_ATP(lista_peliculas):
    total_peliculas = len(lista_peliculas)
    atp_contador = 0

    for pelicula in lista_peliculas:
        if pelicula["ATP"]:
            atp_contador += 1

    no_atp_contador = total_peliculas - atp_contador

    porcentaje_atp = (atp_contador / total_peliculas) * 100
    porcentaje_no_atp = (no_atp_contador / total_peliculas) * 100

    print("Porcentaje por ATP:")
    print("ATP: {:.2f}%".format(porcentaje_atp))
    print("No ATP: {:.2f}%".format(porcentaje_no_atp))

def validar_plataformas() -> list:
    while True:
        plataformas_input = input("Ingrese las plataformas separadas por '/': ")
        plataformas = plataformas_input.split('/')

        plataformas_validas = []
        es_valido = True
        for plataforma in plataformas:
            plataforma_limpia = plataforma.strip()
            if plataforma_limpia.replace(" ", "").isalpha() and len(plataforma_limpia) <= 20:
                plataformas_validas.append(plataforma_limpia)
            else:
                print(f"Nombre de plataforma inválido: '{plataforma_limpia}'. Debe contener solo caracteres alfabéticos o especiales, no caracteres numéricos y no exceder los 20 caracteres.")
                es_valido = False
                break

        if es_valido:
            return plataformas_validas
        
