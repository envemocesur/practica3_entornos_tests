import getpass
import logging


def introduzca_numero(frase="introduzca numero: "):
    try:
        n = int(getpass.getpass(frase))
        frase = "ValueError - introduzca numero entero mayor a 0: "
        return n if n > 0 else introduzca_numero(frase)
    except ValueError as valueError:
        logging.error(valueError)
        frase = "ValueError - introduzca numero entero: "
        return introduzca_numero(frase)


def adivine_numero(frase="adivine numero: "):
    try:
        n = int(input(frase))
        frase = "ValueError - introduzca numero entero mayor a 0: "
        return n if n > 0 else adivine_numero(frase)
    except ValueError as valueError:
        logging.error(valueError)
        return adivine_numero(frase="ValueError - introduzca numero entero: ")


def get_str_intentos(lista_intentos):
    str_intentos = ''
    for intento in lista_intentos:
        str_intentos += str(intento) + ', '
    else:
        str_intentos = str_intentos[:-2]
        str_intentos += '.'
    return str_intentos


def mostrar_intentos(lista_intentos, tipo):
    if len(lista_intentos) > 0:
        str_intentos = get_str_intentos(lista_intentos)
        frase = 'Los intentos ' + tipo + 'fueron los siguientes: '
        print(frase + str_intentos)


def contar_palabras(palabras):
    NUMERO = len(palabras)
    return NUMERO


def definir_variables_juego():
    FRASE = getpass.getpass("Introduzca frase: ")
    palabras = FRASE.split(' ')
    NUMERO = contar_palabras(palabras)
    return FRASE, palabras, NUMERO


def generar_frase(FRASE, lista_intentos_letra_totales):
    frase_acertar = ""
    for _letra in FRASE:
        caracter = '+'
        if _letra == ' ':
            caracter = ' '
        for __letra in lista_intentos_letra_totales:
            if _letra == __letra:
                caracter = _letra
        frase_acertar += caracter
    return frase_acertar


def devuelve_correcto_adivinar(NUMERO, ADIVINAR, INTENTOS):
    if NUMERO > ADIVINAR:
        frase = 'Intento erróneo. El número a adivinar es mayor. '
        return frase + str(INTENTOS) + ' intentos disponibles.'
    elif NUMERO < ADIVINAR:
        frase = 'Intento erróneo. El número a adivinar es menor. '
        return frase + str(INTENTOS) + ' intentos disponibles.'


def mostrar_intentos_letra(letra, FRASE, INTENTOS, frase_acertar):
    if letra in FRASE:
        INTENTOS += 1
        frase = 'Intento correcto. Existe la letra '
        print(frase + letra + '. ' + frase_acertar + '. ' + str(
            INTENTOS) + ' intentos disponibles.')
    else:
        frase = 'Intento erróneo. No existe la letra '
        print(frase + letra + '. ' + frase_acertar + '. ' + str(
            INTENTOS) + ' intentos disponibles.')
    return INTENTOS


def hasAcertado(ACERTAR, FRASE):
    if ACERTAR is True:
        return 'Has acertado la frase!'
    else:
        return 'Fallaste. La frase es ' + FRASE


def acertar_palabra(palabra, palabras, frase_acertar, INTENTOS):
    if palabra in palabras:
        INTENTOS += 1
        frase = 'Intento correcto. Existe la palabra '
        frase = frase + palabra + '. ' + frase_acertar + '. ' + str(
            INTENTOS) + ' intentos disponibles.'
    else:
        frase = 'Intento erróneo. No existe la palabra '
        frase = frase + palabra + '. ' + frase_acertar + '. ' + str(
            INTENTOS) + ' intentos disponibles.'
    return frase, INTENTOS


def acertar(frase, FRASE, INTENTOS):
    if frase == FRASE:
        return True
    else:
        print('Intento erróneo. ' + str(INTENTOS) + ' intentos disponibles.')
        return False


def opcionValida(opcion):
    if opcion in ('2', '1', '0'):
        return int(opcion)


def elegirOpcion():
    opcion = input('elige un nº entre el 0 y el 2: ')
    opcion = opcionValida(opcion)
    if opcion not in (0, 1, 2):
        opcion = elegirOpcion()
    return opcion


def jugar():
    FRASE, palabras, NUMERO = definir_variables_juego()
    INTENTOS = adivine_numero(frase="introduzca intentos permitidos: ")
    lista_intentos_palabras = list()
    lista_intentos_letra = list()
    lista_intentos_palabra = list()
    lista_intentos_frase = list()
    lista_intentos_letra_totales = list()
    ADIVINAR = 0
    frase_acertar = ""
    while NUMERO != ADIVINAR and INTENTOS > 0:
        ADIVINAR = adivine_numero("adivine numero de palabras: ")
        INTENTOS -= 1
        lista_intentos_palabras.append(ADIVINAR)
        print(devuelve_correcto_adivinar(NUMERO, ADIVINAR, INTENTOS))
    if NUMERO == ADIVINAR:
        print('Ha acertado el número!')
        INTENTOS += 1  # recuperamos el intento
        ACERTAR = False
        while ACERTAR is False and INTENTOS > 0:
            INTENTOS -= 1
            print('adivine letra introduzca 2')
            print('adivine palabra introduzca 1')
            print('adivine frase introduzca 0:')
            opcion = elegirOpcion()
            if opcion == 2:
                letra = input("adivine letra: ")
                lista_intentos_letra.append(letra)
                lista_intentos_letra_totales.append(letra)
                lista = lista_intentos_letra_totales
                frase_acertar = generar_frase(FRASE, lista)
                v1 = letra
                v2 = FRASE
                v3 = INTENTOS
                v4 = frase_acertar
                INTENTOS = mostrar_intentos_letra(v1, v2, v3, v4)
            elif opcion == 1:
                palabra = input("adivine palabra: ")
                lista_intentos_palabra.append(palabra)
                for letra in palabra:
                    lista_intentos_letra_totales.append(letra)
                    lista = lista_intentos_letra_totales
                    frase_acertar = generar_frase(FRASE, lista)
                v1 = palabra
                v2 = palabras
                v3 = frase_acertar
                v4 = INTENTOS
                frase, INTENTOS = acertar_palabra(v1, v2, v3, v4)
                print(frase)
            elif opcion == 0:
                frase = input("adivine frase: ")
                lista_intentos_frase.append(frase)
                ACERTAR = acertar(frase, FRASE, INTENTOS)
            else:
                INTENTOS += 1
                print('opción inválida')
        print(hasAcertado(ACERTAR, FRASE))
    else:
        print('Fallaste. El numero es ' + str(NUMERO))
    ##################

    ##################
    mostrar_intentos(lista_intentos_palabras, 'de numero de palabras ')
    mostrar_intentos(lista_intentos_letra, 'de letras ')
    mostrar_intentos(lista_intentos_palabra, 'de palabras ')
    mostrar_intentos(lista_intentos_frase, 'de frases ')


if __name__ == '__main__':
    jugar()
