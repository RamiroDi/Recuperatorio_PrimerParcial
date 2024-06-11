# peliculas.py: Donde se realizan todas las funciones que permitan interactuar con la entidad película.
from inputs import *

def agregar_pelicula(lista_peliculas):#Pide el ingreso de datos y agrega un nueva pelicula a la lista en forma de diccionario
    ID = generar_nuevo_id(lista_peliculas)
    titulo = validar_titulo(input("Ingrese el título de la película:\n"), lista_peliculas)
    genero = validar_genero(input(f"Ingrese un genero de la lista para la pelicula:\n{generos_validos}"))
    año_lanzamiento = get_int("Ingresa un año entre 1888 y el año actual: ","Por favor, ingresa un año válido entre 1888 y el año actual.",1888, 2024)
    duracion = input("Ingrese la duración de la película en minutos: ")
    duracion_validada = validar_duracion(duracion)
    apto_todo_publico = validar_ATP()
    plataformas = validar_plataformas()

    os.system('cls')

    nueva_pelicula = {
        "ID": ID,
        "Título": titulo,
        "Género": genero,
        "Año de lanzamiento": año_lanzamiento,
        "Duración": duracion_validada,
        "ATP": apto_todo_publico,
        "Plataformas": plataformas
    }

    lista_peliculas.append(nueva_pelicula)

def modificar_pelicula(lista_peliculas):
    while True:
        titulo = get_str("Ingrese el título de la película a modificar: ", 1, 30)
        pelicula_encontrada = buscar_pelicula_por_titulo(lista_peliculas, titulo)

        if pelicula_encontrada:
            print("Película encontrada:")
            print("*" * 150)
            print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                "Título", "Género", "Año de lanzamiento",
                "Duración", "ATP", "Plataformas"))
            imprimir_info_pelicula(pelicula_encontrada)
            print("*" * 150)
            while True:
                opcion = get_int("""Qué desea modificar?\n
                                    1. Género\n
                                    2. Año de lanzamiento\n
                                    3. Duración\n
                                    4. ATP\n
                                    5. Plataformas\n
                                    6. Salir\n""", "Error, introduzca un número válido", 1, 6)

                match opcion:
                    case 1:
                        genero_nuevo = input("Ingrese el nuevo género: ")
                        genero = validar_genero(genero_nuevo)
                        pelicula_encontrada["Género"] = genero
                        print("¡Género actualizado con éxito!")
                    case 2:
                        nuevo_año = get_int("Ingrese el nuevo año de lanzamiento: ", "Error, ingrese un año válido", 1888, 2024)
                        pelicula_encontrada["Año de lanzamiento"] = nuevo_año
                        print("Año de lanzamiento actualizado con éxito")
                    case 3:
                        nueva_duracion = validar_duracion(input("Ingrese la nueva duración de la película en minutos: "))
                        pelicula_encontrada["Duración"] = nueva_duracion
                        print("Duración actualizada con éxito")
                    case 4:
                        nuevo_ATP = validar_ATP()
                        pelicula_encontrada["ATP"] = nuevo_ATP
                        print("Clasificación ATP actualizada con éxito")
                    case 5:
                        plataformas_nuevas = validar_plataformas()
                        pelicula_encontrada["Plataformas"] = plataformas_nuevas
                        print("Plataformas actualizadas con éxito")
                    case 6:
                        break

                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                imprimir_info_pelicula(pelicula_encontrada)
                print("*" * 150)

                continuar = respuesta_si_no("Desea seguir modificando? Si/No: ")
                if not continuar:
                    break
        else:
            print("No se encontró ninguna película con ese título.")
            continuar = respuesta_si_no("Desea buscar otra película? Si/No: ")
            if not continuar:
                break

def eliminar_pelicula(lista_peliculas):#Pide el titulo de una pelicula y le pregunta si realmente desea eliminarla
    while True:
        titulo = get_str("Ingrese el título de la película a eliminar: ", 1, 30)
        pelicula_encontrada = buscar_pelicula_por_titulo(lista_peliculas, titulo)
        
        if pelicula_encontrada is not None:
            print("Película encontrada:")
            imprimir_info_pelicula(pelicula_encontrada)
            
            eliminar = respuesta_si_no("Desea eliminar esta película? Si/No: ")
            if eliminar:
                lista_peliculas.remove(pelicula_encontrada)
                print("Película eliminada con éxito")
            else:
                print("La película no fue eliminada.")
        else:
            print("No se encontró ninguna película con ese título.")
        
        continuar = respuesta_si_no("Desea eliminar otra película? Si/No: ")
        if not continuar:
            break

