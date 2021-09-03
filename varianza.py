import random
import math
def media(X):
    return sum(X)/len(X)
def varianza(X):
    mu=media(X)
    acumulador=0
    for i in  X:
        acumulador+=(i-mu)**2
    return acumulador/len(X)
def desv_Estandar(X):
    return math.sqrt(varianza(X))
def opc():
    aux=True
    while aux:
            aux=input("Desea escribir una lista o que se genere aleatoriamente? Digite 1 para aleatorio o 2 para lista de numeros \n 1. Aleatorio\n 2. Lista de numeros\n 3. Para salir\n")
            if aux =="1":
                X=[random.randint(1,21) for i in range(20)]
                mu=media(X)
                print(f'La media de {len(X)} numeros  es {mu} ')
                mu=varianza(X)
                print(f'La varianza de {len(X)} numeros  es {mu} ')
                mu=desv_Estandar(X)
                print(f'La desviación estandar de {len(X)} numeros  es {mu} ')
            elif aux=="2":
                lista=[]
                limite=int(input("Digite limite de la lista: "))
                for i in range(limite):
                    numero=int(input("Digite numero: "))
                    lista.append(numero)
                    longi=media(lista)
                    longi2=varianza(lista)
                    longi3=desv_Estandar(lista)
                print("La media es:",longi)
                print("La varianza es:",longi2)
                print("La desviación estandar es:",longi3)
            elif aux=="3":
                break
            elif aux !="":
                print("Debe digitar una opción")


    
if __name__=='__main__':
    opc()
