from simular import simular_caminata
def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    """ Función que ejecuta todo el proceso de caminos aleatoreos. 
    Imprime en pantalla los resultados. 
    
    Parámetros: 
    distancias_de_caminata (list): Lista de enteros.
    numero_de_intentos (integer): Número de veces que se repetirán las caminatas.
    tipo_de_borracho (instancia de un tipo de Borracho): Borracho a analisar.
    """
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__}')
        print(f'Media={distancia_media}')
        print(f'Máxima={distancia_maxima}')        
        print(f'Mínima={distancia_minima}')
        print('*' * len(tipo_de_borracho.__name__))