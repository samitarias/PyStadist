class Campo:
    """ Campo
    
    Crea el espacio en el que se va a mover el borracho.

    Atributos:
    coordenadas_de_borrachos (dict): Diccionario en el que
    se guardarán las coordenadas de los borrachos segúún avancen,
    en la forma { nombre_borracho: instancia de Coordenada, ... }
    """
    
    def __init__(self):
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self, borracho, coordenada):
        """ Añade un borracho a coordenadas_de_borrachos. """
        self.coordenadas_de_borrachos[borracho] = coordenada
    
    def mover_borracho(self, borracho):
        """ Mueve al borracho, es decir, obtiene las coordenadas
        de un borracho (recuerda que se obtienen de forma random)
        estas coordenadas se usan para obtener nuevas coordenadas
        con la función "mover" de la instancia de Coordenada 
        "coordenada_actual", las nuevas coordenadas nuevas reemplazan 
        las coordenadas anteriores del borracho."""
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada
    
    def obtener_coordenada(self, borracho):
        """ Se obtienen las coordenadas de un borracho del 
        atributo de clase coordenadas_de_borrachos que almacena
        instancias de Coordenadas."""
        return self.coordenadas_de_borrachos[borracho]