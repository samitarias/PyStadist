def caminata(campo, borracho, pasos):
    """ Ejecuta la función mover_borracho de la
    instancia de Campo tantas veces como pasos haya.

    Parámetros:
    campo (instancia de Campo):
    borracho (instancia de Borracho):
    pasos (integer): 

    Return:
    (integer) Regresa la distancia respecto de la última posición del
    borracho con la posición de inicio.
    """
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))