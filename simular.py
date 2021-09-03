from coordenada import Coordenada
from campo import Campo
from caminata import caminata
def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    """ Simula caminatas
    
    Parámetros:
    pasos (integer): Número de pasos que dará un borracho (caminata).
    numero_de_intentos: Número de veces que se realizará la caminata.
    tipo_de_borracho: instancia de un tipo de Borracho.
    
    Return:
    (list) Regresa una lista de distancias (ver. Fn caminata)
    """
    borracho = tipo_de_borracho(nombre='MrNoName')
    origen = Coordenada(0, 0)
    distancias = []
    
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias