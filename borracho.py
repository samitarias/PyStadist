import random
class Borracho:
    """ Borracho padre
    
    Atributos:
    nombre (string): Nombre del borracho
    """

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    """ Borracho tradicional
    Clase hija de Borracho.

    Atributos:
    nombre (string): Nombre del borracho
    """

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        """ Regresa una tubla que represenata una coordenada. """
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])