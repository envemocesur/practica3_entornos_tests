from adivina_palabra import introduzca_numero, contar_palabras, \
    generar_frase, devuelve_correcto_adivinar, mostrar_intentos_letra, \
    hasAcertado, acertar_palabra, acertar, opcionValida, get_str_intentos


##################################################################

# 1. aquí comprobamos que la función solo deja introducir enteros
def test_introduzca_numero():
    assert isinstance(introduzca_numero(), int)


# 2. aquí comprobamos que la función cuenta tres palabras
def test_contar_palabras():
    assert contar_palabras(["uno", "dos", "tres"]) == 3


# 3. comprobamos que se muestra correctamente la parte acertada de la frase
def test_generar_frase():
    frase = "me ++am+ en++++e"
    assert generar_frase('me llamo enrique', ['m', 'e', 'a', 'n']) == frase


# 4. cuando imprimimos los resultados del último intento
def test_devuelve_correcto_adivinar():
    erroneo = 'Intento erróneo. '
    frase = erroneo + 'El número a adivinar es menor. 2 intentos disponibles.'
    assert devuelve_correcto_adivinar(6, 7,
                                      2) == frase
    frase = erroneo + 'El número a adivinar es mayor. 3 intentos disponibles.'
    assert devuelve_correcto_adivinar(7, 6,
                                      3) == frase


# 5. actualiza el numero de intentos según el caso
def test_mostrar_intentos_letra():
    assert mostrar_intentos_letra('a', 'uno dos tres', 5, '*** *** ****') == 5
    assert mostrar_intentos_letra('o', 'uno dos tres', 5, '**o *o* ****') == 6


# 6. ¿has acertado la frase?
def test_hasAcertado():
    acertaste = 'Has acertado la frase!'
    assert hasAcertado(True, 'uno dos tres') == acertaste
    fallaste = 'Fallaste. La frase es uno dos tres'
    assert hasAcertado(False, 'uno dos tres') == fallaste


# 7. devuelve bien los dos valores: la frase a devolver y el numero de intentos
def test_acertar_palabra():
    lista = ('palabra', 'hola')
    correcto = 'Intento correcto. Existe la palabra '
    assert acertar_palabra('palabra', lista, 'frase_acertar', 8) == (
        correcto + 'palabra. frase_acertar. 9 intentos disponibles.', 9)
    erroneo = 'Intento erróneo. No existe la palabra '
    assert acertar_palabra('uno', lista, 'frase_acertar', 8) == (
        erroneo + 'uno. frase_acertar. 8 intentos disponibles.', 8)


# 8. devuelve True o False en función de si has acertado la frase o no
def test_acertar():
    assert acertar('uno', 'uno', 2) is True
    assert acertar('uno', 'dos', 2) is False


# 9. solo acepta y devuelve un valor que sea 0, 1 y 2
def test_opcionValida():
    assert opcionValida('0') == 0
    assert opcionValida('1') == 1
    assert opcionValida('2') == 2
    assert opcionValida('3') is None
    assert opcionValida('hola') is None


# 10. muestra la lista de intentos correctamente si existen
def test_get_str_intentos():
    assert get_str_intentos((1, 2, 3)) == '1, 2, 3.'
    assert get_str_intentos(('uno', 'dos', 'tres')) == 'uno, dos, tres.'
    assert get_str_intentos(['hola']) == 'hola.'
    assert get_str_intentos('hola') == 'h, o, l, a.'
    assert get_str_intentos(list()) == '.'
