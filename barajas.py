import random
import collections
PALOS=['espada','corazon','rombo','trebol']
VALORES=['as','2','3','4','5','6','7','8','9','jota','q','k']

def crear_baraja():
    barajas=[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas

def obtener_mano(barajas,tamano_mano):
    mano=random.sample(barajas,tamano_mano)
    return mano
def main(tamano_mano,intentos):
    barajas=crear_baraja()
    manos=[]
    for _ in range(intentos):
        mano=obtener_mano(barajas,tamano_mano)
        manos.append(mano)
    #print(manos)
    pares=0
    for mano in manos:
        valores=[]
        for carta in mano:
            valores.append(carta[1])
        counter=dict(collections.Counter(valores))
        
        for val in counter.values():
            if val == 2:
                pares+= 1
                break
    probabilidad_par=pares/intentos
    print(f'La probalidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par} en {intentos} intentos')
if __name__=='__main__':
    barajas=crear_baraja()
    mano=obtener_mano(barajas,5)
    tamano_mano=int(input('De cuantas barajas será la mano?: '))
    intentos=int(input('Cuantos intentos?: '))
    main(tamano_mano,intentos)
    #print(mano)
    #print(barajas)