def mostrar_peliculas(lista_peliculas):
    while True:
        opcion = get_int("""
        Menú de opciones:
        1. Todas las películas.
        2. Películas por género.
        3. Películas por año.
        4. Películas aptas para todo público.
        5. Películas no aptas para todo público.
        6. Películas por plataforma.
        7. Salir.
        Ingrese el número de la opción deseada: ""","Error ingrese una opcion valida",1,7)
        match opcion:
            case 1:
                print("Todas las películas:")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 2:
                genero = validar_genero(input("Ingrese el género para filtrar: "))
                print(f"Películas del género '{genero}':")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    if pelicula["Género"] == genero:
                        imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 3:
                año = get_int("Ingrese el año para filtrar: ", "Error, ingrese un año válido", 1888, 2024)
                print(f"Películas del año {año}:")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    if pelicula["Año de lanzamiento"] == año:
                        imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 4:
                print("Películas aptas para todo público:")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    if pelicula["ATP"]:
                        imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 5:
                print("Películas no aptas para todo público:")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    if not pelicula["ATP"]:
                        imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 6:
                plataforma = input("Ingrese la plataforma para filtrar: ")
                print(f"Películas disponibles en la plataforma '{plataforma}':")
                print("*" * 150)
                print("| {:<30} | {:<30} | {:<30} | {:<30} | {:<14} | {:<30} |".format(
                    "Título", "Género", "Año de lanzamiento",
                    "Duración", "ATP", "Plataformas"))
                for pelicula in lista_peliculas:
                    if plataforma in pelicula["Plataformas"]:
                        imprimir_info_pelicula(pelicula)
                print("*" * 150)
            case 7:
                salir = respuesta_si_no("Desea salir? Si/No: ")
                if salir:
                    print("Saliendo...")
                    return
            case _:
                print("Opción no válida.")

        continuar = respuesta_si_no("Desea realizar otra consulta? Si/No: ")
        if not continuar:
            print("Saliendo...")
            break

def ordenar_peliculas(lista_peliculas):#Muestra un submenu y ordena las peliculas dependiendo lo que elija el usuario
    while True:
        opcion = get_int("""Seleccione una opción de ordenamiento:\n
                            1. Título\n
                            2. Género\n
                            3. Año de lanzamiento\n
                            4. Duración\n
                            5. Salir\n""", "Error, seleccione una opción válida", 1, 5)
        
        match opcion:
            case 1:
                orden = elegir_orden()
                lista_peliculas_ordenada = ordenar_peliculas_por_titulo(lista_peliculas, orden)
                if respuesta_si_no("¿Desea imprimir la lista de películas ordenadas por título? Si/No: "):
                    print("Películas ordenadas por título:")
                    for pelicula in lista_peliculas_ordenada:
                        imprimir_info_pelicula(pelicula)
            case 2:
                orden = elegir_orden()
                lista_peliculas_ordenada = ordenar_peliculas_por_genero(lista_peliculas, orden)
                if respuesta_si_no("¿Desea imprimir la lista de películas ordenadas por título? Si/No: "):
                    print("Películas ordenadas por título:")
                    for pelicula in lista_peliculas_ordenada:
                        imprimir_info_pelicula(pelicula)
            case 3:
                orden = elegir_orden()
                lista_peliculas_ordenada = ordenar_peliculas_por_año(lista_peliculas, orden)
                if respuesta_si_no("¿Desea imprimir la lista de películas ordenadas por título? Si/No: "):
                    print("Películas ordenadas por título:")
                    for pelicula in lista_peliculas_ordenada:
                        imprimir_info_pelicula(pelicula)
            case 4:
                orden = elegir_orden()
                lista_peliculas_ordenada = ordenar_peliculas_por_duracion(lista_peliculas, orden)
                if respuesta_si_no("¿Desea imprimir la lista de películas ordenadas por título? Si/No: "):
                    print("Películas ordenadas por título:")
                    for pelicula in lista_peliculas_ordenada:
                        imprimir_info_pelicula(pelicula)
            case 5:
                if not respuesta_si_no("Desea ordenar las peliculas de otra manera? Si/No: "):
                    break

def buscar_pelicula(lista_peliculas):#Busca una pelicula e imprime su informacion
    while True:
        titulo = get_str("Ingrese el título de la película a buscar: ", 1, 30)
        pelicula_encontrada = buscar_pelicula_por_titulo(lista_peliculas, titulo)
        
        if pelicula_encontrada:
            print("Película encontrada:")
            imprimir_info_pelicula(pelicula_encontrada)
        else:
            print("No se encontró ninguna película con ese título.")
        
        continuar = respuesta_si_no("¿Desea buscar otra película? Si/No: ")
        if not continuar:
            break

def calcular_peliculas(lista_peliculas):#calcula la duracion promedio de todas las peliculas o las peliculas lanzadas entre 2005 y 2024
    while True:
        opcion = get_int("""Seleccione una opción de cálculo:\n
                            1. Duración promedio de todas las películas\n
                            2. Cantidad de películas lanzadas en cada año (2005-2024)\n
                            3. Salir\n""", "Error, seleccione una opción válida", 1, 3)
        
        match opcion:
            case 1:
                promedio_duracion = calcular_duracion_promedio(lista_peliculas)
                print(f"La duración promedio de todas las películas es: {promedio_duracion:.2f} minutos.")
            case 2:
                conteo_por_año = contar_peliculas_por_año(lista_peliculas)
                print("Cantidad de películas lanzadas en cada año (2005-2024):")
                for año, cantidad in conteo_por_año.items():
                    print(f"{año}: {cantidad} películas")
            case 3:
                if not respuesta_si_no("¿Desea realizar otro cálculo? Si/No: "):
                    break

def porcentaje_peliculas(lista_peliculas):#Muestra un submenu y muestra(segun la opcion) el porcentaje que representan las peliculas por su genero o ATP
    while True:
        opcion = get_int("""Seleccione una opción de cálculo de porcentaje:\n
                            1. Porcentaje por género\n
                            2. Porcentaje por ATP\n
                            3. Salir\n""", "Error, seleccione una opción válida", 1, 3)
        
        match opcion:
            case 1:
                calcular_porcentaje_genero(lista_peliculas)
            case 2:
                calcular_porcentaje_ATP(lista_peliculas)
            case 3:
                if not respuesta_si_no("¿Desea realizar otro cálculo? Si/No: "):
                    break

