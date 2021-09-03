import random
import math
def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        
        x = random.random() * random.choice([-1, 1])
        #print(f'Imprime X: {x}')
        y = random.random() * random.choice([-1, 1])
        # print(f'Imprime Y: {y}')
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_de_agujas

if __name__=='__main__':
   print( aventar_agujas(10000000)) 