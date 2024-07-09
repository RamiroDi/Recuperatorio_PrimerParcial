# Realizar un paquete denominado Package_Input, el mismo deberá contener los siguientes módulos:
# Input.py
#   get_int()

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    while True:
        numero = input(mensaje)
        if numero.isdigit() and minimo <= int(numero) <= maximo:
            return int(numero)
        else:
            print(mensaje_error)


#   get_float()

def get_float(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:
    
    numero = float(input(mensaje))
    reintentos -= 1
    while numero < minimo or numero > maximo:
        numero = float(input(mensaje_error))

        reintentos -= 1
        if reintentos == 0:
            print("Se quedo sin intentos.")
            break

    return numero


def get_str(cadena: str, min_length: int, max_length: int) -> str | None:
    while True:
        entrada = input(cadena)
        if len(entrada) >= min_length and len(entrada) <= max_length:
            for letra in entrada:
                if ord(letra) >= 32 or ord(letra) <= 126:
                    return entrada
        else:
            print("La entrada no es válida. Debe contener solo caracteres alfabéticos y estar entre", min_length, "y", max_length, "caracteres.")
