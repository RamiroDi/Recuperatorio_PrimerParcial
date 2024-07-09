import sys
from Package_operaciones import *
from peliculas import *
import os

lista_peliculas = cargar_peliculas()

bandera_permitir = False

while True:#Menu principal
    opcion = get_int("""Seleccione una opción.\n
                     1. Dar de alta.\n
                     2. Modificar.\n
                     3. Eliminar\n
                     4. Mostrar películas.\n
                     5. Ordenar películas.\n
                     6. Buscar películas.\n
                     7. Calcular\n
                     8. Calcular porcentaje.\n
                     9. Salir\n""", "Error seleccione una opcion valida", 1,9)

    match opcion:
        case 1:
            agregar_pelicula(lista_peliculas)#Agrega una pelicula
            bandera_permitir = True
        case 2:
            if bandera_permitir:
                modificar_pelicula(lista_peliculas)#Modifica una pelicula solo si se dio de alta una
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 3:
            if bandera_permitir:
                os.system('cls')
                eliminar_pelicula(lista_peliculas)#Elimina una pelicula solo si se dio de alta una
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 4:
            if bandera_permitir:
                os.system('cls')
                mostrar_peliculas(lista_peliculas)#Muestra las peliculas solo si se dio de alta una
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 5:
            if bandera_permitir:
                os.system('cls')
                ordenar_peliculas(lista_peliculas)#Ordena las peliculas solo si se dio de alta una
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 6:
            if bandera_permitir:
                os.system('cls')
                buscar_pelicula(lista_peliculas)#Busca la pelicula solo si se dio de alta una
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 7:
            if bandera_permitir:
                os.system('cls')
                calcular_peliculas(lista_peliculas)#Calcula las peliculas dependiendo lo que ingrese el usuario solo si se dio de alta una pelicula
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 8:
            if bandera_permitir:
                os.system('cls')
                porcentaje_peliculas(lista_peliculas)#Hace el porcentaje dependiendo lo que ingrese el usuario solo si se dio de alta una pelicula
            else:
                os.system('cls')
                print("Debe haber dado de alta al menos una película.")
        case 9:
            print("Guardando películas...")
            guardar_peliculas(lista_peliculas)#Guarda las peliculas para cerrar el programa
            print("¡Gracias por usar nuestro programa!")
            break
