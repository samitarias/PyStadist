class Coordenada:
    """ Coordenada
    
    Se encarga de mover al borracho según las coordenadas que
    se le pasen sen su inicialización. Tambiéén se encarga de
    calcular la distancia (hipotenusa) entre dos coordenadas.

    Atributos:
    x (integer): Ordenada x
    y (integer): Ordenada y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        """ Mueve al borracho según los deltas pasados
        como parámetros
        
        Parámetros:
        delta_x (integer): Nueva ubicación en la ordenada x.
        delta_y (integer): Nueva ubicación en la ordenada y.

        Return:
        Regresa una nueva instancia de la clase de Coordenada.
        """
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        """ Calcula la distancia entre dos coordenadas.
        
        Parámetros:
        otra_coordenada (Coordenada): Instancia de la clase Coordenada.

        Return:
        Devuleve la hipotenuza o distancia de la diferencia entre las
        coordenas de ambas instancias de Coordenadas. 
        """
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y 

        return (delta_x**2 + delta_y**2)**0.5