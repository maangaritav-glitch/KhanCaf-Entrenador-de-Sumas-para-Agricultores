"""
Khancafe: Entrenador de sumas en Python.

Un programa de consola que genera sumas aleatorias de dos dígitos
y entrena al usuario hasta que logra varias respuestas correctas seguidas.
"""

from random import randint

RESPUESTAS_CORRECTAS_REQUERIDAS = 3
MIN_NUM = 10
MAX_NUM = 99


def generar_numero_aleatorio():
    """
    Devuelve un número aleatorio entre MIN_NUM y MAX_NUM (ambos inclusive).
    """
    return randint(MIN_NUM, MAX_NUM)


def verificar_respuesta(num1, num2, respuesta_usuario):
    """
    Recibe dos números y la respuesta del usuario.
    Devuelve True si la respuesta es correcta, False en caso contrario.
    """
    suma_correcta = num1 + num2
    return respuesta_usuario == suma_correcta


def hacerle_una_pregunta():
    """
    Genera una suma aleatoria, pide la respuesta al usuario
    e imprime si es correcta o no.

    Devuelve True si la respuesta es correcta, False si es incorrecta.
    """
    num1 = generar_numero_aleatorio()
    num2 = generar_numero_aleatorio()

    print(f"Cuánto es {num1} + {num2}?")
    entrada = input("Tu respuesta: ")

    # Manejar entradas no numéricas
    try:
        respuesta_usuario = int(entrada)
    except ValueError:
        print("Por favor ingresa un número entero.")
        return False

    if verificar_respuesta(num1, num2, respuesta_usuario):
        print("Correcto!")
        return True
    else:
        suma_correcta = num1 + num2
        print(f"Incorrecto, la respuesta es {suma_correcta}")
        return False


def jugar_entrenador():
    """
    Lógica principal del entrenador:
    cuenta cuántas respuestas correctas seguidas lleva el usuario
    y termina cuando alcanza RESPUESTAS_CORRECTAS_REQUERIDAS.
    """
    print("Khancafe - Entrenador de sumas")
    print(f"Necesitas {RESPUESTAS_CORRECTAS_REQUERIDAS} respuestas correctas seguidas.\n")

    correctas_seguidas = 0

    while correctas_seguidas < RESPUESTAS_CORRECTAS_REQUERIDAS:
        respondio_correctamente = hacerle_una_pregunta()

        if respondio_correctamente:
            correctas_seguidas += 1
            print(f"Has ingresado {correctas_seguidas} bien seguidos.\n")
        else:
            correctas_seguidas = 0
            print("El contador se ha reiniciado.\n")

    print("Felicidades! Has dominado las sumas.")


def main():
    jugar_entrenador()


if __name__ == "__main__":
    main()
